from app.pages.checkout import Checkout


class Testcheckout(Checkout):
    def test_checkout(self):
        headless_status = super().read_config("browser_config", "headless_status")
        driver = super().spawn_driver(headless_status)

        site_url = super().read_config("platform", "site")
        driver.get(site_url)

        super().search_product(driver)
        super().click_product(driver)

        driver.quit()
