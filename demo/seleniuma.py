# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# # 设置无窗口
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
#
# # 声明浏览器对象
# driver = webdriver.Chrome(options=chrome_options)
#
# # 设置隐式等待时间，单位为秒
# # driver.implicitly_wait(10)
#
# # 访问页面
# driver.get("https://www.baidu.com/")
#
# # 设置搜索关键词
# element = driver.find_element_by_id("kw")
# element.send_keys("Selenium", Keys.ENTER)
#
# # 显示等待10秒，直到页面右边的"相关术语"出现
# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "FYB_RD")))
# # 获取页面右边的"相关术语"
# element2 = driver.find_element_by_class_name("FYB_RD")
# print(element2.text)
# # 退出
# driver.close()
from selenium import webdriver
import time

# 声明浏览器对象
driver = webdriver.Chrome()

# 访问百度
driver.get("http://www.baidu.com")

time.sleep(2)

# 新增一个标签页
driver.execute_script('window.open()')

time.sleep(2)

# 打印标签页
print(driver.window_handles)

# 切换至标签页1（当前标签页为0）
driver.switch_to.window(driver.window_handles[1])

time.sleep(2)

# 在当前标签页访问知乎
driver.get("http://www.zhihu.com")

time.sleep(2)

# 切换至标签页0
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

# 在标签页0访问微博
driver.get("http://www.weibo.com")

time.sleep(2)

# 关闭
driver.close()

# 退出
driver.quit()
