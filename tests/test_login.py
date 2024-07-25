import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.run
@pytest.mark.order("first")
class TestLogin:
    def test_login(self, driver, setup_env, get_text):
        # Action elements
        email = driver.find_element(By.ID, ":r1:")
        email.send_keys(get_text["email"])
        password = driver.find_element(By.ID, ":r2:")
        password.send_keys(get_text["password"])
        btn_login = driver.find_element(By.XPATH, "//button[@type='submit']")
        btn_login.click()
        assert driver.find_element(By.XPATH,
                                   "//img[contains(@alt, 'NEW C-HUB logo')]").is_displayed(), "Failed to login"

    def test_homepage_management(self, driver, setup_env, get_text):
        # Action elements
        bth_menu = driver.find_elements(By.XPATH, "//li[@role='menuitem']")[3]
        assert bth_menu.is_displayed(), "Homepage management not displayed"
        assert bth_menu.text == get_text["title_homepage_management"], "Homepage management title not correct"
        bth_menu.click()
        time.sleep(2)
