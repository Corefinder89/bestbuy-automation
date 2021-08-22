from app.pageobject.pageobjectinfo import Selectors
from app.utility.driverutility import Driverutility
from selenium.webdriver.common.by import By


class Checkout(Driverutility):
    def search_product(self, driver):
        search_data = super().read_data("search", "camera")
        webelement_search = driver.find_element(By.XPATH, Selectors.SEARCHINPUT)
        webelement_search.send_keys(search_data.get("search_keyword"))
        super().select_input(webelement_search)
        super().wait_until_clickable(driver, "xpath", Selectors.SEARCHRESULT)
