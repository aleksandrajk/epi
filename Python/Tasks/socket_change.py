import socket

# Input the URL you want to retrieve (e.g., 'http://example.com')
url = input("Enter URL: ")
url_parts = url.split('/')
host = url_parts[2]

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Initialize a flag to detect the end of headers
headers_received = False

# Collect and display data after headers and a blank line
while True:
    data = mysock.recv(1).decode()
    if not data:
        break

    if data == '\n':
        if headers_received:
            print(data, end='')
        else:
            headers_received = True
    else:
        headers_received = False

        # Display data after headers and a blank line
        print(data, end='')

mysock.close()
