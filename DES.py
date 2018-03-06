import struct
import sys
import time
import os

IP = (58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7)
IP_1 = (40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25)
S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8], [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0], [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10], [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15], [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8], [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1], [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7], [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15], [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9], [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4], [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9], [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6], [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14], [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
#S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11], [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8], [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
#S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1], [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6], [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7], [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2], [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8], [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11], [10,15,4,2,7,12,0,5,6,1,13,14,0,11,3,8], [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1], [13,0,11,7,4,0,1,10,14,3,5,12,2,15,8,6], [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
S = [S1, S2, S3, S4, S5, S6, S7, S8]
P = (16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25)
PC1 = (57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4)
PC2 = (14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32)
K_Mov = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

def progress(percent,width=50):
    if percent >= 100:
        percent=100

    show_str=('[%%-%ds]' %width) %(int(width * percent / 100) * "#") #字符串拼接的嵌套使用
    print("\r%s %d%%" %(show_str, percent),end='',file=sys.stdout,flush=True)

def key_iter():  #16轮密钥生成
    _start = 'Yao_yibo'  #初始密钥原型
    k0 = []
    for i in _start:
        k0.append(bin(ord(i))[2:])
    for i in range(8):
        if len(k0[i]) < 8:
            k0[i] = ''.join(['0'*(8-len(k0[i])), k0[i]])
    k2 = ''
    for i in k0:
        k2 = ''.join([k2, i])  #初始64位密钥
    key0 = ''
    for i in range(56):
        key0 = ''.join([key0, k2[PC1[i] - 1]])
    c, d = [], []
    c.append(key0[:28])
    d.append(key0[28:])
    for i in range(16):
        c1 = ''
        for j in range(28):
            c1 = ''.join([c1, c[i][(j+K_Mov[i]) % 28]])
        c.append(c1)
    for i in range(16):
        d1 = ''
        for j in range(28):
            d1 = ''.join([d1, d[i][(j+K_Mov[i]) % 28]])
        d.append(d1)
    Pre_key = []
    for i in range(1, 17):
        pre_key_ = ''.join([c[i], d[i]])
        Pre_key.append(pre_key_)
    Key = []  #十六轮密钥列表
    for i in range(16):
        K_key = ''
        for j in range(48):
            K_key = ''.join([K_key, Pre_key[i][PC2[j]-1]]) 
        Key.append(K_key)   
    return Key  #返回密钥

def expand_chg (b):  #扩展置换  32 -> 48
	c = []
	for i in range(0, 32, 4):
		c.append(b[i:i+4])
	for i in range(8):  #32位分为4位一组，前面添加上一组的最后一位，后面添加下一组的第一位，获得6位一组
		if i == 0:
			c[i] = ''.join([c[(i-1)%8][3], c[i], c[(i+1)%8][0]])
		elif i == 7:
			c[i] = ''.join([c[(i-1)%8][4], c[i], c[(i+1)%8][1]])
		else:
			c[i] = ''.join([c[(i-1)%8][4], c[i], c[(i+1)%8][0]])
	d = ''
	for i in range(8):
		d = ''.join([d, c[i]])
	return d
	
def Xor_48 (a, b):  #48位按位异或
    c = int(a, 2) ^ int(b, 2)
    d = bin(c)[2:]
    e = ''.join(['0'*(48-len(d)), d])
    return e

def Xor_32 (a, b):  #32位按位异或
    c = int(a, 2) ^ int(b, 2)
    d = bin(c)[2:]
    e = ''.join(['0'*(32-len(d)), d])
    return e

def S_box(f):  #S盒  48 -> 32 分八组，每组对应一个S盒， 每组的第一位和最后一位合并，以及剩余四位，转化为十进制作为索引， 查表
    a = []
    for i in range(0, 48, 6):
        a.append(f[i:i+6])
    b = []
    d = ''
    for i in range(8):
        temp = int(a[i][0]+a[i][5], 2)
        temp1 = int(a[i][1:5], 2)
        b.append(bin(S[i][temp][temp1])[2:])
    for i in range(8):
        if len(b[i]) == 4:
            d = ''.join([d, b[i]])
        else:
            d = ''.join([d, '0'*(4-len(b[i])), b[i]])
    return d

def P_box(d):
    e = ''
    for i in range(32):
        e = ''.join([e, d[P[i]-1]])
    return e

def IP_chg(s):  #初始置换
    a = ''
    for i in range(64):
        a = ''.join([a, s[IP[i]-1]])
    return a

def IP_1_chg(s):  #逆初始置换
    a = ''
    for i in range(64):
        a = ''.join([a, s[IP_1[i]-1]])
    return a

def code_to_string(a):  #将传入的数据元组中的每个元素分别转为二进制并合并为一个64位二进制字符串
    b = []
    for i in a:
        b.append(bin(i)[2:])
    if len(b) < 8:
        for i in range(8-len(b)):  #元组个数不足八个，则补零至八个
            b.append('00000000')
    for i in range(8):
        if len(b[i]) < 8:
            b[i] = ''.join(['0'*(8-len(b[i])), b[i]])
    c = ''
    for i in b:
        c = ''.join([c, i])
    #print(c)
    return c
    
def code_write(b, h):  #将64位二进制字符串拆成八位一组，分别转为字节型数据写入文件
    d = []
    for i in range(0, 57, 8):
        d.append(b[i:i+8])
    for i in range(8):
        d[i] = int(d[i], 2)
    for i in range(8):
        h.write(struct.pack('B', d[i]))
    h.flush()

def encrypt(m, k):  #加密
    m = IP_chg(m)
    l, r = [], []
    l.append(m[:32])
    r.append(m[32:])
    for i in range(16):    
        l.append(r[i])
        r[i] = expand_chg(r[i])
        r[i] = Xor_48(r[i], k[i])
        r[i] = S_box(r[i])
        r[i] = P_box(r[i])
        r.append(Xor_32(r[i], l[i]))
    x = ''
    x = ''.join([r[16], l[16]])
    x = IP_1_chg(x)
    return x

def decrypt(m, k):  #解密
    m = IP_chg(m)
    l, r = [], []
    l.append(m[:32])
    r.append(m[32:])
    for i in range(16):    
        l.append(r[i])
        r[i] = expand_chg(r[i])
        r[i] = Xor_48(r[i], k[15-i])
        r[i] = S_box(r[i])
        r[i] = P_box(r[i])
        r.append(Xor_32(r[i], l[i]))
    x = ''
    x = ''.join([r[16], l[16]])
    x = IP_1_chg(x)
    return x

def all_enc():
    name1 = input("请输入加密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    k = []
    k = key_iter()
    for i in range(l//8 + 1):
        if i == l//8:
            a = f.read()
        else:    
            a = f.read(8)
        if len(a) == 8:
            a = struct.unpack('BBBBBBBB', a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)
        m = code_to_string(a)
        b = encrypt(m, k)
        code_write(b, h)
        recv_per=int(100*((i+1)*8/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("加密成功！")
    f.close()
    h.close()
    return

def CBC_enc():
    name1 = input("请输入加密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    k = []
    k = key_iter()
    for i in range(l//8 + 1):
        if i == l//8:
            a = f.read()
        else:    
            a = f.read(8)
        if len(a) == 8:
            a = struct.unpack('BBBBBBBB', a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)
        m = code_to_string(a)
        pre_IV = '0110111111011101101010111010101000001111100010101001010010111011'
        if i == 0:
            m = bin(int(pre_IV, 2) ^ int(m, 2))[2:]
        else:
            m = bin(int(pre, 2) ^ int(m, 2))[2:]
        if len(m)<64:
            m = ''.join(['0'*(64-len(m)), m])
        pre = encrypt(m, k)
        code_write(b, h)
        recv_per=int(100*((i+1)*8/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("加密成功！")
    f.close()
    h.close()
    return

def CBC_dec():
    name1 = input("请输入解密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    k = []
    k = key_iter()
    for i in range(l//8 + 1):
        if i == l//8:
            a = f.read()
        else:    
            a = f.read(8)
        if len(a) == 8:
            a = struct.unpack('BBBBBBBB', a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)
        m = code_to_string(a)
        b = decrypt(m, k)
        temp = b
        pre_IV = '0110111111011101101010111010101000001111100010101001010010111011'
        if i == 0:
            b = bin(int(pre_IV, 2) ^ int(b, 2))[2:]
        else:
            b = bin(int(pre_IV, 2) ^ int(pre, 2))[2:]
        pre = temp
        code_write(b, h)
        recv_per=int(100*((i+1)*8/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("解密成功！")
    f.close()
    h.close()
    return

def all_dec():
    name1 = input("请输入解密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    k = []
    k = key_iter()
    for i in range(l//8 + 1):
        if i == l//8:
            a = f.read()
        else:    
            a = f.read(8)
        if len(a) == 8:
            a = struct.unpack('BBBBBBBB', a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)
        m = code_to_string(a)
        b = decrypt(m, k)
        code_write(b, h)
        recv_per=int(100*((i+1)*8/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("解密成功！")
    f.close()
    h.close()
    return

def show_menu():
    print("""
    请选择所使用的功能：
    1、全加密解密（不考虑文件格式）
    2、png文件加密解密（当前仅支持该文件）
    3、雪崩效应测试
    4、用户登陆测试
    5、CBC模式全加密
    6、退出
    """)

def menu_1():
    print("""
    1、加密
    2、解密
    3、返回
    """)
    choice = input(">>>")
    if choice == '1':
        all_enc()
    elif choice == '2':
        all_dec()
    elif choice == '3':
        return 
    else:
        print("input error")
        return
    return 

def png_enc():
    name1 = input("请输入加密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    k = []
    k = key_iter()
    for i in range(l//8 + 1):
        if i == l//8:
            a = f.read()
        else:    
            a = f.read(8)
        if len(a) == 8:
            a = struct.unpack('BBBBBBBB', a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)
        m = code_to_string(a)
        if i <= 32:  #png文件加密解密
            code_write(m, h)
        else:
            b = encrypt(m, k)
        #b = decrypt(m, k)
            code_write(b, h)

        recv_per=int(100*((i+1)*8/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("加密成功！")
    f.close()
    h.close()
    return

def png_dec():
    name1 = input("请输入解密文件名:")
    name2 = input("请输入输出文件名:")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    k = []
    k = key_iter()
    for i in range(l//8 + 1):
        if i == l//8:
            a = f.read()
        else:    
            a = f.read(8)
        if len(a) == 8:
            a = struct.unpack('BBBBBBBB', a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)
        m = code_to_string(a)
        if i <= 32:  #png文件加密解密
            code_write(m, h)
        else:
            b = decrypt(m, k)
            code_write(b, h)
        recv_per=int(100*((i+1)*8/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("解密成功!")
    f.close()
    h.close()
    return

def menu_2():
    print("""
    1、加密
    2、解密
    3、返回
    """)
    choice = input(">>>")
    if choice == '1':
        png_enc()
    elif choice == '2':
        png_dec()
    elif choice == '3':
        return
    else:
        print("input error")
        return
    return 

def menu_3():
    a = "0" * 63 + '1'
    b = "0" * 64
    print("初始a：")
    print(a)
    print("初始b：")
    print(b)
    k = key_iter()
    a = IP_chg(a)
    b = IP_chg(b)
    la, ra = [], []
    lb, rb = [], []
    la.append(a[:32])
    ra.append(a[32:])
    lb.append(b[:32])
    rb.append(b[32:])
    for i in range(16):    
        la.append(ra[i])
        ra[i] = expand_chg(ra[i])
        ra[i] = Xor_48(ra[i], k[i])
        ra[i] = S_box(ra[i])
        ra[i] = P_box(ra[i])
        ra.append(Xor_32(ra[i], la[i]))

        lb.append(rb[i])
        rb[i] = expand_chg(rb[i])
        rb[i] = Xor_48(rb[i], k[i])
        rb[i] = S_box(rb[i])
        rb[i] = P_box(rb[i])
        rb.append(Xor_32(rb[i], lb[i]))
        print("第", i, "轮a:")
        print(la[i] + ra[i])
        print("第", i, "轮b:")
        print(lb[i] + rb[i])

    xa = ''
    xa = ''.join([ra[16], la[16]])
    xa = IP_1_chg(xa)

    xb = ''
    xb = ''.join([rb[16], lb[16]])
    xb = IP_1_chg(xb)    
    
    print("加密结束的a：")
    print(xa)
    print("加密结束的b：")
    print(xb)
    return 

def str_to_64bin(a):
    k0 = []
    if len(a) < 8:
        a = ''.join([a, '_'*(8-len(a))])
    for i in a:
        k0.append(bin(ord(i))[2:])
    for i in range(8):
        if len(k0[i]) < 8:
            k0[i] = ''.join(['0'*(8-len(k0[i])), k0[i]])
    k2 = ''
    for i in k0:
        k2 = ''.join([k2, i])
    return k2

def menu_4():
    if os.path.exists("log.ini") == False:
        f = open("log.ini", 'a')
        f.close()
    print("模拟登陆系统：")
    passin = input("请输入登录口令：")
    f = open("log.ini", 'r')
    test = 0
    if f.seek(0, 2) == 0:
        test = 1
        f.close()
        f = open("log.ini", 'a')
        ans = input("目前该登录系统还没有口令，回复Y创建新的口令:")
        if ans == 'Y':
            name = input("请输入用户名：")
            if name == 'test_admin':
                password = input("请输入密码：")
                if password == '133545':
                    pass_in = input("请输入所要创建的口令，八个字符及以内:")
                    bin_pass_in = str_to_64bin(pass_in)
                    k = key_iter()
                    cry_pass = encrypt(bin_pass_in, k)
                    f.writelines(cry_pass)
                    f.close()
                else:
                    print("密码错误")
            else:
                print('用户名错误')
        else :
            print("退出。。。")
    if test == 1:
        f = open("log.ini", 'r')
    k = key_iter()
    bin_passin = str_to_64bin(passin)
    cry_passin = encrypt(bin_passin, k)
    flag = 0
    for i in f:
        if cry_passin == i:
            flag = 1
            break
    if flag == 1:
        print("恭喜你，登录成功")
    else :
        print("口令错误！")
    return
    

def menu_5():
    print("""
    1、加密
    2、解密
    3、返回
    """)
    choice = input(">>>")
    if choice == '1':
        CBC_enc()
    elif choice == '2':
        CBC_dec()
    elif choice == '3':
        return 
    else:
        print("input error")
        return
    return 


if __name__ == '__main__':
    show_menu()
    while True:
        menu = input(">>>")
        if menu == '1':
            menu_1()
        elif menu == '2':
            menu_2()
        elif menu == '3':
            menu_3()
        elif menu == '4':
            menu_4()
        elif menu == '5':
            menu_5()
        elif menu == '6':
            break
        else:
            print("input error, please try again")
        time.sleep(1)
        show_menu()





