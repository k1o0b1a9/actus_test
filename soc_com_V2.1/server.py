# Echo server program
import socket
import sys

HOST = None               #ホスト名はクライアントに合わせるので不定
PORT = 8080              #クライアントに合わせて8080
s = None

#プロトコルを不定として環境に合わせてIPv4、IPv6にする
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
    
#本来クライアントプログラムからの操作で終了が正常な使用法だが
#万一サーバープログラムから終了しようとした場合に備えて実装
try:
    conn,addr= s.accept()   #acceptでは受信時に使用するオブジェクトとアドレス情報が生成されるのでアドレス情報用の変数も用意する
except KeyboardInterrupt as clientsock:
    print("とじる")
    sys.exit()

print('Waiting for connections...')

sndmsg=0 #未定義での参照防止のため

while True:
    
    #strでクライアントプログラムからの入力を受け取る
    rcvmsg = conn.recv(4096).decode()

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
            conn.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #足し算
    elif (rcvmsg.find("+"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("+")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg += float(rcvmsg[(rcvmsg.find("+")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            conn.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #引き算
    elif (rcvmsg.find("-"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("-")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg -= float(rcvmsg[(rcvmsg.find("-")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            conn.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #掛け算    
    elif (rcvmsg.find("*"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("*")+1):]))==True:
            sndmsg=float(sndmsg)
            sndmsg *= float(rcvmsg[(rcvmsg.find("*")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            conn.sendall("数値を入力してください".encode('utf-8')) 
            continue
    #割り算
    elif (rcvmsg.find("/"))!=-1:
        if(str.isdigit(rcvmsg[(rcvmsg.find("/")+1):]))==True:
            #0割になる場合は計算行わない
            if(int(rcvmsg[(rcvmsg.find("/")+1):]))==0:
                conn.sendall("0割です".encode('utf-8'))
                continue
            else:    
                sndmsg=float(sndmsg)
                sndmsg /= float(rcvmsg[(rcvmsg.find("/")+1):])
        else:
            #文字列の場合、エラーを直接送りもう一度入力
            conn.sendall("数値を入力してください".encode('utf-8')) 
            continue
    else:
            #文字列の場合、エラーを直接送りもう一度入力
            conn.sendall("数値を入力してください".encode('utf-8')) 
            continue
    
    sndmsg=str(sndmsg) #送信時str型のためキャスト
    
    conn.sendall(sndmsg.encode('utf-8')) #メッセージを返します

#クローズ処理 
print("Now Closing")
conn.close()