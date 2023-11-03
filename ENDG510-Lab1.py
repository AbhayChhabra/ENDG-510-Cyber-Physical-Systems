import socket
import pandas as pd 

df = pd.DataFrame(columns = ['Temp', 'Humd', 'Label'])

s = socket.socket()
print("Socket succesfully created")
port = 12345
s.bind(('', port))
print("socket binded to %s"%(port))
s.listen(5)
print("socket is listening gyattttt")

c,addr = s.accept()
print("got connection from", addr)

i = 700

while i>=0:

    client = c.recv(1024)
    data= client.decode()
    temp = data.split(" ")[0]
    hum = data.split(" ")[1]
    new_data = {
        'Temp': temp,
        'Humd': hum,
        'Label': 1
    }
    df = df.append(new_data, ignore_index=True)

    print(data)
    i = i-1

c.close()
df.to_csv('data.csv',index=False)
