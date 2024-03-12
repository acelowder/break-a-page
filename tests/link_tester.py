from tests.tester import Tester
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class MissingLinkError(Exception):
    """An exception raised when a link element is missing a 'href' attribute."""
    pass

class LinkTester(Tester):
    """A class for testing link elements.

    This class inherits from the Tester class and provides methods to test link elements.

    Attributes:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag name to search for (default is 'a').
        start_url (str): The URL of the page where testing started.
    """
    def __init__(self, driver, tag='a'):
        super().__init__(driver, tag)
        self.start_url = self.driver.current_url
        self.tag = "link"

    def test(self, element):
        """Test the link element by ctrl+clicking the link, checking the new tab, and closing the tab after it loads.

        Args:
            element (WebElement): The link element to be tested.

        Raises:
            MissingLinkError: If the link element has no 'href' attribute.
        """
        link = element.get_attribute("href") or ""
        if not link:
            raise MissingLinkError("Link element has no href")

        main_window_handle = self.driver.current_window_handle

        with ActionChains(self.driver) as actions:
            actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        print(f"Navigating to '{link}': ", end="")

        all_window_handles = self.driver.window_handles
        new_window_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)

        WebDriverWait(self.driver, self.WAIT_TIME).until(
            EC.presence_of_element_located((By.TAG_NAME, 'title'))
        )

        self.driver.close()
        self.driver.switch_to.window(main_window_handle)
