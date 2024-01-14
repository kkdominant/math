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
        'cookie': 'ttwid=1%7CtQ4nDRCV3pAqOoFp9L08WkAXdAzrI-Wufki6vS16mhg%7C1679823113%7Ce51fd666d6981bf0481c83620058a94495f2ba0334adf4c08221dcf713e14dd3; d_ticket=97f5474b57483e130dcbba3559a745c516938; n_mh=eN-JicqfS9XhMpVHEpL8Fvka-uIk6d2m4WZNseKAIL4; LOGIN_STATUS=1; store-region=cn-ah; store-region-src=uid; my_rd=1; passport_assist_user=CjyWwk5tgq1DGw0HRYKpSukx51T7yijOe-SPpXeClRO30aeV9hZM1BmGGKn9kMIfoE4TBvMYUL2wGZXNix0aSAo8fpipvBHzHNnf6zoVplREZ2OEgA5INu-VlJoh-9G5WcwizV7GTw19YHIeVIs6DPA03gbot4f_lImIFH-YEK_lrw0Yia_WVCIBA8XWMxU%3D; sso_uid_tt=ffdedc973421effcd763413bf6f6511a; sso_uid_tt_ss=ffdedc973421effcd763413bf6f6511a; toutiao_sso_user=d47a71ce47031d355c134a1cb0c87dcb; toutiao_sso_user_ss=d47a71ce47031d355c134a1cb0c87dcb; uid_tt=ffdedc973421effcd763413bf6f6511a; uid_tt_ss=ffdedc973421effcd763413bf6f6511a; sid_tt=d47a71ce47031d355c134a1cb0c87dcb; sessionid=d47a71ce47031d355c134a1cb0c87dcb; sessionid_ss=d47a71ce47031d355c134a1cb0c87dcb; s_v_web_id=verify_li7bny8c_yGteBU8P_pxiS_4iSt_9eON_bpy13mmSwFKW; passport_csrf_token=2d6e0d641b0b1641e69e07111468742e; passport_csrf_token_default=2d6e0d641b0b1641e69e07111468742e; pwa2=%223%7C1%7C3%7C1%22; __bd_ticket_guard_local_probe=1688386580166; sid_ucp_sso_v1=1.0.0-KGMyMTRjMDVmYWNjNWZhY2MxYzVkZWYwYWQ2OTEzOGQ4NWYwNzdiMzMKHQjuvcC6xAIQwLmjpQYY7zEgDDCw5IzTBTgCQPEHGgJsZiIgZDQ3YTcxY2U0NzAzMWQzNTVjMTM0YTFjYjBjODdkY2I; ssid_ucp_sso_v1=1.0.0-KGMyMTRjMDVmYWNjNWZhY2MxYzVkZWYwYWQ2OTEzOGQ4NWYwNzdiMzMKHQjuvcC6xAIQwLmjpQYY7zEgDDCw5IzTBTgCQPEHGgJsZiIgZDQ3YTcxY2U0NzAzMWQzNTVjMTM0YTFjYjBjODdkY2I; sid_guard=d47a71ce47031d355c134a1cb0c87dcb%7C1688788160%7C5184001%7CWed%2C+06-Sep-2023+03%3A49%3A21+GMT; __live_version__=%221.1.1.1250%22; download_guide=%223%2F20230702%2F0%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.991%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEekNCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRXV4MVNraitJb1h5c2J6MjBQZlRvcks1SVxyXG5xYU5kYTNoWUdqeFpHNytRWjN1ajdPMmhGVGdBVnJkOERvQWxvQkw4YU0yRzZJNHJNY3JzSmkxcDJ3aDR3YUFzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEU1FBd1JnSWhBTnV4dVQ2S214U0VLakpKK2FuOWRHMTY2UGo2cHJPZWltUjVtV3lyaXQvNVxyXG5BaUVBbFhlbTBKemJjNXh5aFlWSmNBQlJraTVwbEFBcTcyNDBZNW1rUzJJZmJZWT1cclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; SEARCH_RESULT_LIST_TYPE=%22single%22; EnhanceDownloadGuide=%221_1689593748_2_1689739897_0_0%22; _bd_ticket_crypt_cookie=ba50d468ea44f141a7647412e0ff33ed; odin_tt=16dd328280a6265abbab802ff977d0cb0421327b9cc8fa548d479f47e03125370a06ceb21549ff6a8fbfc2732851a74d4ce18be3846a6d3301c5b3da41c0d155; publish_badge_show_info=%220%2C0%2C0%2C1690033616045%22; strategyABtestKey=%221690167036.38%22; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; webcast_local_quality=null; csrf_session_id=fa8330a8675b703a689a0a7cd1e50c15; __ac_nonce=064be4d2f00c7a85bd06f; __ac_signature=_02B4Z6wo00f01MQa08QAAIDBT1FIJHp95UDEOtdAAFW-2bN48C8u1RWUUv4vRaU2amdbUrVnEaJaFDYsOHtR1xh4iuAYq1cVxK6Gp1mrqzHL9EbwH.4GEYfRu17D.m.rBPi.fAtmyNU6hgd824; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAzHiYPzkkfkKOs91eqOOT1cWB0jf5RQEl9gU4Qu1r5eI%2F1690214400000%2F0%2F0%2F1690193801248%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAzHiYPzkkfkKOs91eqOOT1cWB0jf5RQEl9gU4Qu1r5eI%2F1690214400000%2F0%2F1690193209947%2F0%22; FRIEND_NUMBER_RED_POINT_INFO=%22MS4wLjABAAAAzHiYPzkkfkKOs91eqOOT1cWB0jf5RQEl9gU4Qu1r5eI%2F1690214400000%2F1690193217469%2F0%2F0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1690798044651%2C%22type%22%3A1%7D; tt_scid=rbHheqPZA-rqqDW2R0o-fvXtq5t0qHq533DArhJ.w4mk.i7VB2l-4DPgVWJyn3cLdd94; home_can_add_dy_2_desktop=%221%22; passport_fe_beating_status=true; msToken=QsnFy0PHsdrwcrbbVD9aSwNmo-pJVFtLF-yqF6bTwy3G2Ci93uY3dwEr_o_8znG8NiW_1JiSRArW3YssaI_6XVmbDicUTjjNeISR6vxM2jinOmIXhaS3ZjvoBV2mUY57; msToken=ddKVVUOv2hguLcuF70u_sc-NRorfWI-l8jKv3SumSgfvessukxxn49TF_b7ogRX4XqnngK2horQDdy_kAuKXPwJbrOhu13aGT0pT41Y71VIq4wT5SQNT6ugREv0MP31b',
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
