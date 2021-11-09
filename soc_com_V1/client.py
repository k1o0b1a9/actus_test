# -*- coding:utf-8 -*-
import socket

host = socket.gethostname() #ホスト名取得
port = 8765 #PORT指定(クライアントと一致していればOK)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

client.connect((host, port)) #これでサーバーに接続します

massage=0 #message初期値

while massage != 'exit':
    print("Send Message")

    massage=input()

    client.send(massage.encode('utf-8')) #適当なデータを送信します（届く側にわかるように）

    response = client.recv(4096).decode() #レシーブは適当な2の累乗にします（大きすぎるとダメ）

    print(response)
    
client.close()