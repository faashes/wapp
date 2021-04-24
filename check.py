import time
import random
from selenium import webdriver

sample = '918669996623, 919503339966'

my_list = sample.split()


str1 = ""
for m in my_list:
    str1 += m + ','

pno_buffer = str1.split(',')

print(pno_buffer)
