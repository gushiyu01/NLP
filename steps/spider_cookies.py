from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageEnhance
import time
import pytesseract
import json

chrome_options = webdriver.ChromeOptions()
# 声明浏览器对象
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get('https://vip.dmohe.com/index.php')
# 获取当前的cookie

driver.save_screenshot('./a.png')

# 3、打开截图，获取验证码位置，截取保存验证码
ran = Image.open("./a.png")
box = (1795, 302, 1880, 342)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
ran.crop(box).save("./b.png")

# 4、获取验证码图片，读取验证码
imageCode = Image.open("./b.png") # 图像增强，二值化
# imageCode.load()
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("./c.png")
sharp_img.load()  # 对比度增强
print(sharp_img)
code = pytesseract.image_to_string(sharp_img).strip()
# 5、收到验证码，进行输入验证
print(code)

username = driver.find_element_by_name('Login_phone')
password = driver.find_element_by_name('pwd')
captcha = driver.find_element_by_name('captcha')
click = driver.find_element_by_id('showTooltips')
username.send_keys('15893732872')
password.send_keys('gu123456')
captcha.send_keys(code)
click.click()
driver.get_cookies()
coo = driver.get_cookies()
cookies = {}
for co in coo:
    cookies.setdefault(co.get('name'), co.get('value'))

with open('./cookie.json', 'a+', encoding='utf-8') as c_file:
    detail = {"name": "guchenyang", "value": cookies}
    json.dump(detail, c_file)
    c_file.write('\n')

driver.close()
