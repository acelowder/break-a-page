from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException

class Tester(object):
    def __init__(self, driver, tag):
        self.driver = driver
        self.tag = tag
        self.WAIT_TIME = 5
        self.elements = []
        self.passed = 0
        self.failed = 0

        self.find_elements()

    def find_elements(self):
        try:
            self.elements = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.tag)))
            print(f"Found {len(self.elements)} <{self.tag}> elements...")
        except:
            print(f"Could not find any <{self.tag}> elements...")

    def test(self, element):
        raise NotImplementedError("Subclasses must implement the test method")

    def run(self):
        if len(self.elements) >= 1:
            print(f"Testing {self.tag} elements...")

        for self.element_index, element in enumerate(self.elements, start=1):
            try:
                print(f"\tTesting [{self.element_index}/{len(self.elements)}]: ", end="")
                self.current_element_id = self.get_element_id(element)
                print(f"{self.current_element_id}: ", end="")

                if not (element.is_displayed() and element.is_enabled()):
                    raise UntargetableElement("Element is hidden or disabled")

                self.test(element)

                print("Pass")
                self.passed += 1

            except Exception as e:
                if isinstance(e, UnexpectedAlertPresentException):
                    self.dismiss_alert_if_present()

                print("Fail")
                self.failed += 1
                self.print_error_message(e)

        total_tested = self.passed + self.failed
        print(f"[{self.tag.capitalize()} Results: {self.passed}/{total_tested} Passed]\n")

    def get_element_id(self, element):
        element_id = element.get_attribute('id')
        element_name = element.get_attribute('name')
        return (
            f"id='{element_id}'" if element_id else
            f"name='{element_name}'" if element_name else
            "unidentifiable"
        )

    def dismiss_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            print("Alert")
        except NoAlertPresentException:
            pass

    def print_error_message(self, e):
        error_name = type(e).__name__
        error_message = str(e).split('\n', 1)[0] if '\n' in str(e) else str(e)
        print(f"\t\t{error_name}: {error_message}")

class UntargetableElement(Exception):
    pass
