import time
from selenium.webdriver.common.by import By

'''
#positive scenario
'''


def test_log_in(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test11@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("t1234567")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(1)
    user_nav_bar = driver.find_element(By.CSS_SELECTOR, "#username").text
    assert "testing123" in user_nav_bar.lower()


'''
#Negative scenario
'''


def test_log_in_by_input_wrong_password(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test11@test.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("tt")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(1)
    text = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > "
                                                "div.fade.alert.alert-danger.show").text
    assert text == "No active account found with the given credentials"

