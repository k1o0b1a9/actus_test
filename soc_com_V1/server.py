# -*- coding:utf-8 -*-
import socket

host = socket.gethostname() #ホスト名取得
port = 8765 #PORT指定(クライアントと一致していればOK)

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

print('Waiting for connections...')
clientsock, client_address = serversock.accept() #接続されればデータを格納

while True:

    rcvmsg = clientsock.recv(4096).decode()
    print(type(rcvmsg))
    if rcvmsg == 'exit':
        break
    
    print(rcvmsg)
    #rcvmsg=rcvmsg.encode('utf-8')
    clientsock.sendall(rcvmsg.encode('utf-8')) #メッセージを返します

#クローズ処理 
print("Now Closing")
clientsock.close()