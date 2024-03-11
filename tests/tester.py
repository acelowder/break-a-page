from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DisabledError(Exception):
    pass

class HiddenError(Exception):
    pass

class Tester(object):
    def __init__(self, driver, tag):
        self.driver = driver
        self.tag = tag

        self.WAIT_TIME = 10
        self.test_elements = []
        self.passed = 0
        self.failed = 0

        self.find_elements()

    def find_elements(self):
        WebDriverWait(self.driver, self.WAIT_TIME).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.tag)))

        self.test_elements = self.driver.find_elements(By.CSS_SELECTOR, self.tag)

    def test(self, element):
        raise NotImplementedError("Subclasses must implement the test method")

    def run(self):
        print(f"Testing {self.tag} elements...")

        for element in self.test_elements:
            print(f"\tTesting '{element.get_attribute('id') or element.get_attribute('name') or 'noname'}': ", end="")

            try:
                if not element.is_enabled():
                    raise DisabledError("Element is disabled")

                if not element.is_displayed():
                    raise HiddenError("Element is disabled")

                self.test(element)

                print("Pass")
                self.passed += 1
            except Exception as e:
                print("Fail")
                self.failed += 1

                error_name = type(e).__name__
                error_message = str(e).split('\n', 1)[0] if '\n' in str(e) else str(e)
                print(f"\t\t{error_name}: {error_message}")

        print(f"[Results: {self.passed}/{self.passed + self.failed} Passed]\n")