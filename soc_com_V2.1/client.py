# Echo client program
import socket
import sys

HOST = socket.gethostname()    #ホスト名取得
PORT = 8080              #ポート番号8080にする
client = None

response=0 #response初期値
massage=0 #massage初期値(未定義エラー回避のためexit以外で定義)

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        client = socket.socket(af, socktype, proto)
    except OSError as msg:
        client = None
        continue
    #getaddrinfoで取得しtアドレス情報とポート番号で接続
    #失敗時はエラー文表示
    try:
        client.connect(sa)
    except OSError as msg:
        client.close()
        client = None
        continue
    break
if client is None:
    print('could not open socket')
    sys.exit(1)
    
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
        continue
    else:
        client.send(massage.encode('utf-8')) #サーバープログラムにデータ送信

        response = client.recv(4096).decode() #サーバーの処理結果受信(レシーブは適当な2の累乗)

    print(response)

print("計算を終了します")
client.close()