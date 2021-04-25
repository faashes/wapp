from django.shortcuts import render, HttpResponse , HttpResponseRedirect
import time

from django.urls import reverse
from selenium import webdriver
import random
import pandas


# Create your views here.

def sendfromcsv(request):
    name = request.POST['filepath']
    MasterFile_Name = r'C:\Users\Aashay\Desktop\{}'.format(name)
    df = pandas.read_csv(MasterFile_Name)

    df = df['Mobile']

    print(len(df))
    str1 = ''
    for i in range(0, len(df)):
        str1 += str(df[i]) + ','

    p_no = str1.split(',')

    msg = request.POST['content']
    browser = webdriver.Chrome("C:/Users/Aashay/Downloads/chromedriver_win32/chromedriver.exe")
    browser.get('https://web.whatsapp.com/')
    time.sleep(7 + (random.randint(1, 30)) / 100)

    for p in p_no:
        if len(p) == 10:
            p = '91' + p
        else:
            pass

    for p in p_no:
        if len(p) == 12:
            browser.get('https://api.whatsapp.com/send?phone=' + p)
            but1 = browser.find_element_by_xpath('//*[@id="action-button"]')
            but1.click()
            time.sleep(3 + (random.randint(1, 30)) / 100)
            but2 = browser.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
            but2.click()
            time.sleep(3 + (random.randint(1, 30)) / 100)

            text = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            # text = browser.find_element_by_xpath('*[ @ id = "main"] / footer / div[1] / div[2] / div / div[1]')
            text.send_keys(msg)
            time.sleep(3 + (random.randint(1, 30)) / 100)
            send = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            send.click()
            time.sleep(1 + (random.randint(1, 30)) / 100)

            time.sleep(3 + (random.randint(1, 30)) / 100)
        else:
            pass
    browser.close()
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request, 'auto/home.html')


def send(request):
    sample = request.POST['numbers']

    my_list = sample.split()

    str1 = ""
    for m in my_list:
        str1 += m + ','

    pno_buffer = str1.split(',')
    print(pno_buffer)
    browser = webdriver.Chrome("C:/Users/Aashay/Downloads/chromedriver_win32/chromedriver.exe")
    browser.get('https://web.whatsapp.com/')
    time.sleep(10 + (random.randint(1, 30)) / 100)
    msg = request.POST['content']
    for p in pno_buffer:
        if len(p) == 10:
            p = '91' + p

        if len(p) == 12:
            browser.get('https://api.whatsapp.com/send?phone=' + p)
            but1 = browser.find_element_by_xpath('//*[@id="action-button"]')
            but1.click()
            time.sleep(4 + (random.randint(1, 30)) / 100)
            but2 = browser.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
            but2.click()
            time.sleep(4 + (random.randint(1, 30)) / 100)

            text = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            text.send_keys(msg)
            time.sleep(4 + (random.randint(1, 30)) / 100)
            send = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            send.click()
            time.sleep(1 + (random.randint(1, 30)) / 100)

            time.sleep(3 + (random.randint(1, 30)) / 100)


        else:
            pass

    browser.close()
    return HttpResponseRedirect(reverse('home'))
