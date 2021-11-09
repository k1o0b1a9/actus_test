# coding: utf-8
#入力がなかった場合前回値表示プログラム
line = 0
before_val=0
while line != 'exit':
    line = input('>>>')
    if line == '' :
        line=before_val
        print("入力なし")
        print(line)
    else:
        print(line)
        before_val=line
