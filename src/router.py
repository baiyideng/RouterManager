# -*- coding: utf8 -*-
#
#
#***************************
#作者：baiyideng"
#邮箱：baiyideng@outlook.com"
#博客：baiyideng.tk"
#授权方式：GPL
#***************************
import urllib2
import base64
import urllib
import random
import hashlib
import os
import subprocess
import platform
import re
from settings import *

#检测网络连通性
def NetCheck():
        url = ['http://www.163.com','http://www.baidu.com','http://www.sina.com.cn']
        res = []
        for x in url:
                try:
                        s = urllib2.urlopen(x)
                        res.append(s)
                except:
                        res.append(None)
        if not any(res):
                return False
        else:
                return True
        
#解码电信宽带账号
def decoding(account,password):
        i = 0
        ran = ''
        while i < 8:
                c = random.randint(0,15)
                s = "%x"%c
                ran += s.upper()
                i += 1
        str1 = "jepyid" + account + ran +password 
        str2 = hashlib.md5(str1).hexdigest().upper()
        return "~ghca"+ ran + "2007"+str2[:20]+account


if __name__ == '__main__':
    print u"*----------------------------------"
    print u"*程序：Router Manager"
    print u"*版本：1.0"
    print u"*作者：baiyideng"
    print u"*邮箱：baiyideng@outlook.com"
    print u"*博客：baiyideng.tk"
    print u"*声明：仅供学习交流使用。"
    print u"*----------------------------------"
    print u"*提示：首次使用前请设置好setting.py"
    print u"*----------------------------------"
    print
    print
    print

    # 请求地址
    reboot_url = 'http://' + ip+'/userRpm/SysRebootRpm.htm?Reboot=%D6%D8%C6%F4%C2%B7%D3%C9%C6%F7'
    reboot_ref ='/userRpm/SysRebootRpm.htm'

    name = decoding(pppoe_usename,pppoe_password)
    pppoe_url ='http://'+ip+'/userRpm/PPPoECfgRpm.htm?wan=0&wantype=2&acc='+name+'&psw='+pppoe_password+'&confirm='+pppoe_password+'&specialDial=100&SecType=0&sta_ip=0.0.0.0&sta_mask=0.0.0.0&linktype=4&waittime2=0&Connect=%C1%AC+%BD%D3'
    pppoe_ref ='/userRpm/PPPoECfgRpm.htm'
    
    wifi_psw_url ='http://' + ip +'/userRpm/WlanSecurityRpm.htm?vapIdx=1&secType=3&pskSecOpt=2&pskCipher=3&pskSecret='+wifi_psw +'&interval=86400&wpaSecOpt=3&wpaCipher=1&radiusIp=&radiusPort=1812&radiusSecret=&intervalWpa=86400&wepSecOpt=3&keytype=1&keynum=1&key1=&length1=0&key2=&length2=0&key3=&length3=0&key4=&length4=0&Save=%B1%A3+%B4%E6'
    wifi_psw_ref ='/userRpm/WlanSecurityRpm.htm'
    
    while 1:
        print u'输入序号设置\n1.设置PPPOE（宽带拨号）\n2.设置wifi密码\n3.重启路由器\n4.退出'
        choice = input()
        if choice == 1:
            url = pppoe_url
            ref = pppoe_ref
        if choice == 2:
            url = wifi_psw_url
            ref = wifi_psw_ref
        if choice == 3:
            url = reboot_url
            ref = reboot_ref
        if choice == 4:
            break
        if len(url)==0&len(ref)==0:
            continue
        heads = { 'Referer' : 'http://' + ip + ref}
        request = urllib2.Request(url, None, heads)
        auth = 'Basic ' + base64.encodestring('admin:'+login_pw)
        auth = auth.rstrip()
        #print auth
        cookie = 'Authorization=' + urllib.quote(auth)
        #print cookie
        request.add_header('Cookie', cookie)
        try:
                response = urllib2.urlopen(request)
        except  urllib2.HTTPError   as e    :
                print   u'验证错误\n\n'
                continue
        except  urllib2.URLError   as e    :
                print u'连接错误，请确保正确连接到路由器\n\n'
                continue
        if choice == 1:
                if NetCheck():
                        print u"网络已连通！\n\n"
                else:
                        print u"网络未连通！请检查后重新拨号\n\n"
        else:
                print u"设置完成\n\n"
                
        # print response.read().decode('gb2312').encode('utf8')
        #print response.read().decode('gb2312')
