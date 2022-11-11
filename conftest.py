import pytest
from django.contrib.auth.models import User
from rest_framework.templatetags.rest_framework import data
from base.models import Product, Order, OrderItem, ShippingAddress, Review
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import warnings


@pytest.fixture()
# def driver():
#     firefox_driver_binary = "./geckodriver"
#     ser_firefox = FirefoxService(firefox_driver_binary)
#     firefox_options = FireFoxOptions()
# #     firefox_options.add_argument("--headless")
#     browser_name = 'firefox'
#     if browser_name == "firefox-webdriver":
#         driver = webdriver.Firefox(service=ser_firefox)
#     elif browser_name == "firefox":
#
#         dc = {
#             "browserName": "firefox",
#             "platformName": "Windows 11"
#         }
#         driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=firefox_options)
#
#     yield driver
#     driver.close()
def driver():
    firefox_driver_binary = "./drivers/geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()

    chrome_options = webdriver.ChromeOptions()

    browser_name = 'firefox'
    # if isinstance(browserName,list):
    #     for browser_name in browserName:
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            # "browserVersion": "101.0.1(x64)",
            "platformName": ""
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=firefox_options)
    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=chrome_options)

    elif browser_name == "Edge":

        dc = {
            "browserName": "Microsoft Edge",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=edge_options)

    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)

    elif browser_name == "android-emulator":
        dc = {
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "Android Emulator",
            # "platformVersion": "11.0.0",
            # "deviceName": "1aaa4ea80404",
            "automationName": "Appium",
            # "app": "com.android.chrome",
            "browserName": "Chrome"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

    elif browser_name == "android-phone":
        dc = {
            "platformName": "Android",
            "platformVersion": "11.0.0",
            "deviceName": "1aaa4ea80404",
            "automationName": "Appium",
            "browserName": "Chrome"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
    else:
        raise Exception("driver doesn't exists")
    yield driver
    driver.close()


@pytest.fixture()
def create_new_user(db):
    def create_app_user(
            username: str = None,
            password: str = None,
            first_name: str = "firstname",
            last_name: str = "lastname",
            email: str = "test@test.com",
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,

    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=False,
            is_superuser=False,
            is_active=True,

        )
        return user

    return create_app_user


@pytest.fixture()
def new_user(db, create_new_user):
    return create_new_user("test@test.com", "test_password", "test_name")


@pytest.fixture()
def new_superuser(db, create_new_user):
    return create_new_user("test@test.com", "test_password", "test_name", is_staff="True", is_superuser="True",
                           is_active="True")


@pytest.fixture()
def create_product(db, new_user):
    new_product = Product.objects.create(
        user=new_user,
        name="my product",
        price=1000,
        brand="my brand",
        countInStock=3,
        category="Sample category",
        description="new product")
    return new_product


@pytest.fixture()
def create_review(db, new_user, create_product):
    new_review = Review.objects.create(
        user=new_user,
        product=create_product,
        name=User.username,
        rating=3,
        comment="comment",
    )
    return new_review


@pytest.fixture()
def create_order(db, new_user):
    return Order.objects.create(
        user=new_user,
        paymentMethod='paypal',
        taxPrice=17,
        shippingPrice=25,
        totalPrice=300
    )


@pytest.fixture()
def create_shipping_address(db, create_order):
    return ShippingAddress.objects.create(
        order=create_order,
        address="taibe",
        city="taibe",
        postalCode=2222,
        country="israel",
    )


@pytest.fixture()
def create_order_item(db, create_order, create_product):
    return OrderItem.objects.create(
        product=create_product,
        order=create_order,
        name=Product.name,
        qty=2,
        price=10,
        # image=Product.image.url,
    )
