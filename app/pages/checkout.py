from app.pageobject.pageobjectinfo import Selectors
from app.utility.driverutility import Driverutility
from app.utility.assertutility import Assertutility
from selenium.webdriver.common.by import By


class Checkout(Driverutility, Assertutility):
    def search_product(self, driver):
        search_input_data = super().read_data("search", "camera")
        webelement_search = driver.find_element(By.XPATH, Selectors.SEARCHINPUT)
        webelement_search.send_keys(search_input_data.get("search_keyword"))
        super().select_input(webelement_search)
        super().wait_until_clickable(driver, "xpath", Selectors.SEARCHRESULT)
        webelement_search_header = driver.find_element(By.XPATH, Selectors.SEARCHRESULTHEAD)
        actual_header = super().get_text(webelement_search_header)
        expected_header = super().read_data("assert", "search_result")
        super().check_equals(actual_header, expected_header.get("data"), "Actual and expected header type is different")

    def click_product(self, driver):
        driver.find_element(By.XPATH, Selectors.PRODUCT1).click()
        super().check_element_present(driver, "xpath", Selectors.PRODUCTIMG)