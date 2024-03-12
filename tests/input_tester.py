from tests.tester import Tester

class InputTester(Tester):
    def __init__(self, driver, tag='input'):
        super().__init__(driver, tag)
        self.test_data_file = "tests/input_data.txt"
        self.test_data = self.read_test_data()

    def read_test_data(self):
        with open(self.test_data_file, "r") as file:
            return [line.rstrip('\n') for line in file.readlines()]

    def test(self, element):
        for line_number, data in enumerate(self.test_data, start=1):
            print("\r", end="")
            print(f"\tTesting [{self.element_index}/{len(self.elements)}]: "
                  f"{self.current_element_id}: "
                  f"[{line_number}/{len(self.test_data)}] Inputting '{data}': ", end="")

            element.clear()
            element.send_keys(data)
            assert element.get_attribute("value") == data
