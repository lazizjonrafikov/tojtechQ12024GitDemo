from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    add_coupon_button = (By.XPATH, "//a[@aria-label='Add a coupon']")
    coupon_input_field = (By.ID, "wc-block-components-totals-coupon__input-0")
    apply_button = (By.XPATH, "//span[text()='Apply']")
    proceed_to_checkout_button = (By.XPATH, "//span[text()='Proceed to Checkout']")

    def get_add_coupon_button(self):
        return self.driver.find_element(*CartPage.add_coupon_button)

    def get_coupon_input_field(self):
        return self.driver.find_element(*CartPage.coupon_input_field)

    def get_apply_button(self):
        return self.driver.find_element(*CartPage.apply_button)

    def get_proceed_to_checkout_button(self):
        return self.driver.find_element(*CartPage.proceed_to_checkout_button)



# self.driver.find_element(By.XPATH, "//a[@aria-label='Add a coupon']").click()
#
# self.driver.find_element(By.ID, "wc-block-components-totals-coupon__input-0").send_keys("Tojtech-10$")
#
# self.driver.find_element(By.XPATH, "//span[text()='Apply']").click()
#
# self.driver.find_element(By.XPATH, "//span[text()='Proceed to Checkout']").click()

