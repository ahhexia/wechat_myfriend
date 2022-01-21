from appium.webdriver.webdriver import WebDriver
import time


caps={}
caps['automationName'] = 'UiAutomator2'
caps['platformName'] = 'Android'
caps['platformVersion'] = '11'
caps['deviceName'] = 'rozl5xwgmbq8toaa'
caps['appPackage'] = 'com.android.settings'
caps['appActivity'] = '.MiuiSettings'
caps['unlockType'] = 'password'
caps['unlockKey'] = '949659'

# 这2个参数解决每次打开都有同意用户须知和账户登出
caps['noReset'] = True
caps['fullReset'] = False
driver = WebDriver('http://127.0.0.1:4723/wd/hub',caps)

# 不等待的话会找不到元素定位
# time.sleep(3)
driver.find_element_by_android_uiautomator('new UiSelector().textContains("连接与共享")').click()
driver.find_element_by_android_uiautomator('new UiSelector().textContains("飞行模式")').click()
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().textContains("飞行模式")').click()

# time.sleep(3)
driver.quit()

