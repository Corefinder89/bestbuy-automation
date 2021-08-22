import json
import pandas as pd
import logging
import sys
from selenium.webdriver.common.keys import Keys


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

        if val.empty:
            raise ValueError("Empty data returned")
        else:
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