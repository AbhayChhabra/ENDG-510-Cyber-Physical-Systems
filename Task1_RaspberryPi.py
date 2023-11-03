import socket
import time
import Adafruit_DHT

s= socket.socket()

port = 12345
s.connect(('172.20.10.2',port))

while True:
    humidity,temperature = Adafruit_DHT.read_retry(11,4)

    data= str(temperature) + " " + str(humidity)
    print(data)

    s.send(data.encode())

    time.sleep(1)

s.close()
