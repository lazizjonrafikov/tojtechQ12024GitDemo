from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.cartPage import CartPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.shopPage import ShopPage
from utilities.baseClass import BaseClass


class TestEndToEnd(BaseClass):
    def test_end_to_end(self):
        shop_page = ShopPage(self.driver)
        shop_page.get_add_to_cart_button().click()
        shop_page.get_cart_button().click()
        shop_page.get_view_my_cart_button().click()
        cart_page = CartPage(self.driver)
        cart_page.get_add_coupon_button().click()
        cart_page.get_coupon_input_field().send_keys("Tojtech-10$")
        cart_page.get_apply_button().click()
        cart_page.get_proceed_to_checkout_button().click()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.get_country_field().send_keys("Uni")

        for country in checkout_page.get_list_of_countries():
            if country.text == "United Kingdom (UK)":
                country.click()
                break



        # list_of_countries = self.driver.find_elements(By.CSS_SELECTOR, ".components-form-token-field__suggestion")


        # sleep(3)
        frame_element = self.driver.find_elements(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(frame_element[1])
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#Field-numberInput").send_keys("4242424242424242")
        sleep(5)
        self.driver.switch_to.default_content()
        sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Place Order']").click()
        sleep(5)
        self.driver.quit()
        print("New changes by American Timezone guy.")



