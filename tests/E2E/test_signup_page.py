import time
from selenium.webdriver.common.by import By

'''
# positive scenario
'''


def test_register_new_account(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "div.py-3:nth-child(3) > div:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("test12")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test12@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(1)
    assert "Latest Products" in driver.page_source


'''
#Negative scenario
'''


def test_register_new_account_with_existing_email(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "div.py-3:nth-child(3) > div:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("test12")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test12@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(1)
    text = driver.find_element(By.CSS_SELECTOR, ".fade").text
    assert text == "User with this email is already registered"
