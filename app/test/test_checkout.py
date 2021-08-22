from app.utility.driverutility import Driverutility


class Testcheckout(Driverutility):
    def test_checkout(self):
        headless_status = super().read_config("browser_config", "headless_status")
        driver = super().spawn_driver(headless_status)

        driver.get("https://www.google.co.in")
