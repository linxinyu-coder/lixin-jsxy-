#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:40:54 2021

@author: lin
"""


import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions

try:
    a={
      #'986': 'I', 'l'
      '998': '1',
      '1068': 'l',
      '1081': '1',
      '1082': 'v',
      '1130': 'Y',
      '1134': 'Y',
      '1164': 'v',
      '1172': 'v',
      '1216':'Y',
      '1274': 'L',
      '1224': 'Y',
      #'1274': 'L', 'y',
      '1298': 'V',
      '1311': 'V',
      '1360': 'i',
      '1373':'y',
      #'1380': 'L', 'y',
      '1406': 'V',
      '1473': 'i',
      '1478': 'T',
      '1491': 'r',
      #'1598': 'N', 'X',
      '1601': 'T',
      '1604': 'X',
      '1610': 'J',
      '1613': 'x',
      '1614': 'N',
      #'1615': 'r', 'N',
      '1616': 'N',
      '1617': 'N',
      '1618': 'N',
      '1634': 'k',
      '1637': 'k',
      '1689':'N',
      #'1694': 'z', 't',
      '1706': 'k',
      '1707':'x',
      '1709': 'K',
      #'1731': 'X', 'N',
      #'1744': 'x', 'J',
      '1754': 'F',
      '1770': 'k',
      #'1835': 'z', 't',
      '1838': 'u',
      '1840': 'A',
      '1844': 'A',
      '1848': 'K',
      '1850': 'Z',
      '1853': 'Z',
      '1886': 'h',
      '1900': 'F',
      '1922': 'H',
      '1928': 'H',
      '1960': 'P',
      '1985': 'u',
      '1991': 'u',
      '1993': 'A',
      '1996': 'D',
      '2004': 'Z',
      '2012': 'w',
      '2018': 'w',
      '2035': 'w',
      '2042': '7',
      '2043': 'h',
      '2080': 'j',
      '2082': 'H',
      '2104': 'R',
      '2107': 'R',
      '2117': 'P',
      '2123': 'P',
      '2140': '4',
      '2160':'w',
      '2162': 'D',
      '2164': 'O',
      '2183': 'w',
      #'2198': 'n', 'C',
      '2198': 'C',
      '2200': 'C',
      '2201': 'C',
      '2202': 'C',
      '2210': 'f',
      '2212': '7',
      '2241': 'j',
      '2246': 'E',
      '2253': 'j',
      '2260': 'o',
      '2264':'R',
      '2272':'M',
      #'2279': 'R', 'M',
      '2282': 'M',
      '2285':'M',
      '2294': 'U',
      '2301': 'U',
      '2303': 'W',
      '2310': 'W',
      #'2318': '4', 'W',
      '2321': 'M',
      '2332': 'a',
      '2344': 'O',
      '2345': 'W',
      '2346': 'W',
      '2366': 's',
      '2380': 'b',
      #'2381': 'n', 'C',
      '2382': '0',
      '2394': 'f',
      '2409': 'M',
      '2422': 'E',
      '2433': 'E',
      '2446': 'U',
      '2448': 'o',
      '2461': 'd',
      '2464': 'p',
      '2466': 'M',
      '2485': 'U',
      '2498': 'c',
      '2501': 'e',
      '2503': 'a',
      '2512': 'q',
      '2526': 'a',
      '2546': '2',
      '2563': 's',
      '2565':'b',
      '2578': 'b',
      '2580': '0',
      '2606': '5',
      '2632': '6',
      '2669': 'p',
      '2706': 'c',
      '2709': 'e',
      '2721': 'q',
      '2758': '2',
      '2800': '9',
      '2823': '5',
      '2851': '6',
      '3033': '9',
      '3038': 'S',
      '3054': 'B',
      '3160': 'g',
      '3244': 'Q',
      '3254': 'Q',
      '3266': 'G',
      '3291': 'S',
      '3308': 'B',
      '3394': 'g',
      '3414': '8',
      '3423': 'g',
      '3514': 'Q',
      '3538': 'G',
      '3663': 'm',
      '3667': 'm',
      '3698': '8',
      '3878': '3',
      '3914': 'm',
      '3968': 'm',
      '4165': '3',
      '4168': '3',
      '1694':'t',
      }
    ci=0
    li=0        
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_experimental_option('w3c',  False)
    browser = webdriver.Chrome(options=opt)
    while True:
        M=0
        browser.get('http://222.190.105.10:8455/')
        time.sleep(5)
        doc = browser.find_element_by_xpath('/html/body/div/div/div[4]/label')
        TouchActions(browser).tap(doc).perform()
        time.sleep(15)
        browser.find_element_by_xpath('/html/body/div/div/button').click()
        M=M+1#错误原因1:网页已打开
        browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[2]/div/input').send_keys('js20180316')
        browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys('123456')
        time.sleep(1)
        jsxyurl='http://222.190.105.10:8455/login'
        n=0
        while browser.current_url==jsxyurl:
            q=0
            w=0
            e=0
            r=0
            a1=0
            a2=0
            a3=0
            a4=0
            for i in range(1,7):
                name = browser.find_element_by_css_selector("#app > div > div.yd-flexbox-item.logo-content.yd-flexbox-item-center > div.yd-cell-box > div > div:nth-child(3) > div.yd-cell-right > div > svg > path:nth-child("+str(i)+")")
                key=name.get_attribute('d')
                location=name.location
                location=location['x']
                lenkey=len(key)
                
                if lenkey<100:
                    continue
               # print('位置',location)
                try:
                    lin=a[str(len(key))]
                except:
                    lin=0
                #print('元素',lin)
               # print('长度值',lenkey)
                if location>q and location>w and location>e and location>r:
                    r,e,w,q=location,r,e,w
                    a4,a3,a2,a1=lin,a4,a3,a2
                elif location>q and location>w and location>e and location<r:
                    e,w,q=location,e,w
                    a3,a2,a1=lin,a3,a2
                elif location>q and location>w and location<e and location<r:
                    w,q=location,w
                    a2,a1=lin,a2
                else:
                    q=location
                    a1=lin
            A=str(a1)+str(a2)+str(a3)+str(a4)
            browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[3]/div[2]/input').send_keys(A)
            time.sleep(2)
            browser.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/button').click()
            time.sleep(5)
            n=n+1
            if n>40:
                
                mail_server = "smtp.126.com"
                mail_port = 25
                sender = "linxinyu0110@126.com"
                sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
                receivers = "1017270114@qq.com"
                
                
                message = MIMEText('错误原因:验证码错误次数过多', 'plain', 'utf-8')
                message['From'] = sender
                message['To'] = receivers
                
                send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                subject = '打卡失败' + send_time 
                message['Subject'] = subject
                
                
                
                smtp_obj = smtplib.SMTP()
                smtp_obj.connect(mail_server, mail_port)
                smtp_obj.login(sender, sender_password)
                smtp_obj.sendmail(sender, [receivers], message.as_string())
                li=999999
                break
        if li==999999:
            break
            browser.close()
        M=M+1#错误原因2:网页已登陆
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[14]/div/div[2]/div/input').send_keys('36.5')
        M=M+1#错误原因3:温度已填写
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[16]/button').click()
        M=M+1#错误原因4:按钮已按
        time.sleep(5)
        if browser.current_url!='http://222.190.105.10:8455/student/perday':
            
            mail_server = "smtp.126.com"
            mail_port = 25
            sender = "linxinyu0110@126.com"
            sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
            receivers = "1017270114@qq.com"
            
            
            message = MIMEText('打卡成功', 'plain', 'utf-8')
            message['From'] = sender
            message['To'] = receivers
            
            send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            subject = '打卡成功' + send_time 
            message['Subject'] = subject
            
            
            
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(mail_server, mail_port)
            smtp_obj.login(sender, sender_password)
            smtp_obj.sendmail(sender, [receivers], message.as_string())
            browser.close()
            break
        else:
            browser.close()
            ci=ci+1
            if ci>4:
                mail_server = "smtp.126.com"
                mail_port = 25
                sender = "linxinyu0110@126.com"
                sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
                receivers = "1017270114@qq.com"
                
                
                message = MIMEText('打卡失败:页面元素错误', 'plain', 'utf-8')
                message['From'] = sender
                message['To'] = receivers
                
                send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                subject = '打卡失败' + send_time 
                message['Subject'] = subject
                
                
                
                smtp_obj = smtplib.SMTP()
                smtp_obj.connect(mail_server, mail_port)
                smtp_obj.login(sender, sender_password)
                smtp_obj.sendmail(sender, [receivers], message.as_string())
                browser.quit()
                break
except:
    mail_server = "smtp.126.com"
    mail_port = 25
    sender = "linxinyu0110@126.com"
    sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
    receivers = "1017270114@qq.com"
    
    M=str(M)
    M1='打卡失败:错误原因'+M
    message = MIMEText(M1, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receivers
    
    send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    subject = '打卡失败' + send_time 
    message['Subject'] = subject
    
    
    
    smtp_obj = smtplib.SMTP()
    smtp_obj.connect(mail_server, mail_port)
    smtp_obj.login(sender, sender_password)
    smtp_obj.sendmail(sender, [receivers], message.as_string())
    browser.quit()

    


