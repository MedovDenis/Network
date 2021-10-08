import socket
import requests

PORT = 80
HTTPS = 'https://'
HOST = 'www.ssau.ru'
LOCATION = 'index.html'

# mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect((HOST,PORT))

# msg = 'GET {}ssau.ru HTTP/1.0\r\nHost:{}\r\n\r\n'.format(HTTPS, HOST)
# mysocket.sendall(msg.encode())

# while True:
#     data = mysocket.recv(1024)
#     if len(data) < 1:
#         break
#     data.rstrip()

#     info = data.decode()
#     print(info)
#     start = info.find('Location:')
#     end = info.find('Date:')

#     location = info[start + 10:end - 1]
#     print(location)

# mysocket.close()

r = requests.get('https://ssau.ru/index')
print(r.text)
