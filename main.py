from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.input_tester import InputTester

def initialize_driver():
    print("Initializing chrome driver...")
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    print("Navigating to URL...")
    driver.get("http://www.techstepacademy.com/training-ground")
    print()

    return driver

def main():
    print("== Break-a-Page ==")
    driver = initialize_driver()

    print("== Stress Testing ==\n")
    InputTester(driver).run()

    driver.quit()

if __name__ == "__main__":
    main()