# -*- coding:utf-8 -*-
import socket

host = socket.gethostname() #ホスト名取得
port = 8080 #PORT指定(クライアントと一致していればOK)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成

client.connect((host, port)) #これでサーバーに接続します

response=0 #response初期値
massage=0 #massage初期値(未定義エラー回避のためexit以外で定義)

print("計算を行います、終了する場合は'exit'と入力してください")

while massage != 'exit':

    print("Send Message")

    
    try:
        massage=input()
    except KeyboardInterrupt as message:
        massage="exit"
        client.send(massage.encode('utf-8')) #サーバープログラムにデータ送信
        client.close()
        break
    
    #入力ない場合は送信しない
    if not massage:
        print("文字を入力してください")
    else:
        client.send(massage.encode('utf-8')) #サーバープログラムにデータ送信

        response = client.recv(4096).decode() #サーバーの処理結果受信(レシーブは適当な2の累乗)

    print(response)

print("計算を終了します")
client.close()