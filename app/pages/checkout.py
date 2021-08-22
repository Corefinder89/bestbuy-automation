from app.pageobject.pageobjectinfo import Search
from app.utility.driverutility import Driverutility
from selenium.webdriver.common.by import By


class Checkout(Driverutility):
    def search_product(self, driver):
        search_data = super().read_data("search", "camera")
        webelement_search = driver.find_element(By.XPATH, Search.SEARCHINPUT)
        webelement_search.send_keys(search_data.get("search_keyword"))
        super().select_input(webelement_search)