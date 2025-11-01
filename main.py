from browser import MyBrowser
from bs4 import BeautifulSoup
from counter import ip_range_int
from coutries_code import CODE

firefox = MyBrowser()
for country_code in CODE:
    try:
        firefox.open_page(country_code)

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
                    tags = row.find_all("td")
                    from_ip = tags[0]
                    to_ip = tags[1]
                    ip_range = ip_range_int(from_ip.text, to_ip.text, country_code)

                if firefox.check_next_page():
                    firefox.go_to_next_page()
                else:
                    break
            else:
                firefox.page = firefox.get_real_time_page_source()
    except:
        continue
firefox.browser.quit()
