from django.shortcuts import render, HttpResponse
import time
from selenium import webdriver
import random
import pandas

# Create your views here.

def sendfromcsv(request):
    df = pandas.read_csv(r'C:\Users\Aashay\Desktop\check.csv')

    print(df)

    df = df['Mobile']

    print(df)

    print(len(df))
    str1 = ''
    for i in range(0, len(df)):
        str1 += str(df[i]) + ','

    p_no = str1.split(',')

    msg = "Thank you for overwhelming response for Alphonso mangos. We sincerely hope that you enjoyed delivered mangos. " \
          "Our next delivery date will be declared, based on government's decision about lockdown in Maharashtra. We will inform as soon as we know the dates. " \
          "In the meantime, do join our WhatsApp group to know about our latest offers on seasonal foods as well as wooden pressed oils, Sendhav namak, Turmeric Powder and Jaggery products. " \
          "Follow this link to join our WhatsApp group: https://chat.whatsapp.com/KhUOeOteXk41IU1EYNQ5Sc"
    # pno = request.POST['numbers']
    # pno_list = pno.split(",")
    browser = webdriver.Chrome("C:/Users/Aashay/Downloads/chromedriver_win32/chromedriver.exe")
    browser.get('https://web.whatsapp.com/')
    time.sleep(10 + (random.randint(1, 30)) / 100)

    for p in p_no:
        browser.get('https://api.whatsapp.com/send?phone=' + p)
        but1 = browser.find_element_by_xpath('//*[@id="action-button"]')
        but1.click()
        time.sleep(4 + (random.randint(1, 30)) / 100)
        but2 = browser.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
        but2.click()
        time.sleep(4 + (random.randint(1, 30)) / 100)

        attach = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        attach.click()

        filepath1 = r'C:\Users\Aashay\Desktop\image1.PNG'  # so this is image path which will be sent in the next section

        image_box = browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        image_box.send_keys(filepath1)
        time.sleep(1 + (random.randint(1, 30)) / 100)

        time.sleep(1 + (random.randint(1, 30)) / 100)
        send_image1 = browser.find_element_by_xpath('//span[@data-icon="send"]')
        send_image1.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        filepath2 = r'C:\Users\Aashay\Desktop\image2.PNG'
        attach = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        attach.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        image_box = browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        image_box.send_keys(filepath2)
        time.sleep(1 + (random.randint(1, 30)) / 100)
        send_image1 = browser.find_element_by_xpath('//span[@data-icon="send"]')
        send_image1.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)

        text = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        text.send_keys(msg)
        time.sleep(4 + (random.randint(1, 30)) / 100)
        send = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)

        time.sleep(3 + (random.randint(1, 30)) / 100)


def index(request):
    return render(request, 'auto/home.html')

def send(request):
    number = request.POST['numbers']
    my_list = number.split(",")

    my_list = number.split()

    print(my_list)
    str1 = ""
    for m in my_list:
        str1 += m + ','

    print(str1)

    pno_buffer = str1.split(',')
    print(pno_buffer)

    pno_list = ""

    for p in pno_buffer:
        if (len(p) == 12):
            pno_list += p + ','

    p_no = pno_list.split(',')



    # msg = request.POST['content']
    msg = "Thank you for overwhelming response for Alphonso mangos. We sincerely hope that you enjoyed delivered mangos. " \
          "Our next delivery date will be declared, based on government's decision about lockdown in Maharashtra. We will inform as soon as we know the dates. " \
          "In the meantime, do join our WhatsApp group to know about our latest offers on seasonal foods as well as wooden pressed oils, Sendhav namak, Turmeric Powder and Jaggery products. " \
          "Follow this link to join our WhatsApp group: https://chat.whatsapp.com/KhUOeOteXk41IU1EYNQ5Sc"
    # pno = request.POST['numbers']
    # pno_list = pno.split(",")
    browser = webdriver.Chrome("C:/Users/Aashay/Downloads/chromedriver_win32/chromedriver.exe")
    browser.get('https://web.whatsapp.com/')
    time.sleep(10 + (random.randint(1,30))/100)

    for p in p_no:
        browser.get('https://api.whatsapp.com/send?phone=' + p)
        but1 = browser.find_element_by_xpath('//*[@id="action-button"]')
        but1.click()
        time.sleep(4 + (random.randint(1,30))/100)
        but2 = browser.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
        but2.click()
        time.sleep(4 + (random.randint(1,30))/100)

        attach = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        attach.click()

        filepath1 = r'C:\Users\Aashay\Desktop\image1.PNG'  # so this is image path which will be sent in the next section

        image_box = browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        image_box.send_keys(filepath1)
        time.sleep(1 + (random.randint(1,30))/100)

        time.sleep(1 + (random.randint(1,30))/100)
        send_image1 = browser.find_element_by_xpath('//span[@data-icon="send"]')
        send_image1.click()
        time.sleep(1 + (random.randint(1,30))/100)
        filepath2 = r'C:\Users\Aashay\Desktop\image2.PNG'
        attach = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        attach.click()
        time.sleep(1 + (random.randint(1,30))/100)
        image_box = browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        image_box.send_keys(filepath2)
        time.sleep(1 + (random.randint(1,30))/100)
        send_image1 = browser.find_element_by_xpath('//span[@data-icon="send"]')
        send_image1.click()
        time.sleep(1 + (random.randint(1,30))/100)

        text = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        text.send_keys(msg)
        time.sleep(4 + (random.randint(1,30))/100)
        send = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send.click()
        time.sleep(1 + (random.randint(1,30))/100)

        time.sleep(3 + (random.randint(1,30))/100)





