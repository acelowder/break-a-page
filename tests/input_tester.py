from tests.tester import Tester

class InputTester(Tester):
    def __init__(self, driver, tag='input'):
        super().__init__(driver, tag)
        self.test_data_file = "tests/input_data.txt"
        self.test_data = []

        self.read_test_data()

    def read_test_data(self):
        with open(self.test_data_file, "r") as file:
            self.test_data = [line.rstrip('\n') for line in file.readlines()]

    def test(self):
        pass