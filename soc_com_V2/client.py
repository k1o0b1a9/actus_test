# -*- coding:utf-8 -*-
import socket

host = socket.gethostname() #ホスト名取得
port = 8080 #PORT指定(クライアントと一致していればOK)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成

client.connect((host, port)) #これでサーバーに接続します

massage=0 #message初期値

print("計算を行います、終了する場合は'exit'と入力してください")

while massage != 'exit':
    print("Send Message")

    massage=input()
    
    #入力ない場合は送信しない
    if not massage:
        print("文字を入力してください")
    else:
        client.send(massage.encode('utf-8')) #サーバープログラムにデータ送信

        response = client.recv(4096).decode() #サーバーの処理結果受信(レシーブは適当な2の累乗)

        print(response)

print("計算を終了します")
client.close()