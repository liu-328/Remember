
from selenium.webdriver.common.by import By

"""
脚本名字： 测试

脚本步骤：
- 打开网址 ：http://101.34.221.219:8010/?s=user/regInfo.html
- 输入  用户名
- 输入  密码
- 点击  同意协议
- 点击  注册
"""

from webdriver_helper import get_webdriver

driver = get_webdriver()
driver.get("http://101.34.221.219:8010/?s=user/regInfo.html")
driver.find_element(
    By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[1]/input"
).send_keys("beifan222")
driver.find_element(
    By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[2]/div/input"
).send_keys("123123")
driver.find_element(
    By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[3]/label/span"
).click()
driver.find_element(
    By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[4]/button"
).click()
msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text

assert msg == "注册成功"  # 测试用例的一部分
