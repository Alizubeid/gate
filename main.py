from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


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


firefox = MyBrowser()
firefox.open_page("IR")
while True:
    saved_page = firefox.result_page
    if saved_page == firefox.get_real_time_page_source():
        table = (
            BeautifulSoup(saved_page, "html.parser")
            .find_all("table")[0]
            .find("tbody")
            .find_all("tr")
        )
        for row in table:
            print("From TO")
            [print(f"{ip.get_text()} ", end="\n") for ip in row.find_all("td")[:3]]
        if firefox.check_next_page():
            firefox.go_to_next_page()
        else:
            break
    else:
        firefox.page = firefox.get_real_time_page_source()
firefox.browser.quit()
