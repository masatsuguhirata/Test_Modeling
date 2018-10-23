import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import page #自前で書く

class TestPythonOrgTest(object):
    def setup_method(self):
        # webdriver を指定(chorme)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://www.python.org")

    def teardown_method(self):
        self.driver.close()

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
