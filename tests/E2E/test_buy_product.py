import time
from selenium.webdriver.common.by import By
import random

'''
# buy product scenario - 
1- you need to register to the website
2- login
3- choose a product 

'''


def test_buy_product_scenario(driver):
    sNum = random.randint(2, 100)
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "div.py-3:nth-child(3) > div:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("test13")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test" + str(sNum) + "@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "div.col-xl-3:nth-child(1) > div:nth-child(1) > div:nth-child(2) > "
                                         "a:nth-child(1) > div:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(@class,'w-100')]").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(2)
    driver.find_element(By.ID, "address").send_keys("taibe")
    driver.find_element(By.ID, "city").send_keys("taibe")
    driver.find_element(By.ID, "postalCode").send_keys("2222")
    driver.find_element(By.ID, "country").send_keys("israel")
    driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(2)
    text = driver.find_element(By.CSS_SELECTOR, "div.fade:nth-child(5)").text
    assert text == "Not Delivered"
