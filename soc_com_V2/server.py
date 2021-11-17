# -*- coding:utf-8 -*-
import socket

host = socket.gethostname() #ホスト名取得
port = 8080 #PORT指定(クライアントと一致していればOK)

print(host)
serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(1) #接続の待ち受けをします（キューの最大数を指定）

print('Waiting for connections...')
clientsock, client_address = serversock.accept() #接続されればデータを格納

while True:
    
    #strでクライアントプログラムからの入力を受け取る
    rcvmsg = clientsock.recv(4096).decode()
    #入力された文字列がexitであった場合、その時点で処理終了
    if rcvmsg == 'exit':
        break
    
    #数値単独の場合そのまま代入
    if(str.isdigit(rcvmsg))==True:
        sndmsg=rcvmsg
    #=のあとに数値が続いている場合もそのまま代入
    elif (rcvmsg.find("="))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("=")+1):]))==True:
            sndmsg = rcvmsg[(rcvmsg.find("=")+1):]
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            clientsock.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #足し算
    elif (rcvmsg.find("+"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("+")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg += float(rcvmsg[(rcvmsg.find("+")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            clientsock.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #引き算
    elif (rcvmsg.find("-"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("-")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg -= float(rcvmsg[(rcvmsg.find("-")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            clientsock.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #掛け算    
    elif (rcvmsg.find("*"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("*")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg *= float(rcvmsg[(rcvmsg.find("*")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            clientsock.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #割り算
    elif (rcvmsg.find("/"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("/")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg /= float(rcvmsg[(rcvmsg.find("/")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            clientsock.sendall("数値を入力してください".encode('utf-8')) 
            continue
    else:
            #文字列の場合、エラーを直接送りもう一度入力
            clientsock.sendall("数値を入力してください".encode('utf-8')) 
            continue
    
    sndmsg=str(sndmsg)
    
    clientsock.sendall(sndmsg.encode('utf-8')) #メッセージを返します

#クローズ処理 
print("Now Closing")
clientsock.close()