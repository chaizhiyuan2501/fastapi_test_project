import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8000))
sock.listen(5)

while 1:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("クライアントからリクエスト:\n", data)
    conn.send(b"HTTP/1.1 200 ok\r\nserver:test\r\n\r\nhello world")
    conn.close()
