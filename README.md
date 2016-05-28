# fpv-gcc
Analysing (MSP430-)GCC generated Map files for measuring code footprint

Example output with an MSP430-ELF-GCC map file
----------------------------------------------

    +--------------------------------+--------+----------+-------+------+-------+-------+
    | FILE                           | VECT52 | RESETVEC |   ROM |  RAM | HIROM | TOTAL |
    +--------------------------------+--------+----------+-------+------+-------+-------+
    | TOTALS                         |      2 |        2 | 14504 | 1314 |     0 |       |
    | libusb-api-msp430f5529.a       |      0 |        0 |  6580 |  200 |     0 |  6780 |
    | libdriverlib-msp430f5529.a     |      0 |        0 |  1756 |    8 |     0 |  1764 |
    | libprintf-msp430f5529.a        |      0 |        0 |  1314 |    0 |     0 |  1314 |
    | UsbIsr.c.obj                   |      2 |        0 |  1252 |    0 |     0 |  1254 |
    | libusb-config-msp430f5529.a    |      0 |        0 |  1034 |    2 |     0 |  1036 |
    | libmodbus-msp430f5529.a        |      0 |        0 |    70 |  612 |     0 |  682  |
    | libgcc.a                       |      0 |        0 |   546 |    0 |     0 |  546  |
    | libbc-iface-usb-msp430f5529.a  |      0 |        0 |   304 |  212 |     0 |  516  |
    | main.c.obj                     |      0 |        0 |   358 |   22 |     0 |  380  |
    | crtbegin.o                     |      0 |        0 |   344 |   24 |     0 |  368  |
    | libbytebuf-msp430f5529.a       |      0 |        0 |   270 |    0 |     0 |  270  |
    | libucdm-msp430f5529.a          |      0 |        0 |     0 |  224 |     0 |  224  |
    | libhal-uc-core-msp430f5529.a   |      0 |        0 |   154 |    0 |     0 |  154  |
    | libusb-app-msp430f5529.a       |      0 |        0 |   136 |    0 |     0 |  136  |
    | libcontrol-iface-msp430f5529.a |      0 |        0 |   100 |    0 |     0 |  100  |
    | libc.a                         |      0 |        0 |    82 |    0 |     0 |   82  |
    | crt0.o                         |      0 |        2 |    72 |    0 |     0 |   74  |
    | crtend.o                       |      0 |        0 |    48 |    2 |     0 |   50  |
    | libcrt.a                       |      0 |        0 |    44 |    0 |     0 |   44  |
    | libprbs-msp430f5529.a          |      0 |        0 |    22 |    0 |     0 |   22  |
    | libboard-funcs-msp430f5529.a   |      0 |        0 |     6 |    8 |     0 |   14  |
    | crtn.o                         |      0 |        0 |    12 |    0 |     0 |   12  |
    +--------------------------------+--------+----------+-------+------+-------+-------+

Example output with an AVR-GCC map file
---------------------------------------

    +-----------------+-------+------+--------+-------+
    | FILE            |  text | data | eeprom | TOTAL |
    +-----------------+-------+------+--------+-------+
    | TOTALS          | 43446 | 1266 |      0 |       |
    | Comm.o          |  7554 |   77 |      0 |  7631 |
    | Application.o   |  6875 |  442 |      0 |  7317 |
    | libsys.a        |  6041 |  168 |      0 |  6209 |
    | Calibration.o   |  4808 |    0 |      0 |  4808 |
    | libprintf_flt.a |  3580 |    0 |      0 |  3580 |
    | CM.o            |  1877 |   84 |      0 |  1961 |
    | libavr.a        |  1758 |  190 |      0 |  1948 |
    | libc.a          |  1700 |   10 |      0 |  1710 |
    | VM.o            |  1464 |   84 |      0 |  1548 |
    | CS.o            |  1405 |   61 |      0 |  1466 |
    | libm.a          |  1398 |    0 |      0 |  1398 |
    | VM2.o           |  1320 |   18 |      0 |  1338 |
    | VS.o            |  1092 |   61 |      0 |  1153 |
    | RM.o            |  1056 |   10 |      0 |  1066 |
    | libutils.a      |   614 |    0 |      0 |  614  |
    | SystemConfig.o  |   268 |   40 |      0 |  308  |
    | libgcc.a        |   300 |    0 |      0 |  300  |
    | Storage.o       |   252 |   12 |      0 |  264  |
    | LEDDisplay.o    |    56 |    9 |      0 |   65  |
    | crtm644.o       |    28 |    0 |      0 |   28  |
    +-----------------+-------+------+--------+-------+