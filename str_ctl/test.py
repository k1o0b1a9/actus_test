import re
y = 0
while True:
    #inputで入力された値はstr型なので演算時キャストしてやる必要あり
    x = input()
    #数値単独の場合そのまま代入
    if(str.isdigit(x))==True:
        y=x
    #=のあとに数値が続いている場合もそのまま代入
    elif (x.find("="))!=-1:
        if(str.isdigit(x[(x.find("=")+1):]))==True:
            y = x[(x.find("=")+1):]
        else:
            print("数値を入力してください")
            continue
    #足し算
    elif (x.find("+"))!=-1:
        if(str.isdigit(x[(x.find("+")+1):]))==True:
            y=int(y)
            y += int(x[(x.find("+")+1):])
        else:
            print("数値を入力してください")
            continue
    #引き算
    elif (x.find("-"))!=-1:
        if(str.isdigit(x[(x.find("-")+1):]))==True:
            y=int(y)
            y -= int(x[(x.find("-")+1):])
        else:
            print("数値を入力してください")
            continue
    #掛け算    
    elif (x.find("*"))!=-1:
        if(str.isdigit(x[(x.find("*")+1):]))==True:
            y=int(y)
            y *= int(x[(x.find("*")+1):])
        else:
            print("数値を入力してください")
            continue
    #割り算
    elif (x.find("/"))!=-1:
        if(str.isdigit(x[(x.find("/")+1):]))==True:
            y=int(y)
            y /= int(x[(x.find("/")+1):])
        else:
            print("数値を入力してください")
            continue
    #文字列が入力された場合
    else:
        print("数値を入力してください")
        continue
    print(y)
    