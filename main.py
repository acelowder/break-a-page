from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Stress tests

    driver.quit()

if __name__ == "__init__":
    main()