from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.input_tester import InputTester
from tests.button_tester import ButtonTester
import time

def initialize_driver():
    print("== Break-a-Page ==")

    print("Initializing chrome driver...")
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    print("Navigating to URL...")
    # driver.get("http://www.techstepacademy.com/training-ground")
    driver.get("http://www.youtube.com")

    print("Ready for testing...")
    print()

    return driver

def stress_testing(driver):
    print("== Stress Testing ==\n")

    testers = [
        InputTester(driver),
        ButtonTester(driver)
    ]

    print()

    for tester in testers:
        tester.run()

    return testers

def display_test_results(testers, test_start_time):
    print("== Test Results ==")

    test_duration = time.time() - test_start_time
    print(f"Stress Test Duration: {test_duration:.2f}")

    total_passed = 0
    total_failed = 0
    total_tested = 0
    for tester in testers:
        total_passed += tester.passed
        total_failed += tester.failed
        tested = tester.passed + tester.failed
        print(f"{tester.tag.capitalize()} Test: {tester.passed}/{tested} Passed")

    total_tested = total_passed + total_failed
    print(f"[{total_passed}/{total_tested} Passed, {total_failed} Failed]")

def main():
    # Creating driver and navigating to url
    driver = initialize_driver()

    # Creating testers and running them
    test_start_time = time.time()
    testers = stress_testing(driver)

    # Display total results
    display_test_results(testers, test_start_time)

    # Closing the driver
    driver.quit()

if __name__ == "__main__":
    main()