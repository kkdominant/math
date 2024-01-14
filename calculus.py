from IPython.display import display, Math
from sympy import *
import time
import math
time_now=int(time.strftime("%H:%M:%S").split(":")[0])
# import sympy#使用display＋sympy.latex(expr)如果使用上面的引用的直接latex(expr)
x,a,b,m,n=symbols("x,a,b,m,n")
###极限limitation
def my_limit(expression,tendency,dir=None):
     try:
          if dir:
            #    print(f"welcome to limitation ,time is {time_now} clock\n{greeting}")
               outcome=limit(expression,x,tendency,dir=dir)
               display(Math('$\displaystyle\lim_{x\\rightarrow {%s}^{%s}} {%s}={%s}$'%(tendency,dir,latex(expression),latex(outcome))))
          else:
            #    print(f"welcome to limitation ,time is {time_now} clock\n{greeting}")
               outcome=limit(expression,x,tendency,dir="+-")
               display(Math('$\displaystyle\lim_{x\\rightarrow {%s}} {%s}={%s}$'%(tendency,latex(expression),latex(outcome))))
     except ValueError as e:
          # wrong=traceback.print_exc()
          # print(type(wrong))
          print("出现了以下错误：", e)

### 不定积分与定积分  indefinite integral and definite integral
def my_int(expression,a=None,b=None):#b写成B了,我真是小丑joker
    if a and b or a==0 or b==0:##如果不写这两个or的话，积分上下限有0都会变成不定积分
    #    print(f"welcome to definite integral ,time is {time_now} clock\n{greeting}")
       outcome=integrate(expression,(x,a,b))                                                                                                                                                                                                                                                                                                               
       display(Math('$\displaystyle\int_{%s}^{%s}{%s}\mathrm{dx}={%s}={%s}$'%(a,b,latex(expression),latex(outcome),(N(outcome)))))

    else:
        # print(f"welcome to indefinite integral ,time is {time_now} clock\n{greeting}")
        outcome=integrate(expression)  
        display(Math('$\displaystyle\int{%s}\mathrm{dx}={%s}+C$'%(latex(expression),latex(outcome))))
       
# expression=(sqrt(4*x**2-1)+x+1)/sqrt(x**2+sin(x))
# print(my_limit(expression,0))
# my_int(expression,2,3)
# my_int(expression)
def  my_diff(expression,n=1):#求导、其中expression是表达式、n是要求的阶数
    outcome=expression.diff(x,n)      
    display(Math('$\displaystyle ({%s})^{({%s})}={%s}$'%(latex(expression),n,latex(outcome))))



def factorial(n):
    return  math.factorial(n)
factorial(10)
def Combination(a,b):
    return int(factorial(a)/(factorial(b)*factorial(a-b)))
def Permutation(a,b):
    return int(factorial(a)/(factorial(a-b)))





##抖音热度排行榜获取
def get_douyin_ranks():
    import requests

    headers = {
        'authority': 'www.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
         # "cookie":填写自己的cookie
        'referer': 'https://www.douyin.com/discover',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&board_type=0&board_sub_type=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=en-US&browser_platform=Win32&browser_name=Chrome&browser_version=115.0.0.0&browser_online=true&engine_name=Blink&engine_version=115.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7214785270990161412&msToken=ddKVVUOv2hguLcuF70u_sc-NRorfWI-l8jKv3SumSgfvessukxxn49TF_b7ogRX4XqnngK2horQDdy_kAuKXPwJbrOhu13aGT0pT41Y71VIq4wT5SQNT6ugREv0MP31b&X-Bogus=DFSzswVOZtUANyOEtjOsOBt/pLvK',
        headers=headers,
    )
    # pprint(response.text)
    x=response.text
    import re
    contents=re.findall('word":"(.*?),',x)
    hot_values=re.findall('hot_value":(.*?),',x)
    # len(contents);len(hot_values)
    # contents;hot_values
    print("title".ljust(30),"hotvalues".rjust(25))
    for i,j in zip(contents,hot_values):
        ii=i.replace('"','').replace("}",'')
        jj=j.replace('}',' ').replace(']',' ')
        print(str(ii).ljust(50-len(ii)),jj.rjust(10-len(str(jj))))
