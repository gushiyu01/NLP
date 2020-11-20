from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置无窗口
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

# 声明浏览器对象
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

# 设置隐式等待时间，单位为秒
# driver.implicitly_wait(10)

# url = 'http://127.0.0.1:5000/login/'
# # 访问页面
# driver.get(url)
#
# # 获取页面右边的"相关术语"
# element2 = driver.find_element_by_id("csrf_token")
# print(element2.get_property('value'))
# driver.find_element_by_id('username').send_keys('lily')
# driver.find_element_by_id('password').send_keys('123')
# name = driver.find_elements_by_tag_name('input')
# click = name[3].click()
#
# # 新增一个标签页
# driver.execute_script('window.open()')
# # 切换至标签页1（当前标签页为0）
# driver.switch_to.window(driver.window_handles[1])
driver.maximize_window()
driver.get('https://vip.dmohe.com/index.php')
# 获取当前的cookie

driver.save_screenshot('F:/a.png')

from PIL import Image, ImageEnhance
import time
import pytesseract


# 3、打开截图，获取验证码位置，截取保存验证码
ran = Image.open("F:/a.png")
box = (1795, 302, 1880, 342)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
ran.crop(box).save("F:/b.png")

# 4、获取验证码图片，读取验证码
imageCode = Image.open("F:/b.png") # 图像增强，二值化
# imageCode.load()
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("F:/c.png")
sharp_img.load()  # 对比度增强
print(sharp_img)
code = pytesseract.image_to_string(sharp_img).strip()
# 5、收到验证码，进行输入验证
print(code)

username = driver.find_element_by_name('Login_phone')
password = driver.find_element_by_name('pwd')
captcha = driver.find_element_by_name('captcha')
click = driver.find_element_by_id('showTooltips')
username.send_keys('13523511140')
password.send_keys('123456')
captcha.send_keys(code)
click.click()
driver.get_cookies()
print(driver.get_cookies())
退出
driver.close()
coo = [{'domain': '.dmohe.com', 'httpOnly': False, 'name': 'Hm_lpvt_1f4615ff33183230f77694fcb34175ad', 'path': '/', 'secure': False, 'value': '1605757504'}, {'domain': '.vip.dmohe.com', 'expiry': 1637293503, 'httpOnly': False, 'name': 'openid', 'path': '/', 'secure': False, 'value': 'p516056794757577491'}, {'domain': '.dmohe.com', 'expiry': 1637293504, 'httpOnly': False, 'name': 'Hm_lvt_1f4615ff33183230f77694fcb34175ad', 'path': '/', 'secure': False, 'value': '1605757502'}, {'domain': 'vip.dmohe.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'tjts3dsniitc2bfmqt1ovo6jg8'}]
cookies = {}
for co in coo:
    cookies.setdefault(co.get('name'), co.get('value'))
print(cookies)
