import json
import os
import time

import pytest
from selenium import webdriver

# @allure.title("Test Login")
# @allure.description("This is test login description")
# @allure.tag("NewUI", "Essentials", "Authentication")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.label("Tester", "Andrew")
# @allure.link(f"", name="Website")
# @allure.testcase(url="", name="TMS-456")


# Setup
@pytest.fixture(scope="session")
def setup_env():
    env = int(os.getenv('ENV'))
    env_urls = {
        1: "https://dev.service.cms.newshub.kr",
        2: "https://stag.service.cms.newshub.kr",
        3: "https://service.cms.newshub.kr"
    }
    url = env_urls.get(env)
    if not url:
        print("Environment invalid")
    yield url


@pytest.fixture(scope="session")
def driver(setup_env):
    # Option browser
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)  # Disable closing browser
    # Open browser
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)
    # Go to the webpage
    driver.get(setup_env)
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.fixture(scope="session")
def get_text():
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "Datatest", "text_ko.json")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    yield data
