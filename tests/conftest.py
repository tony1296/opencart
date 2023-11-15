from selenium import webdriver
import pytest

from Utilities import Readconfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = Readconfigurations.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("Edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    driver.maximize_window()
    app_url = Readconfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
