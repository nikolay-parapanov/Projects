from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime


def extract_table_data(page):
    html_content = page.content()

    # Parsing HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting the table with class 'roundedCorners'
    table = soup.find('table', class_='roundedCorners')
    if not table:
        print("Table with class 'roundedCorners' not found")
        return None, None

    # Extracting headers from the table
    headers = [th.text.strip() for th in table.find('thead').find_all('th')]
    print("Headers found:", headers)

    # Extracting data rows from the table
    options_data_notable_options_volume = []
    for row in table.find('tbody').find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == len(headers):
            option = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
            options_data_notable_options_volume.append(option)

    print("Extracted options data:", options_data_notable_options_volume)

    return headers, options_data_notable_options_volume


def ss_login_and_options_scan():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto('https://www.shortablestocks.com/login.cgi', timeout=0)
        page.fill('input[name="Username"]', 'n.parapanoff@gmail.com')
        page.fill('input[name="Password"]', 'slepha2')
        page.click('input[type="submit"]')
        page.wait_for_load_state("load")
        print("Form was submitted")

        page.click('a[href="javascript:openOptionsNOA();"]', timeout=0)
        print('JS was clicked')

        page.click('a#formOVL')
        print("Clicked on the 'Notable Options Activity' tab")

        # Wait for the options page to load
        page.wait_for_selector('table.roundedCorners', timeout=30000)
        print('Options page loaded')

        # Extract total number of pages
        html_content = page.content()
        soup = BeautifulSoup(html_content, 'html.parser')

        pagination_info = soup.find(text=lambda x: "results" in x and "Page" in x)

        if pagination_info:
            total_pages = int(pagination_info.split('Page 1 of ')[1].split()[0])
        else:
            print("Total pages not found")
            browser.close()
            return

        print(f"Total pages: {total_pages}")

        all_data = []
        headers = None

        for current_page in range(1, total_pages + 1):
            headers, options_data = extract_table_data(page)
            if headers is None or options_data is None:
                break


            all_data.extend(options_data)

            if current_page < total_pages:
                next_button = page.query_selector('button.link-button:has-text("Next")')
                if next_button:
                    next_button.click()
                    page.wait_for_load_state("load")
                else:
                    break

        if not headers or not all_data:
            print("No data found")
            browser.close()
            return

        # Create a Pandas DataFrame from the options data
        df = pd.DataFrame(all_data)

        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")

        # Get today's date in the format YY-MM-DD
        today_date = datetime.now().strftime('%y-%m-%d')

        # Insert the date column at the beginning
        df.insert(0, 'Report Date', today_date)



        # Creating the CSV file name with the current date and time
        file_name_retrieve_general = f'daily_retrieves/options_volume_leaders_data_{timestamp}.csv'

        # Saving options data to CSV
        # df.to_csv(file_name, index=False)
        df.to_csv(file_name_retrieve_general, index=False)

        print(f"Options data saved to {file_name_retrieve_general}")

        # Closing the browser
        # browser.close()


        return