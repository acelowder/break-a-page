from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MissingElement(Exception):
    pass

class DisabledError(Exception):
    pass

class HiddenError(Exception):
    pass

class Tester(object):
    def __init__(self, driver, tag):
        self.driver = driver
        self.tag = tag

        self.WAIT_TIME = 5
        self.test_elements = []
        self.current_element_id = ""
        self.passed = 0
        self.failed = 0

        self.find_elements()

    def find_elements(self):
        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.tag)))

            self.test_elements = self.driver.find_elements(By.CSS_SELECTOR, self.tag)
            print(f"Found {len(self.test_elements)} {self.tag} elements...")
        except:
            print(f"Could not find any <{self.tag}> elements...")

    def test(self, element):
        raise NotImplementedError("Subclasses must implement the test method")

    def run(self):
        if len(self.test_elements) >= 1:
            print(f"Testing <{self.tag}> elements...")

        for element_num, element in enumerate(self.test_elements):
            try:
                if not element.is_present():
                    print(f"\tTesting 'element {element_num}': ", end="")
                    raise MissingElement("Element is no longer present")

                self.current_element_id = element.get_attribute('id') or element.get_attribute(
                    'name') or f"element {element_num}"
                print(f"\tTesting '{self.current_element_id}': ", end="")

                if not element.is_displayed():
                    raise HiddenError("Element is disabled")

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

        total_tested = self.passed + self.failed
        print(f"[{self.tag.capitalize()} Results: {self.passed}/{total_tested} Passed]\n")