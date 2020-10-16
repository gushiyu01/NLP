from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置无窗口
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# 声明浏览器对象
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

# 设置隐式等待时间，单位为秒
# driver.implicitly_wait(10)

url = 'http://127.0.0.1:5000/login/'
# 访问页面
driver.get(url)

# 获取页面右边的"相关术语"
element2 = driver.find_element_by_id("csrf_token")
print(element2.get_property('value'))
driver.find_element_by_id('username').send_keys('lily')
driver.find_element_by_id('password').send_keys('123')
name = driver.find_elements_by_tag_name('input')
click = name[3].click()

# 新增一个标签页
driver.execute_script('window.open()')
# 切换至标签页1（当前标签页为0）
driver.switch_to.window(driver.window_handles[1])
driver.get('http://127.0.0.1:5000/index2')
# 获取当前的cookie
driver.add_cookie({
    'name': 'gsy',
    'value': 'gushiyu'
})
print(driver.get_cookies())
# 退出
# driver.close()

