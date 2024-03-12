from tests.tester import Tester

class InputTester(Tester):
    """A class for testing input elements.

    This class inherits from the Tester class and provides methods to test input elements.

    Attributes:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag name to search for (default is 'input').
        test_data_file (str): The path to the file containing test data.
        test_data (list): A list containing test data read from the file.
    """
    def __init__(self, driver, tag='input'):
        """Initialize the InputTester.

        Args:
            driver (WebDriver): The WebDriver instance.
            tag (str, optional): The HTML tag name to search for (default is 'input').
            test_data_file (str): Path to text file with input data
            test_data (list): List of strings read from the test data file
        """
        super().__init__(driver, tag)
        self.test_data_file = "tests/input_data.txt"
        self.test_data = self.read_test_data()

    def read_test_data(self):
        """Read test data from the input data file.

        Returns:
            list: A list containing test data read from the file.
        """
        with open(self.test_data_file, "r") as file:
            return [line.rstrip('\n') for line in file.readlines()]

    def test(self, element):
        """Test the input element by inputting all the test data.

        Args:
            element (WebElement): The input element to be tested.

        Raises:
            AssertionError: If the input value does not match the expected value.
        """
        for line_number, data in enumerate(self.test_data, start=1):
            print("\r", end="")
            print(f"\tTesting [{self.element_index}/{len(self.elements)}]: "
                  f"{self.current_element_id}: "
                  f"[{line_number}/{len(self.test_data)}] Inputting '{data}': ", end="")

            element.clear()
            element.send_keys(data)
            assert element.get_attribute("value") == data
