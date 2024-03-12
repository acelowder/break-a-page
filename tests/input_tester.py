from tests.tester import Tester

class InputTester(Tester):
    def __init__(self, driver, tag='input'):
        super().__init__(driver, tag)
        self.test_data_file = "tests/input_data.txt"
        self.test_data_length = 0
        self.test_data = []

        self.read_test_data()

    def read_test_data(self):
        with open(self.test_data_file, "r") as file:
            self.test_data = [line.rstrip('\n') for line in file.readlines()]
            self.test_data_length = len(self.test_data)

    def test(self, element):
        for line_number, data in enumerate(self.test_data, start=1):
            print("\r", end="")
            print(f"\tTesting [{self.current_element_num}/{len(self.test_elements)}]: ", end = "")
            print(f"{self.current_element_id}: ", end="")
            print(f"[{line_number}/{self.test_data_length}] Inputting '{data}': ", end="")

            element.clear()
            element.send_keys(data)
            assert element.get_attribute("value") == data
