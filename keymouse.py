NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

write_report(NULL_CHAR*2+chr(6)+chr(7)+chr(8)+chr(9)+chr(10)+chr(11))
write_report(NULL_CHAR*8)

NULL_CHAR = chr(0)

def ms_write(report):
    with open("/dev/hidg1", "wb+") as fd:
        fd.write(report.encode())

ms_write(NULL_CHAR+chr(100)+NULL_CHAR)
ms_write(NULL_CHAR+chr(200)+NULL_CHAR)
ms_write(NULL_CHAR+chr(300)+NULL_CHAR)
ms_write(NULL_CHAR+chr(400)+NULL_CHAR)
ms_write(NULL_CHAR+chr(100)+NULL_CHAR)
ms_write(NULL_CHAR+chr(200)+NULL_CHAR)
ms_write(NULL_CHAR+chr(300)+NULL_CHAR)
ms_write(NULL_CHAR+chr(400)+NULL_CHAR)
ms_write(NULL_CHAR+chr(100)+NULL_CHAR)

ms_write(NULL_CHAR*3)
