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

    client.send(massage.encode('utf-8')) #サーバープログラムにデータ送信

    response = client.recv(4096).decode() #サーバーの処理結果受信(レシーブは適当な2の累乗)

    print(response)
    
client.close()