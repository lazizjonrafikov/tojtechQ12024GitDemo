import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None


def pytest_addoption(parser):      #creating customizing environment
    parser.addoption("--environment-name", action="store", default="firefox")  #default is po umolchaniyu


@pytest.fixture(scope="class")
def setup(request):
    global driver
    option = Options()
    option.add_experimental_option("detach", True)
    environment_name = request.config.getoption("--environment-name")
    if environment_name == "staging":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    elif environment_name == "admin":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://staging.shopping.beeyor.com/shop/")
    request.cls.driver = driver
    yield
    driver.quit()
