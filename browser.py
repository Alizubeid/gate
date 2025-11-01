from selenium import webdriver
from selenium.webdriver.common.by import By

class MyBrowser:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.result_page = None

    def open_page(self, country_code):
        self.browser.get(f"https://cable.ayra.ch/ip/?c={country_code}")
        self.page = self.browser.page_source

    def get_real_time_page_source(self):
        return self.browser.page_source

    @property
    def page(self):
        return self.result_page

    @page.setter
    def page(self, source):
        self.result_page = source

    def check_next_page(self):
        value = self.browser.find_element(
            By.ID, "DataTables_Table_0_next"
        ).get_attribute("class")
        return "disable" not in value

    def go_to_next_page(self):
        if self.check_next_page():
            self.browser.find_element(By.CLASS_NAME, "next").click()
            return True