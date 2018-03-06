import random
import math
import sys
import struct

#  平方乘算法 | 快速指数算法
def Fast_exp(base, power, modNum):
    temp = 1
    result = 0
    while(power >= 1):
        if power == 1:
            result = (temp * base) % modNum
            return result
        else:
            if power % 2 == 0:
                base = (base * base) % modNum
                power = power >> 1  #用除法会显示数据过大而无法除
            else:
                temp = (temp * base) % modNum
                power -= 1

#  求最大公约数
def gcd(a, b):
    temp = 0
    if b > a:
        temp = b
        b = a
        a = temp
    while b != 0:
        temp = a % b
        a = b
        b = temp     
    return a

#  带模求逆
def mod_oppo(num, modNum):
    temp1 = 0
    temp2 = 1
    oppo = 0
    mod_res = 0
    if num < modNum:
        temp = num
        num = modNum
        modNum = temp
    t = num
    while True:
        mod_res = num % modNum
        if mod_res != 0:
            oppo = -1 * (num // modNum) * temp2 + temp1
        temp1 = temp2
        temp2 = oppo
        num = modNum
        modNum = mod_res
        if mod_res == 1:
            break
    if oppo < 0:
        oppo = oppo + t
    return oppo

#  miller-Rabin 素性检验
def Mi_Ra_Test(n, k):
    m = n-1
    s = 0
    while True:
        if m % 2 == 0 :
            m = m//2
            s += 1
        else:
            break
    #  print(s)
    while k!=0 :
        a = random.randint(1, n-1)
        #  print(a, end=' ')
        #  print('')
        b = Fast_exp(a, m, n)
        #if b == 1 or b == n-1:
        if b == 1:
            return True
            #  continue
        for i in range(s-1):
            #   print(b)
            b = Fast_exp(b, 2, n)
            if b == 1:
                return False
            if b == n-1:
                break
        if b != (n-1):
            return False
        k -= 1
    return True

#  进度条函数
def progress(percent, width=50):
    if percent >= 100:
        percent = 100
    show_str=('[%%-%ds]' %width) %(int(width * percent / 100) * "#") #字符串拼接的嵌套使用
    print("\r%s %d%%" %(show_str, percent),end='',file=sys.stdout,flush=True)

#  生成2至20000素数集
def Scr_pri():
    a = []
    for i in range(2, 20000):
        b = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                b = 1
        if b == 0:
            a.append(i)
    return a

#  素数生成测试
def test(t):
    count = 0
    for i in range(10000):
        a = random.randint(int('1'*500), int('9'*500))
        flag = 0
        for x in t:
            if a % x == 0:
                flag = 1
                break
        if flag == 1:
            continue
        if Mi_Ra_Test(a, 10) == True:
            print('\n', a)
            count += 1
        recv_per = int(100*(i/10000) + 1)  #  接收的比例
        progress(recv_per, width=50)  #  进度条的宽度30  
    return count

#  生成素数
def prime_iter():
    t = Scr_pri()
    for i in range(10000):
        a = random.randint(int('1'*300), int('9'*300))
        flag = 0
        for x in t:
            if a%x == 0:
                flag = 1
                break
        if flag == 1:
            continue
        if Mi_Ra_Test(a, 10) == True:
            break
    return a

#  计算欧拉函数
def cal_Euler(a, b):
    return (a-1)*(b-1)

#  计算e
def cal_e(n):
    for i in range(random.randint(int('1'*300), int('9'*300)), n):
        if gcd(i, n) == 1:
            return i

#  将读取的字节转为大整数
def bytes_to_num(a):
    b = []
    for i in a:
        b.append(str(i))
    for i in range(len(b)):
        if len(b[i]) < 3:
            b[i] = ''.join(['0'*(3-len(b[i])), b[i]])
    c = ''
    for i in range(len(b)):
        c = ''.join([c, b[i]])
    if len(c) < 192:
        c = ''.join([c, '0'*(192-len(c))])
    #print(c)
    d = int(c)
    return d

#  将加密数据按照一定格式写入文件
def encry_code(n, h):
    a = str(n)
    l_0 = len(a)
    l = str(l_0)
    a = ''.join([a, '0'*(600-len(a))])
    l = ''.join(['0'*(10-len(l)), l])
    b = ''.join([a, l])
    c = []
    for i in range(0, 610, 2):
        c.append(int(b[i:i+2]))
    for i in range(len(c)):
        h.write(struct.pack('B', c[i]))
    h.flush()

#  将从文件中读取的密文按格式进行读取还原
def decry_code(a):
    b = []
    for i in a:
        b.append(str(i))
    for i in range(len(b)):
        if len(b[i]) < 2:
            b[i] = ''.join(['0'*(2-len(b[i])), b[i]])
    c = ''
    for i in range(len(b)):
        c = ''.join([c, b[i]])
    d = int(c[600:])
    e = int(c[:d])
    return e

#  将明文写入解密文件
def num_to_bytes(n, h):
    a = str(n)
    if len(a) < 192:
        a = ''.join(['0'*(192-len(a)), a])
    b = []
    for i in range(0, 192, 3):
        b.append(int(a[i:i+3]))
    for i in range(64):
        h.write(struct.pack('B', b[i]))
    h.flush()

#  加密操作
def encrypt(m, e, n):
    c = Fast_exp(m, e, n)
    return c

#  解密操作
def decrypt(c, d, n):
    p = Fast_exp(c, d, n)
    return p

#  全加密函数
def all_enc():
    name1 = input("请输入加密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #总字节数
    f.seek(0, 0) 
    for i in range(l//64 + 1):
        if i == l//64:
            a = f.read()
        else:    
            a = f.read(64)
        if len(a) == 64:
            a = struct.unpack('B'*64, a)
        elif a == b'':
            break
        else:
            a = struct.unpack('B'*len(a), a)      
        m = bytes_to_num(a)
        b = encrypt(m, e, n)
        encry_code(b, h)
        recv_per=int(100*((i+1)*64/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
        
    print("\n")
    print("加密成功！")
    f.close()
    h.close()

#  全解密函数
def all_dec():
    name1 = input("请输入解密文件名：")
    name2 = input("请输入输出文件名：")
    f = open(name1, 'rb')  #  按字节存取
    h = open(name2, 'ab')
    l = f.seek(0, 2)  #  总字节数
    f.seek(0, 0) 
    for i in range(l//305 + 1):
        if i == l//305:
            a = f.read()
        else:    
            a = f.read(305)
        if len(a) == 64:
            a = struct.unpack('B'*305, a)
        elif a == b'':
            break
        c = decry_code(a)
        b = decrypt(c, d, n)
        num_to_bytes(b, h)
        recv_per=int(100*((i+1)*305/l)) #接收的比例
        progress(recv_per,width=30) #进度条的宽度30
    print("\n")
    print("解密成功！")
    f.close()
    h.close()
    return

if __name__ == '__main__':
    x = prime_iter()
    y = prime_iter()
    n = x*y
    euler = cal_Euler(x, y)
    e = cal_e(euler)
    d = mod_oppo(e, euler)
    print("本次运行公钥为:")
    print('n = ', n)
    print('e = ', e)
    print("本次运行私钥为:")
    print('d = ', d)
    print('x = ', x)
    print('y = ', y)
    while True:
        print("""
        请选择功能：
        1、加密
        2、解密
        3、退出
        """)
        choice = input(">>>")
        if choice == '1':
            all_enc()
        elif choice == '2':
            all_dec()
        elif choice == '3':
            break
        else:
            pass
