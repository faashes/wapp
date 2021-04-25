import time
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains as A
from selenium.webdriver.common.keys import Keys as K
import csv

#str1 = '918669996623,918669996623,918669996623,919930456677,919960404050,919960457609,919960599244,919960927910,919970166806,919970183026,919970198017,919970266529,919970613934,919970654832,919975568117,919975578529,919977868586,917066810969,917276445988,917350350464,917387046151,917387161665,917405590087,917415270842,917447760777,917448154553,917507111212,917507588866,917709917662,917719894495,917720048074,917755905164,917768896743,917774031577,917875322965,917875771454,917888044049,917974008725,918008204273,918055239881,918080333434,918089475972,918097452603,918105731570,918149087690,918149410555,918149449655,918279397043,918291003816,918308876606,918378999828,918425887275,918554809864,918554855799,918600143756,918600269111,918600383353,918600400522,918600696834,918657181046,918698274411,918698452717,918770581898,918793847742,918796249684,918796359940,918806165786,918830228231,918860483388,918871030735,918879499989,918888140051,918928168222,918928973646,919011021719,919011063994,919011587585,919011707425,919028449799,919028476985,919049000876,919049004892,919049829275,919074918749,919158776958,919167016917,919167538073,919168168475,919168514477,919168571917,919321699474,919325012560,919325565358,919371011886,919405537768,919420732737,919422964945,919423252849,919503446228,919503649560,919511620373,919527422100,919545144944,919545559483,919552266400,919552590898,919561033300,919619527437,919623452673,919632150490,919637314894,919637740634,919650333906,919673640505,919673709585,919673996128,919730889992,919730890868,919730901000,919742637787,919765816252,919766018041,919766930745,919767720500,919769976005,919770087374,919790467282,919811997475,919819081264,919819194583,919820004151,919820967904,919822041776'

str1 = '918669996623,918669996623,918669996623'

p_no = str1.split(',')
count = 0
msg = "To know our latest offer all the time, join our WhatsApp group. Click to join: https://chat.whatsapp.com/KhUOeOteXk41IU1EYNQ5Sc"
valid_numbers = []
invalid_numbers = []
browser = webdriver.Chrome("C:/Users/Aashay/Downloads/chromedriver_win32/chromedriver.exe")

browser.implicitly_wait(8)
browser.get('https://web.whatsapp.com/')
time.sleep(4)
a = A(browser)
for p in p_no:
    try:
        browser.get('https://api.whatsapp.com/send?phone=' + p)
        but1 = browser.find_element_by_xpath('//*[@id="action-button"]')
        but1.click()
        time.sleep(2)
        but2 = browser.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
        but2.click()
        time.sleep(4)
        attach = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        attach.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        filepath1 = r'C:\Users\Aashay\Desktop\image1.png'  # so this is image path which will be sent in the next section
        time.sleep(1 + (random.randint(1, 30)) / 100)
        image_box = browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        image_box.send_keys(filepath1)
        time.sleep(1 + (random.randint(1, 30)) / 100)

        send_image1 = browser.find_element_by_xpath('//span[@data-icon="send"]')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        send_image1.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        filepath2 = r'C:\Users\Aashay\Desktop\image2.png'
        time.sleep(1 + (random.randint(1, 30)) / 100)
        attach = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        attach.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        image_box = browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        image_box.send_keys(filepath2)
        time.sleep(1 + (random.randint(1, 30)) / 100)
        send_image1 = browser.find_element_by_xpath('//span[@data-icon="send"]')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        send_image1.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        text = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        text.send_keys(msg)
        # a.key_down(K.LEFT_CONTROL).send_keys("v").perform()
        # a.key_up(K.LEFT_CONTROL).perform()
        time.sleep(2 + (random.randint(1, 30)) / 100)
        send = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        time.sleep(1 + (random.randint(1, 30)) / 100)
        send.click()
        time.sleep(1 + (random.randint(1, 30)) / 100)
        valid_numbers.append(p)
        count += 1
        print("valid"+p)
        time.sleep(5 + (random.randint(1, 30)) / 100)


    except NoSuchElementException:
        count += 1
        invalid_numbers.append(p)
        print("invalid"+p)
        time.sleep(2)

print('Invalid numbers below:')
for i in invalid_numbers:
    print(i)
print('Valid numbers below:')
for i in valid_numbers:
    print(i)
count = str(count)
len_number = str(len(valid_numbers))
len_inv_number = str(len(invalid_numbers))
print('Total numbers tried: ' + count)
print('Number of successful messages: ' + len_number)
print('Number of unsuccessful messages: ' + len_inv_number)

with open('valid_numbers.csv', 'w') as new_file:
    for v in valid_numbers:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow([p])

with open('invalid_numbers.csv', 'w') as f:
    for v in invalid_numbers:
        csv_writer = csv.writer(f)
        csv_writer.writerow([p])
