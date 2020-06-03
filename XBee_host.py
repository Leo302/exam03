import serial
import time

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY <BASE_MY>\r\n".encode())
char = s.read(3)
print("Set MY <BASE_MY>.")
print(char.decode())

s.write("ATDL <BASE_DL>\r\n".encode())
char = s.read(3)
print("Set DL <BASE_DL>.")
print(char.decode())

s.write("ATID <PAN_ID>\r\n".encode())
char = s.read(3)
print("Set PAN ID <PAN_ID>.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
while True:
    # send RPC to remote
    s.write(bytes("\r", 'UTF-8'))
    line=s.readline() # Read an echo string from K66F terminated with '\n' (pc.putc())
    print(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/getAcc/run\r", 'UTF-8'))
    line=s.readline() # Read an echo string from K66F terminated with '\n' (pc.putc())
    print(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/getAddr/run\r", 'UTF-8'))
    line=s.readline() # Read an echo string from K66F terminated with '\n' (pc.putc())
    print(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)
    s.close()