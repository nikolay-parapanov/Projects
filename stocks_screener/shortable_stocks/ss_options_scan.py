from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import shortable_stocks.get_tickers_screen_results_current_page_pagination
import csv


def ss_login_and_options_scan():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto('https://www.shortablestocks.com/login.cgi', timeout=0)
        page.fill('input[name="Username"]', 'n.parapanoff@gmail.com')
        page.fill('input[name="Password"]', 'slepha2')
        page.click('input[type="submit"]')
        page.wait_for_load_state("load")
        print("form was submitted")

        page.click('a[href="javascript:openOptionsNOA();"]', timeout=0)
        print('js was clicked')

        # Optional: Wait for the options page to load (adjust selector as needed)
        page.wait_for_selector('#optionsPageContent')  # Replace with a real selector from the options page
        print('Options page loaded')

        # Waiting for the table to load and extracting HTML content
        page.wait_for_selector('.roundedCorners', timeout=10000)
        html_content = page.content()

        print(html_content)

        # Parsing HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extracting the table with class 'roundedCorners'
        table = soup.find('table', class_='roundedCorners')
        if not table:
            print("Table with class 'roundedCorners' not found")
            browser.close()
            return

        # Extracting headers from the table
        headers = [th.text.strip() for th in table.find('thead').find_all('th')]

        # Extracting data rows from the table
        options_data = []
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == len(headers):
                option = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
                options_data.append(option)

        # Saving options data to CSV
        with open('options_data.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(options_data)

        print("Options data saved to options_data.csv")

    # Closing the browser
        # browser.close()

    return


# scroll_pages = []
# is_visible = page.is_visible('div#screen_results', timeout=0)

# html_scrollable = page.inner_html('div.scrollable')
# # print('html_scrollable = ', html_scrollable)

# soup_scrollable = BeautifulSoup(html_scrollable, 'html.parser')
# # for button in soup_scrollable:
# #     items = button.split(' ')
# soup_scrollable_buttons_list = soup_scrollable.find_all('button', {'class': 'link-button-left'})
