import time
from selenium.webdriver.common.by import By
import random

'''
# positive scenario
'''


def test_register_new_account_with_random_emails(driver):
    rnum = random.randint(2, 100)
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "div.py-3:nth-child(3) > div:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("test12")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test" + str(rnum) + "@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(3)
    user_nav_bar = driver.find_element(By.CSS_SELECTOR, "#username").text
    assert "test12" in user_nav_bar.lower()


'''
#Negative scenario
'''


def test_register_new_account_with_existing_email(driver):
    driver.get("http://127.0.0.1:8000/#/")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "div.py-3:nth-child(3) > div:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("test12")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test12@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(3)
    text = driver.find_element(By.CSS_SELECTOR, ".fade").text
    assert text == "User with this email is already registered"
