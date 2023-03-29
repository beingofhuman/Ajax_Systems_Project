import pytest
from appium import webdriver
from framework.login_page import LoginPage

@pytest.fixture(scope="function")
def driver(request):
    desired_caps = {
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "Pixel 4",
        "appium:automationName": "UiAutomator2",
        "appium:app": "/Users/eliasbudnytskyi/Downloads/Ajax Security System_Apk.apk",
        "appPackage": "com.ajaxsystems",
        "appWaitActivity": "com.ajaxsystems.bootstrap.presentation.hello.HelloActivity",
        "appium:autoGrantPermissions": "true"
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)

    def finalizer():
        driver.quit()
    request.addfinalizer(finalizer)
    return driver

@pytest.mark.parametrize("email, password", [("qa.ajax.app.automation@gmail.com", "qa_automation_password")])
def test_login(driver, email, password):
    login_page = LoginPage(driver)
    login_page.login(email, password)
    assert driver.current_activity == '.ui.activity.DashboardActivity'

@pytest.mark.parametrize(
    "email, password",
    [
        ("incorrect_email@example.co", "qa_automation_password"),
        ("qa.ajax.app.automation@gmail.com", "incorrect_password")
    ]
)
def test_login_incorrect(driver, email, password):
    login_page = LoginPage(driver)
    login_page.login(email, password)
    assert driver.current_activity == '.auth.presentation.login.LoginActivity'
