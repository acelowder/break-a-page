from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementTester(object):
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
            self.test(element)

        print(f"Passed: {self.passed}/{self.passed + self.failed}")