"""
Copyright (C) 2015 Quazar Technologies Pvt. Ltd.
              2015 Chintalagiri Shashank

This file is part of fpv-gcc.

fpv-gcc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fpv-gcc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fpv-gcc.  If not, see <http://www.gnu.org/licenses/>.
"""


from ntreeSize import SizeNTree, SizeNTreeNode

memory_regions = None


class GCCMemoryMapNode(SizeNTreeNode):
    def __init__(self, parent=None, node_t=None,
                 name=None, address=None, size=None, fillsize=None,
                 arfile=None, objfile=None, arfolder=None):
        super(GCCMemoryMapNode, self).__init__(parent, node_t)
        self._leaf_property = '_size'
        self._ident_property = 'name'
        self._size = None
        if name is None:
            if objfile is not None:
                name = objfile
            else:
                name = ""
        self.name = name
        if address is not None:
            self._address = int(address, 16)
        else:
            self._address = None
        if size is not None:
            self._defsize = int(size, 16)
        else:
            self._defsize = None
        self.arfolder = arfolder
        self.arfile = arfile
        self.objfile = objfile
        self.fillsize = fillsize

    @property
    def address(self):
        if self._address is not None:
            return format(self._address, '#010x')
        else:
            return ""

    @address.setter
    def address(self, value):
        self._address = int(value, 16)

    @property
    def defsize(self):
        return self._defsize

    @defsize.setter
    def defsize(self, value):
        self._defsize = int(value, 16)

    @property
    def osize(self):
        return self._size

    @osize.setter
    def osize(self, value):
        self._size = int(value, 16)

    def add_child(self, newchild=None, name=None,
                  address=None, size=None, fillsize=0,
                  arfile=None, objfile=None, arfolder=None):
        if newchild is None:
            nchild = GCCMemoryMapNode(name=name, address=None, size=None,
                                      fillsize=0, arfile=None, objfile=None,
                                      arfolder=None)
            newchild = super(GCCMemoryMapNode, self).add_child(nchild)
        else:
            newchild = super(GCCMemoryMapNode, self).add_child(newchild)
        return newchild

    @property
    def leafsize(self):
        if self.fillsize is not None:
            if self._size is not None:
                return self._size + self.fillsize
            else:
                return self.fillsize
        return self._size

    @leafsize.setter
    def leafsize(self, value):
        raise AttributeError

    @property
    def region(self):
        if self._address is None:
            return 'UNDEF'
        tla = self.get_top_level_ancestor
        if tla is not None and tla is not self:
            if tla.region == 'DISCARDED':
                return 'DISCARDED TLA'
        if self._address == 0:
            return "DISCARDED"
        for region in memory_regions:
            if self._address in region:
                return region.name
        raise ValueError(self._address)

    def __repr__(self):
        r = '{0:.<60}{1:<15}{2:>10}{3:>10}    {5:<15}{4}'.format(self.gident, self.address or '',
                                                                 self.defsize or '', self.size or '',
                                                                 self.objfile or '', self.region,)
        return r


class GCCMemoryMap(SizeNTree):
    def __init__(self):
        node_t = GCCMemoryMapNode
        super(GCCMemoryMap, self).__init__(node_t)


class MemoryRegion(object):
    def __init__(self, name, origin, size, attribs):
        self.name = name
        self.origin = int(origin,16)
        self.size = int(size, 16)
        self.attribs = attribs

    def __repr__(self):
        r = "\n\nMemory Region :"
        r += "\n Name: " + self.name
        r += "\n Origin: " + hex(self.origin)
        r += "\n Size: " + str(self.size)
        r += "\n Attributes: " + self.attribs
        return r

    def __contains__(self, value):
        if not isinstance(value, int):
            value = int(value, 16)
        if self.origin <= value < (self.origin + self.size):
            return True
        else:
            return False