import time

import allure
import pytest
from selenium.webdriver.common.by import By


# @pytest.mark.run
@pytest.mark.order("second")
class TestHeader:
    @allure.severity(allure.severity_level.MINOR)
    def test_title_btn_template(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Verify title button
        title_btn = driver.find_elements(By.XPATH, "//span[contains(@class, 'font-[600] text-[#9397A1]')]")
        assert title_btn[0].text == language["title_btn_template"], "Text wrong"
        title_btn[0].click()
        time.sleep(0.5)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_popup_btn_template(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Verify title popup
        title_popup = driver.find_element(By.XPATH, "//article[contains(@class, 'ant-typography')]")
        assert title_popup.text == language["title_template_popup"], "Text wrong"
        # Verify total template
        total_template = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-0']")
        assert len(total_template) == 3, "Total template wrong"
        time.sleep(0.1)

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_popup_change_template(self, driver, setup_env, get_text):
        def popup_confirm_check():
            popup_confirm = driver.find_elements(By.XPATH, "//div[contains(@tabindex, '-1')]")[0]
            assert popup_confirm.text == language["popup_confirm_change_template"]
            btn_confirm = driver.find_element(By.CSS_SELECTOR,
                                              "[class='MuiBox-root css-1o5kvuu'] [tabindex='0']:nth-of-type(2)")
            btn_confirm.click()

        # Setup
        language = get_text
        # Action elements
        btn_submit = driver.find_elements(By.XPATH, "/html//button[@type='submit']")
        assert btn_submit[1].text == language["title_select_template_popup_selected"], "Text wrong"
        assert btn_submit[2].text == language["title_select_template_popup_not_selected"], "Text wrong"
        assert btn_submit[3].text == language["title_select_template_popup_not_selected"], "Text wrong"
        btn_submit[2].click()
        popup_confirm_check()
        assert btn_submit[1].text == language["title_select_template_popup_not_selected"], "Text wrong"
        assert btn_submit[2].text == language["title_select_template_popup_selected"], "Text wrong"
        assert btn_submit[3].text == language["title_select_template_popup_not_selected"], "Text wrong"
        btn_submit[3].click()
        popup_confirm_check()
        assert btn_submit[1].text == language["title_select_template_popup_not_selected"], "Text wrong"
        assert btn_submit[2].text == language["title_select_template_popup_not_selected"], "Text wrong"
        assert btn_submit[3].text == language["title_select_template_popup_selected"], "Text wrong"
        btn_submit[1].click()
        popup_confirm_check()
        assert btn_submit[1].text == language["title_select_template_popup_selected"], "Text wrong"
        assert btn_submit[2].text == language["title_select_template_popup_not_selected"], "Text wrong"
        assert btn_submit[3].text == language["title_select_template_popup_not_selected"], "Text wrong"

    def test_menu(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Action elements
        title_btn = driver.find_elements(By.XPATH, "//span[contains(@class, 'font-[600] text-[#9397A1]')]")
        assert title_btn[3].text == language["title_btn_review"], "Text wrong"
        time.sleep(0.5)

    def test_btn_save(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Verify text
        btn_save = driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
        assert btn_save.text == language["title_btn_save"], "Text wrong"

    def test_frame_logo(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Action elements
        frame_logo = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-nb176b']")
        assert frame_logo[0].text == language["title_btn_sign_in_logo"], "Text wrong"

    def test_frame_main_section(self, driver, setup_env, get_text):
        # Setup
        language = get_text
        # Action elements
        frame_logo = driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiBox-root css-16k0pct')]")
        assert frame_logo[0].text == language["title_main_section"], "Text wrong"
