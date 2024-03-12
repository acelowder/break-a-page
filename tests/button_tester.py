from tests.tester import Tester
import time

class ButtonTester(Tester):
    """A class for testing button elements.

    This class inherits from the Tester class and provides methods to test button elements.

    Attributes:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag name to search for (default is 'button').
    """
    def __init__(self, driver, tag='button'):
        """Initialize the ButtonTester.

        Args:
            driver (WebDriver): The WebDriver instance.
            tag (str, optional): The HTML tag name to search for (default is 'button').
        """
        super().__init__(driver, tag)

    def test(self, element):
        """Test a button element by clicking it 10 times.

        Args:
            element (WebElement): The button element to be tested.
        """
        for x in range(10):
            element.click()
