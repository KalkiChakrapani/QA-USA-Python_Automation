import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================
    # LOCATORS
    # =========================

    # Addresses
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    CALL_TAXI_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'button') and "
        "contains(normalize-space(.), 'Call a taxi')]"
    )

    # Supportive tariff
    SUPPORTIVE_TARIFF = (
        By.XPATH,
        "//div[contains(@class, 'tcard-title') and "
        "contains(normalize-space(.), 'Supportive')]"
    )

    SELECTED_SUPPORTIVE_TARIFF = (
        By.XPATH,
        "//div[contains(@class, 'tcard') and "
        "contains(@class, 'active') and "
        ".//div[contains(normalize-space(.), 'Supportive')]]"
    )

    # Phone
    # Used to open the phone-number form.
    PHONE_NUMBER_BUTTON = (
        By.CLASS_NAME,
        "np-button"
    )

    # Used for the assertion after phone confirmation.
    PHONE_NUMBER_TEXT = (
        By.CLASS_NAME,
        "np-text"
    )

    PHONE_INPUT = (
        By.ID,
        "phone"
    )

    PHONE_NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'button') and "
        "contains(@class, 'full') and "
        "normalize-space(.)='Next']"
    )

    PHONE_CODE_INPUT = (
        By.ID,
        "code"
    )

    PHONE_CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'button') and "
        "contains(@class, 'full') and "
        "normalize-space(.)='Confirm']"
    )

    # Payment
    # Used to open the payment-method section.
    PAYMENT_METHOD = (
        By.CLASS_NAME,
        "pp-text"
    )

    # Used for the Cash/Card assertion.
    PAYMENT_METHOD_VALUE = (
        By.CLASS_NAME,
        "pp-value-text"
    )

    ADD_CARD_BUTTON = (
        By.CLASS_NAME,
        "pp-plus-container"
    )

    CARD_NUMBER_INPUT = (
        By.ID,
        "number"
    )

    CARD_CODE_INPUT = (
        By.XPATH,
        "//input[@id='code' and "
        "contains(@class, 'card-input')]"
    )

    LINK_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'button') and "
        "contains(@class, 'full') and "
        "normalize-space(.)='Link']"
    )

    # Driver comment
    COMMENT_INPUT = (
        By.ID,
        "comment"
    )

    # Blanket and handkerchiefs
    BLANKET_CLICK = (
        By.XPATH,
        "//div[@class='r-sw-label' and "
        "contains(normalize-space(.), "
        "'Blanket and handkerchiefs')]"
        "/following-sibling::div[@class='r-sw']//span"
    )

    BLANKET_SWITCH = (
        By.XPATH,
        "//div[@class='r-sw-label' and "
        "contains(normalize-space(.), "
        "'Blanket and handkerchiefs')]"
        "/following-sibling::div[@class='r-sw']//input"
    )

    # Ice cream
    ICE_CREAM_PLUS = (
        By.XPATH,
        "//div[normalize-space(.)='Ice cream']"
        "/following-sibling::div[@class='r-counter']"
        "//div[@class='counter-plus']"
    )

    ICE_CREAM_COUNT = (
        By.XPATH,
        "//div[normalize-space(.)='Ice cream']"
        "/following-sibling::div[@class='r-counter']"
        "//div[@class='counter-value']"
    )

    # Final order
    ORDER_BUTTON = (
        By.CLASS_NAME,
        "smart-button"
    )

    CAR_SEARCH_MODAL = (
        By.CLASS_NAME,
        "order-body"
    )

    # =========================
    # ADDRESS METHODS
    # =========================

    def enter_from_address(self, address):
        from_input = self.wait.until(
            EC.visibility_of_element_located(
                self.FROM_INPUT
            )
        )

        from_input.clear()
        from_input.send_keys(address)

    def enter_to_address(self, address):
        to_input = self.wait.until(
            EC.visibility_of_element_located(
                self.TO_INPUT
            )
        )

        to_input.clear()
        to_input.send_keys(address)

    def get_from_address(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.FROM_INPUT
            )
        ).get_attribute("value")

    def get_to_address(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.TO_INPUT
            )
        ).get_attribute("value")

    def click_call_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CALL_TAXI_BUTTON
            )
        ).click()

    # =========================
    # SUPPORTIVE TARIFF
    # =========================

    def select_supportive_plan(self):
        selected = self.driver.find_elements(
            *self.SELECTED_SUPPORTIVE_TARIFF
        )

        if not selected:
            self.wait.until(
                EC.element_to_be_clickable(
                    self.SUPPORTIVE_TARIFF
                )
            ).click()

    def is_supportive_selected(self):
        selected = self.driver.find_elements(
            *self.SELECTED_SUPPORTIVE_TARIFF
        )

        if selected:
            return selected[0].get_attribute("class")

        return ""

    # =========================
    # PHONE
    # =========================

    def enter_phone_number(self, phone_number):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PHONE_NUMBER_BUTTON
            )
        ).click()

        phone_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PHONE_INPUT
            )
        )

        phone_input.clear()
        phone_input.send_keys(phone_number)

    def click_phone_next(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PHONE_NEXT_BUTTON
            )
        ).click()

    def enter_phone_code(self, code):
        code_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PHONE_CODE_INPUT
            )
        )

        code_input.clear()
        code_input.send_keys(code)

        self.wait.until(
            EC.element_to_be_clickable(
                self.PHONE_CONFIRM_BUTTON
            )
        ).click()

    def get_phone_number(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PHONE_NUMBER_TEXT
            )
        ).text

    # =========================
    # CREDIT CARD
    # =========================

    def get_payment_method_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PAYMENT_METHOD_VALUE
            )
        ).text

    def add_credit_card(self, card_number, card_code):
        # Open Payment Method.
        self.wait.until(
            EC.element_to_be_clickable(
                self.PAYMENT_METHOD
            )
        ).click()

        # Open Add Card.
        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_CARD_BUTTON
            )
        ).click()

        # Enter card number.
        self.wait.until(
            EC.visibility_of_element_located(
                self.CARD_NUMBER_INPUT
            )
        ).send_keys(card_number)

        # Enter CVV.
        card_code_input = self.wait.until(
            EC.visibility_of_element_located(
                self.CARD_CODE_INPUT
            )
        )

        card_code_input.send_keys(card_code)

        # Move focus away from CVV so validation is triggered.
        self.wait.until(
            EC.element_to_be_clickable(
                self.CARD_NUMBER_INPUT
            )
        ).click()

        # Allow the Link button to update.
        time.sleep(2)

        # Locate the updated Link button and click it.
        self.wait.until(
            EC.element_to_be_clickable(
                self.LINK_BUTTON
            )
        ).click()

    # =========================
    # DRIVER COMMENT
    # =========================

    def enter_driver_comment(self, message):
        comment_input = self.wait.until(
            EC.visibility_of_element_located(
                self.COMMENT_INPUT
            )
        )

        comment_input.clear()
        comment_input.send_keys(message)

    def get_driver_comment(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.COMMENT_INPUT
            )
        ).get_attribute("value")

    # =========================
    # BLANKET / HANDKERCHIEFS
    # =========================

    def order_blanket_and_handkerchiefs(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.BLANKET_CLICK
            )
        ).click()

    def is_blanket_and_handkerchiefs_selected(self):
        return self.driver.find_element(
            *self.BLANKET_SWITCH
        ).is_selected()

    # =========================
    # ICE CREAM
    # =========================

    def order_ice_creams(self, quantity):
        for _ in range(quantity):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.ICE_CREAM_PLUS
                )
            ).click()

    def get_ice_cream_quantity(self):
        value = self.wait.until(
            EC.visibility_of_element_located(
                self.ICE_CREAM_COUNT
            )
        ).text

        return int(value)

    # =========================
    # FINAL ORDER
    # =========================

    def click_order(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ORDER_BUTTON
            )
        ).click()

    def is_car_search_modal_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.CAR_SEARCH_MODAL
            )
        ).is_displayed()