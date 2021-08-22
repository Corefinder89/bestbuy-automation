import json
import pandas as pd
import logging
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException


class Baseutility:
    # read configurations from project config
    def read_config(self, p_datatype, c_datatype):
        with open("app/configurations/projectconfig.json") as fobj:
            read_json = json.load(fobj)
            json_obj = read_json.get(p_datatype).get(c_datatype)

        if json_obj is not None:
            return json_obj
        else:
            raise ValueError("None type returned for association " + p_datatype + " -> " + c_datatype)

    # read data from excel sheet
    def read_data(self, data_type, keyword):
        platformdata_path = self.read_config("data", "platformdata")
        val = None
        if data_type == "customer":
            df = pd.read_excel(
                platformdata_path,
                sheet_name="customer_data"
            )

            val = df[df['user_id'].str.contains(keyword)]

        if data_type == "search":
            df = pd.read_excel(
                platformdata_path,
                sheet_name="search_keyword"
            )

            val = df[df['product_type'].str.contains(keyword)]

        if data_type == "assert":
            df = pd.read_excel(
                platformdata_path,
                sheet_name="assert_data"
            )

            val = df[df['assert_keyword'].str.contains(keyword)]

        if val.empty:
            raise ValueError("Empty data returned")
        else:
            self.set_log("info", "Fetching data for data type: %s and keyword: %s" % (data_type, keyword))
            return val.to_dict('records')[0]

    # Set log based on message type
    def set_log(self, log_type, msg):
        logging.basicConfig(filemode='w')

        logger = logging.getLogger()

        logger.setLevel(logging.INFO)

        if log_type == "debug":
            logger.debug(msg)
        if log_type == "info":
            logger.info(msg)
        if log_type == "warning":
            logger.warning(msg)
        if log_type == "error":
            logger.error(msg)
        if log_type == "critical":
            logger.critical(msg)

    # set window size of the browser when running headless
    def set_windowsize(self, driver, height, width):
        window_height = int(height)
        window_width = int(width)
        self.set_log("info", "setting window size to " + str(window_width) + "x" + str(window_height))
        driver.set_window_size(window_height, window_width)

    # replicate key press enter
    def select_input(self, element):
        if sys.platform.lower() == "darwin":
            element.send_keys(Keys.RETURN)
        else:
            element.send_keys(Keys.ENTER)
        self.set_log("info", "Press enter through key strokes")

    # Fluent wait for clickable
    def wait_until_clickable(self, driver, selector_type, selector):
        try:
            if selector_type == "xpath":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
                self.set_log("info", "clicking on element: " + selector)
                element.click()
            if selector_type == "css":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                self.set_log("info", "clicking on element: " + selector)
                element.click()
            if selector_type == "id":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, selector)))
                self.set_log("info", "clicking on element: " + selector)
                element.click()
            if selector_type == "class_name":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, selector)))
                self.set_log("info", "clicking on element: " + selector)
                element.click()
            if selector_type == "link_text":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, selector)))
                self.set_log("info", "clicking on element: " + selector)
                element.click()
            if selector_type == "name":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, selector)))
                self.set_log("info", "clicking on element: " + selector)
                element.click()
            if selector_type not in ["xpath", "css", "id", "class_name", "link_text", "name", "tag"]:
                self.set_log("error", "selector type not available")
        except NoSuchElementException:
            self.set_log("error", "element not found for " + selector)
        except ElementClickInterceptedException:
            self.set_log("error", "element is not clickable at point for " + selector)
        except InvalidElementStateException:
            self.set_log("error", "invalid element state exception for " + selector)

    # Fluent wait to check for element is present
    def check_element_present(self, driver, selector_type, selector):
        try:
            if selector_type == "xpath":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                self.set_log("info", "element " + selector + " is found")
            if selector_type == "css":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                self.set_log("info", "element " + selector + " is found")
            if selector_type == "id":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                self.set_log("info", "element " + selector + " is clickable")
            if selector_type == "class_name":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, selector)))
                self.set_log("info", "element " + selector + " is clickable")
            if selector_type == "link_text":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, selector)))
                self.set_log("info", "element " + selector + " is clickable")
            if selector_type == "name":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, selector)))
                self.set_log("info", "element " + selector + " is clickable")
        except NoSuchElementException:
            self.set_log("error", "Element not present for web element: " + selector)

    # Get text for web object
    def get_text(self, element):
        return element.text.strip()
