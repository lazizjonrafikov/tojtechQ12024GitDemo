from selenium.webdriver.common.by import By


class ShopPage:
    # self.driver.find_element(By.XPATH, "(//span[text()='Add to cart'])[1]").click()
    #
    # self.driver.find_element(By.CLASS_NAME, "wc-block-mini-cart__button ").click()
    #
    # self.driver.find_element(By.XPATH, "//span[contains(text(), 'View')]").click()
    add_to_cart_button = (By.XPATH, "(//span[text()='Add to cart'])[1]")
    cart_buttton = (By.CLASS_NAME, "wc-block-mini-cart__button ")
    view_my_cart_button = (By.XPATH, "//span[contains(text(), 'View')]")

    def __init__(self, driver):
        self.driver = driver

    def get_add_to_cart_button(self):
        return self.driver.find_element(*ShopPage.add_to_cart_button)

    def get_cart_button(self):
        return self.driver.find_element(*ShopPage.cart_buttton)

    def get_view_my_cart_button(self):
        return self.driver.find_element(*ShopPage.view_my_cart_button)



