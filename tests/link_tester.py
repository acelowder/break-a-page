from tests.tester import Tester
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class MissingLinkError(Exception):
    pass

class LinkTester(Tester):
    def __init__(self, driver, tag='a'):
        super().__init__(driver, tag)
        self.start_url = self.driver.current_url
        self.tag = "link"

    def test(self, element):
        link = element.get_attribute("href")

        if link == None:
            raise MissingLinkError("Link element has no href")

        # Get the current window handle
        main_window_handle = self.driver.current_window_handle

        # Open the link in a new tab/window
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        print(f"Navigating to '{link}': ", end="")

        # Switch to the new tab/windowgit ad
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)

        # Check if the new tab/window is loaded
        WebDriverWait(self.driver, self.WAIT_TIME).until(
            EC.presence_of_element_located((By.TAG_NAME, 'title'))
        )

        # Close the new tab/window
        self.driver.close()

        # Switch back to the main window
        self.driver.switch_to.window(main_window_handle)
