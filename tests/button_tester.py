from tests.tester import Tester

class ButtonTester(Tester):
    def __init__(self, driver, tag='button'):
        super().__init__(driver, tag)

    def test(self, element):
        element.click()
