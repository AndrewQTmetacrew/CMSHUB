import time

import allure
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.order("third")
class TestAction:
    @allure.severity(allure.severity_level.MINOR)
    def test_drag_drop(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Verify title button
        article_list_total = driver.find_elements(By.XPATH,
                                                  "//*[@id='simple-tabpanel-0']/div/div[3]/div")

        assert len(article_list_total) == 30, "Should have 30 elements"

        headline = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div[1]/div[1]/div/div[2]/div/div/main/div/div/div[1]/div[4]/div/div[1]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", headline)

        actions = ActionChains(driver)
        actions.move_to_element(headline)
        actions.click_and_hold(article_list_total[1])
        actions.move_to_element(headline)
        # actions.drag_and_drop(article_list_total[0], headline)
        actions.perform()
        # time.sleep(2)
