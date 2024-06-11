import pytest
from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore

@pytest.fixture
def browser():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    # Quit the driver after the test
    driver.quit()

def test_google_search(browser):
    # Open Google
    browser.get('https://www.google.com')

    # Find the search box
    search_box = browser.find_element(By.NAME, 'q')

    # Type 'VCU' in the search box
    search_box.send_keys('VCU')

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    first_result = browser.find_element(By.CSS_SELECTOR, 'h3')
    first_result.click()

    # Verify that results are displayed
    assert 'Virginia Commonwealth University' in browser.title

