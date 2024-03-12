from tests.tester import Tester
import time

class ButtonTester(Tester):
    def __init__(self, driver, tag='button'):
        super().__init__(driver, tag)

    def test(self, element):
        for x in range(10):
            element.click()
