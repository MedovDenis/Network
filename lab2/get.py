import socket

def get(url):
    client_socket = socket.socket()
    server_address = (url, 80)
    client_socket.connect(server_address)

    request = '''GET / HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36
Host: {}

'''.format(url)


    client_socket.send(request.encode())
    mod_request = client_socket.recv(1024).decode()
    client_socket.close()

    return mod_request