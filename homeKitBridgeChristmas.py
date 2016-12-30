import socket
import sys
from time import sleep
import serial

#setup UDP server port
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))

#setup serial port for the arduino
#ser = serial.Serial('/dev/ttyACM0', 9600)


print "waiting on port:", port
while 1:
    data, addr = s.recvfrom(1024)
    print data

#sleep(2)
#hue = int(sys.argv[1])
#saturation = int(sys.argv[2])
#brightness = int(sys.argv[3])

#print hue + saturation

#hue_mapped = int((hue) * (255) / 359)
#saturation_mapped = int((saturation) * (255) / 100 )
#brightness_mapped = int((brightness) * (255) / 100 )
#n = ser.write('A'+chr(hue_mapped)+chr(saturation_mapped)+chr(brightness_mapped)+'\n')
#n = ser.write('A')
#sleep(0.1)
#n = ser.write(chr(hue_mapped))
#sleep(0.1)
#n = ser.write(chr(saturation_mapped))
#sleep(0.1)
#n = ser.write(chr(brightness_mapped))
#sleep(0.1)
#n = ser.write('\n')
#print n
#print hue_mapped
#print saturation_mapped
#print brightness_mapped
#sleep(0.5)


