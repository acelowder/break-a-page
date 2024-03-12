from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.input_tester import InputTester
from tests.button_tester import ButtonTester
from tests.link_tester import LinkTester
import time

def initialize_driver():
    print("== Break-a-Page ==")
    user_url = input("Enter a URL to stress test (press Enter for default): ") or "http://www.techstepacademy.com/training-ground"
    headless_mode = input("Run headless test? (y/n): ").lower() == 'y'

    print("\nInitializing chrome driver...")
    options = Options()
    options.add_argument('--headless') if headless_mode else None
    driver = webdriver.Chrome(options=options)

    print(f"Navigating to {user_url}...")
    driver.get(user_url)

    print("Ready for testing...\n")
    return driver

def stress_testing(driver):
    print("== Stress Testing ==")

    testers = [InputTester(driver), ButtonTester(driver), LinkTester(driver)]
    print()

    for tester in testers:
        tester.run()

    return testers

def display_test_results(testers, test_start_time):
    print("== Test Results ==")

    test_duration = time.time() - test_start_time
    minutes = int(test_duration // 60)
    seconds = int(test_duration % 60)
    print(f"Stress Test Duration: {minutes}m {seconds}s")

    total_passed, total_failed, total_tested = 0, 0, 0
    for tester in testers:
        total_passed += tester.passed
        total_failed += tester.failed

        tested = tester.passed + tester.failed
        print(f"{tester.tag.capitalize()} Test: {tester.passed}/{tested} Passed")

    total_tested = total_passed + total_failed
    print(f"[{total_tested} Tested, {total_passed} Passed, {total_failed} Failed]")

def main():
    driver = initialize_driver()
    test_start_time = time.time()
    testers = stress_testing(driver)
    display_test_results(testers, test_start_time)
    driver.quit()

if __name__ == "__main__":
    main()