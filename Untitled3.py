
# coding: utf-8

# In[1]:



#object 不是一个参数
class Student(object):
    def __init__(self,a,b):
        print('a-b=',a-b);
        print('a+b=',a+b);
        print('a*b=',a*b);
        print('a/b=',a/b);
        print('a%b=',a%b);
        print('a//b=',a//b);
        print('a的平方是',a*a);
        print('b的平方是',b*b);
Student(10,5)


# In[2]:


class asd(object):
    def __init__(self,a):
        if(a>50):
            print("别看了，扛不住的")
        elif(a>20):
            print("岛国")
        elif(a>18):
            print("只能观看四级")
        else:
            print("你只能观看动画片")
            
asd(16)


# In[3]:


class Name(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def func1(self):
        if self.a>40:
            print("老年")
        elif self.a>18:
            print("中年")
        else:
            print("青年")
    def func2(self):
        if self.b == "男":
            print("男人")
        elif self.b == "女":
            print("女人")
        else:
            print("不知道你是什么玩意儿")
name = Name(25,"女")
name.func1()
name.func2()


# In[6]:


import time
class Time(object):
    def __init__(self):
        self.time=time
    def shuzi(self):
        for i in range(1,100):
            i=i+1
            if i<100:
                time.sleep(1)
                now = time.localtime()  # 返回服务器时间
                print(time.strftime("%H:%M:%S \r", now),end="",flush=True)
                if time.strftime("%H:%M:%S", now)=='15:05:00':
                    print("闹钟响了！！! ")
                else:
                    pass

Time().shuzi()


# In[7]:


class A(object):
    def __init__(self,a):
        self.a=a
    def B(self):
        m=2
        for i in range(2,self.a):
            m=m+1
            if self.a%i==0:
                print("不是素数")
                break
            if m == self.a:
                print("是素数")
                
qwe=A(11)
qwe.B()


# In[8]:


res = input('输入')
print(res,type(res))


# In[9]:


import numpy as np
res = np.random.choice(['典韦','赵云','鲁班'])


# In[10]:


import numpy as np
class Wangzhe(object):
    def __init__(self):
        pass
    def renji(self):
        print('请选择人机或者多人对战！')
        res = input('输入')
        print("您选的是",res)
        self.res=res
    def tiaoxuan(self):
        print('请从典韦、赵云、鲁班中挑选一个人物！')
        ren = input('输入')
        print("您选的是",ren)
        self.ren=ren
    def xianshizhanli(self):
        if self.ren == '典韦':
            print("您选择的典韦战力为10000，防御力为5000")
        elif self.ren == '赵云':
            print("您选择的赵云战力为20000，防御力为2000")
        else:
            print("您选择的鲁班战力为15000，防御力为3500")
    def renwuqueding(self):
        print("您的人物以确定，现在系统随机为您生成对战玩家")
        q = np.random.choice(['典韦','赵云','鲁班'])
        print('您的对手为',q)
    def kaishi(self):
        print("请输入开始")
        w = input('输入')
        if w == "开始":
            print("输入正确")
        else:
            print("输入有误！")
    def jiazai(self):
        print('正在加载，请耐心等待！')
    
qwe = Wangzhe()
qwe.renji()
qwe.tiaoxuan()
qwe.xianshizhanli()
qwe.renwuqueding()
qwe.kaishi()
qwe.jiazai()


# In[11]:


"""
1/一个五角数被定义为n(3n-1)/2,编写一个测试程序使用这个函数显示前100个五角数，
每行显示10个
"""
def getPentagonalNumber(n):
    c = n*(3*n-1)/2
    if n%10 !=0:
        print(c,end=' ')
    else:
        print(c)
        
for i in range(1,101):
    getPentagonalNumber(i)


# In[12]:


"""
2/计算一个整数各个数字的和
"""
def sumDigits(n):
    a=n
    w=0
    for i in range(0,len(str(a))):
        if i<len(str(a)):
            q = n%10
            n = n//10
        w = w + q
    print(w)
sumDigits(456789)


# In[13]:


"""
3/提醒用户输入三个整数，然后调用函数按升序显示三个数
"""
def desplaySortedNumbers(num1,num2,num3):
    print("Enter three number:",num1,num2,num3)
    if num1>num2 and num1>num3:
        if num2 > num3:
            print("The sorted number are",num3,num2,num1)
        else:
            print("The sorted number are",num2,num3,num1)
    elif num2>num1 and num2>num3:
        if num1 > num3:
            print("The sorted number are",num3,num1,num2)
        else:
            print("The sorted number are",num1,num3,num2)
    elif num3>num1 and num3>num2:
        if num1 > num2:
            print("The sorted number are",num2,num1,num3)
        else:
            print("The sorted number are",num1,num2,num3)

desplaySortedNumbers(89,42,2)


# In[14]:


"""
4/ 编写一个程序提示用户输入投资额和百分比格式的年利率，然后输出一份表格显示
年份从1到30年的未来值。
"""
def futureInvestmentValue(benjin,lilv,years):
    years = years+1
    for i in range(1,years):
        shouyi = benjin + benjin*lilv
        print(i,shouyi)
        benjin=shouyi
futureInvestmentValue(10000,0.09,30)


# In[15]:


"""
5、打印ch1到ch2之间的字符，按每行指定某个数来打印。
编写一个测试程序，打印“1”到“Z”的字符，每行打印10个
"""
def printChars(ch1,ch2,num):
    q=ord(ch1)+1
    w=ord(ch2)
    n=0
    for i in range(q,w):
        n=n+1
        if n%num !=0:
            print(chr(i),end='  ')
        else:
            print(chr(i))
        
printChars('1','Z',10)


# In[16]:


"""
6、编写一个程序测试，显示从2010年到2020年每年的天数
"""
def numberOfDaysInAYrea(year):
    if year%100==0:
        if year%400==0:
            print(year,"366天")
        else:
            print(year,"365天")
    elif year%4==0:
        print(year,"366天")
    else:
        print(year,"365天")

for year in range(2010,2021):
    numberOfDaysInAYrea(year)


# In[17]:


"""
7、计算两点间距离
"""
import math
def distance(x1,y1,x2,y2):
    q=(x1-x2)**2
    w=(y1-y2)**2
    e=q+w
    dis= math.sqrt(e)
    print("两点间距离为：",dis)
    
distance(1,2,3,4)


# In[18]:


"""
8、如果一个素数可以写成2**（P-1）的形式，其中p是某个正整数，
    那么这个数就被称作梅森素数。编写程序找出p<=31的梅森素数。
"""
def meisen(p):
    q=pow(2,p)-1
    m=2
    if p==2:
        print(p,q)
    for i in range(2,p):
        m=m+1
        if p%i==0:
            break
        if m == p:
            print(p,q)
            
for p in range(1,32):
    meisen(p)


# In[19]:


"""
9、调用time.time()返回1970年1月1日0点开始的毫秒数。
"""
import time
print(time.time())
"""
 time.localtime(time.time())输出结果为
 time.struct_time(tm_year=2019, tm_mon=8, 
 tm_mday=6, tm_hour=19, tm_min=21, tm_sec=46, 
 tm_wday=1, tm_yday=218, tm_isdst=0)
"""
time = time.localtime(time.time())
print("Cuurrent date and time is",time.tm_year,"年",
      time.tm_mon,"月",time.tm_mday,"日",
      time.tm_hour,":",time.tm_min,":",time.tm_sec)


# In[20]:


"""
10、投色子。
"""
import numpy as np
def dianshu():
    res1 = np.random.choice([1,2,3,4,5,6])
    print("您第一次抛出的点数为:",res1)
    res2 = np.random.choice([1,2,3,4,5,6])
    print("您第二次抛出的点数为:",res2)
    res = res1 + res2
    print("您抛出的两次点数之和为：",res)
    return res
res = dianshu()
if res==2 or res==3 or res==12:
    print("你输了！！！")
elif res==7 or res==11:
    print("你赢了！！！")
else:
    res3 = res
    res = dianshu()
    if res ==7 or res == res3:
        print("你赢了！！！")
    else:
        print("请开始下一局！")


# In[21]:


"""
1、矩形……
"""
class Rectangle(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        q=self.height*self.width
        print("这个矩形的面积为：",q)
    def getPerimeter(self):
        w=2*self.height+2*self.width
        print("这个矩形的周长为：",w)
qwe = Rectangle(12,15)
qwe.getArea()
qwe.getPerimeter()


# In[22]:


"""
2、定义一个名为Account类，……
"""
class Account(object):
    def __init__(self):
        self.lilv=0
        self.ann=100
        self.lixi=0
    def shuju(self,id,ann):
        self.id=id
        self.ann=ann
    def getMonthlyInterestRate(self,lilv):
        self.lilv=lilv
    def getMonthlyInterest(self):
        q=self.ann*self.lilv
        self.lixi=q
    def withdraw(self):
        print("请输入取钱金额")
        res = input("输入")
        self.ann = self.ann - int(res)
        print("您成功取出",res,"元")
    def deposit(self):
        print("请输入存钱金额")
        res1=input("输入")
        self.ann=self.ann+int(res1)
        print("您成功存入",res1,"元")
    def dayin(self):
        print(self.id,"您账户余额为：",self.ann,"利率为：",self.lilv,"利息为",self.lixi)
        
qwe = Account()
qwe.shuju(1122,20000)
qwe.getMonthlyInterestRate(0.045)
qwe.getMonthlyInterest()
qwe.withdraw()
qwe.deposit()
qwe.dayin()


# In[23]:


"""
3、设计一个名为Fan的类表示一个风扇。
"""
class Fan(object):
    def __init__(self):
        self.speed=1
        self.on=False
        self.radius=5.0
        self.color="blue"
    def fengshan(self,speed,on,radius,color):
        self.speed=speed
        self.color=color
        self.radius=radius
        self.on=on
    def xianshi(self):
        if self.speed==1:
            speed1="SLOW"
        elif self.speed==2:
            speed1="MEDIUM"
        else:
            speed1="FAST"
        print(speed1,self.on,self.radius,self.color)
qwe = Fan()
qwe.fengshan(3,10.0,True,"yellow")
qwe.xianshi()
qwe.fengshan(2,5.0,False,"blue")
qwe.xianshi()


# In[24]:


"""
4、一个正n边形的边都有同样的长度，……
"""
import math
class RegularPolygon(object):
    def __init__(self,n,side,x,y):
        self.n=n
        self.side=side
        self.x=x
        self.y=y
    def getPerimenter(self):
        print(self.n*self.side)
    def getArea(self):
        Area = self.n*self.side/(4*math.tan(math.pi/self.n))
        print(Area)
qwe = RegularPolygon(10,4,5.6,7.8)
qwe.getPerimenter()
qwe.getArea()


# In[25]:


"""
5、2*2线性方程
"""
class LinearEquation(object):
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
        self.x=0
        self.y=0
        self.z=0
    def isSolvable(self):
        z=self.__a*self.__d-self.__b*self.__c
        if z !=0:
            self.z=True
        else:
            self.z=False
    def get(self):
        self.x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        self.y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
    def getX(self):
        self.isSolvable()
        if self.z == True:
            self.get()
            print(self.x)
        else:
            pass
    def getY(self):
        self.isSolvable()
        if self.z == True:
            self.get()
            print(self.y)
        else:
            pass
        
qwe=LinearEquation(1,2,3,4,5,6)
qwe.getX()
qwe.getY()


# In[26]:


"""
6、求两个线段的交点
"""
import numpy as np
def get_crossing(s1,s2):
    xa,ya = s1[0][0],s1[0][1]
    xb,yb = s1[1][0],s1[1][1]
    xc,yc = s2[0][0],s2[0][1]
    xd,yd = s2[1][0],s2[1][1]
    #判断两条直线是否相交，矩阵行列式计算
    a = np.matrix(
        [
            [xb-xa,-(xd-xc)],
            [yb-ya,-(yd-yc)]
        ]
    )
    delta = np.linalg.det(a)
    #不相交,返回两线段
    if np.fabs(delta) < 1e-6:
        print(delta)
        return None        
    #求两个参数lambda和miu
    c = np.matrix(
        [
            [xc-xa,-(xd-xc)],
            [yc-ya,-(yd-yc)]
        ]
    )
    d = np.matrix(
        [
            [xb-xa,xc-xa],
            [yb-ya,yc-ya]
        ]
    )
    lamb = np.linalg.det(c)/delta
    miu = np.linalg.det(d)/delta
    #相交
    if lamb <= 1 and lamb >= 0 and miu >= 0 and miu <= 1:
        x = xc + miu*(xd-xc)
        y = yc + miu*(yd-yc)
        return (x,y)
    #相交在延长线上
    else:
        return None
get_crossing(((1,2),(3,4)),((1,4),(2,3)))


# In[27]:


"""
7、2*2线性方程
"""
class LinearEquation(object):
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
        self.x=0
        self.y=0
        self.z=0
    def isSolvable(self):
        z=self.__a*self.__d-self.__b*self.__c
        if z !=0:
            self.z=True
        else:
            self.z=False
    def get(self):
        self.x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        self.y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
    def getX(self):
        self.isSolvable()
        if self.z == True:
            self.get()
            print(self.x)
        else:
            pass
    def getY(self):
        self.isSolvable()
        if self.z == True:
            self.get()
            print(self.y)
        else:
            pass
        
qwe=LinearEquation(1,2,3,4,5,6)
qwe.getX()
qwe.getY()


# In[28]:


import random
import http.client 
import urllib
import urllib3
host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
 
#查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
account  = "C48856660"
#查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
password = "7505ea7957222ed2fe6fc2958311cdbd"
 
class zhuCe(object):
    def __init__(self):
        pass
    def youxiang(self):
        print("请输入邮箱号码")
        self.youxiang=input("")
        print("您输入邮箱号码为：",self.youxiang)
    def mima(self):
        print("请输入密码")
        self.mima_1=input("")
        print("请输入确认密码")
        self.mima_2=input("")
        if self.mima_1==self.mima_2:
            print("密码输入成功")
            self.mima=self.mima_1
        else:
            print("两次密码输入不一致！！！")
            self.mima()
    def yanzheng(self):
        for i in range(1,4):
            
            yanzheng_1=random.randrange(1000,9999)
            print("请输入验证码：",yanzheng_1)
            yanzheng_2=int(input(""))
            if yanzheng_1==yanzheng_2:
                print("验证通过")
                self.duanxin()
                break
        else:
            exit(0)
    def duanxin(self):
        print("请输入手机号码")
        self.shoujihao=input("")
        print("请输入手机验证码")
    def send_sms(self):
        self.mobile = self.shoujihao
        text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
        params = urllib.parse.urlencode({'account': account, 'password' : password, 'content': text, 'mobile':self.mobile,'format':'json' })
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection(host, port=80, timeout=30)
        conn.request("POST", sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
    def yanzhengma(self):
        self.phone=input("")
        self.T=False
        if self.phone=="121254":
            print("注册成功")
            self.T= True
        else:
            print("注册失败")
            exit(0)
qwe=zhuCe()
qwe.youxiang()
qwe.mima()
qwe.yanzheng()
qwe.send_sms()
qwe.yanzhengma()


# In[ ]:


import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
 
wangzhe = mpimg.imread('wangzhe.jpg') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
luban = mpimg.imread('luban.jpg')
dianwei = mpimg.imread('dianwei.jpg')
zhaoyun = mpimg.imread('zhaoyun.jpg')
jiazai = mpimg.imread('jiazai.jpg')
wangzhe.shape #(512, 512, 3)
dianwei.shape #(512, 512, 3)
zhaoyun.shape #(512, 512, 3)
zhaoyun.shape #(512, 512, 3)
jiazai.shape #(512, 512, 3)
plt.imshow(wangzhe) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
class Wangzhe(object):
    def __init__(self):
        pass
    def renji(self):
        print('请选择人机或者多人对战！')
        res = input('输入')
        print("您选的是",res)
        self.res=res
    def tiaoxuan(self):
        print('请从典韦、赵云、鲁班中挑选一个人物！')
        ren = input('输入')
        print("您选的是",ren)
        self.ren=ren
    def xianshizhanli(self):
        if self.ren == '典韦':
            plt.imshow(dianwei) # 显示图片
            plt.axis('off') # 不显示坐标轴
            plt.show()
            print("您选择的典韦战力为10000，防御力为5000")
        elif self.ren == '赵云':
            plt.imshow(zhaoyun) # 显示图片
            plt.axis('off') # 不显示坐标轴
            plt.show()
            print("您选择的赵云战力为20000，防御力为2000")
        else:
            plt.imshow(luban) # 显示图片
            plt.axis('off') # 不显示坐标轴
            plt.show()
            print("您选择的鲁班战力为15000，防御力为3500")
    def renwuqueding(self):
        print("您的人物以确定，现在系统随机为您生成对战玩家")
        q = np.random.choice(['典韦','赵云','鲁班'])
        print('您的对手为',q)
    def kaishi(self):
        print("请输入开始")
        w = input('输入')
        if w == "开始":
            print("输入正确")
        else:
            print("输入有误！")
    def jiazai(self):
        print('正在加载，请耐心等待！')
        plt.imshow(luban) # 显示图片
        plt.axis('off') # 不显示坐标轴
        plt.show()
qwe = Wangzhe()
qwe.renji()
qwe.tiaoxuan()
qwe.xianshizhanli()
qwe.renwuqueding()
qwe.kaishi()
qwe.jiazai()


# In[1]:


class YinSi(object):
    def __init__(self):
        self.__ys="小怪兽喜欢奥特曼"
        self.__mima="000000"
    @property
    def YS(self):
        print(self.__ys)
    @YS.setter
    def YS(self,ys):
        self.__ys=ys
    def mima(self):
        print("请输入密码：")
        res=input("")
        if res == self.__mima:
            print("密码输入正确，请更改隐私内容！")
            ys=input("")
            self.YS=ys
            print("内容成功修改为",self.__ys)
        else:
            print("密码输入错误，请重新输入：")
            self.mima()
    def wer(self):
        print("你想更改还是退出？")
        we = input("")
        if we == "更改":
            self.mima()
        else:
            pass
qwe=YinSi()
qwe.YS
qwe.wer()


# In[2]:



class Name(object):
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=0
    @property
    def A(self):
        print(self.__a)
    @A.setter
    def A(self,a1):
        self.__a=a1
    @property
    def B(self):
        print(self.__b)
    @A.setter
    def B(self,b1):
        self.__b=b1
    @property
    def C(self):
        print(self.__c)
    @A.setter
    def C(self,c1):
        self.__c=c1
    def play(self):
        print("三者之和为：",self.__a+self.__b+self.__c)
        
qwe=Name(4,5,6)
qwe.play()
qwe.a1=10
qwe.B=20
qwe.play()

