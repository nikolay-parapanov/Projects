from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime
import os

def convert_date_format(date_str):
    try:
        # Check if the date_str contains '-' and is in '%Y-%m-%d' format
        if '-' in date_str:
            # Parse the date in '%Y-%m-%d' format
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Convert it to '%m/%d/%Y' format
            return date_obj.strftime('%m/%d/%Y')
        else:
            # Return as is if it doesn't match the expected format
            return date_str
    except ValueError:
        # Return as is if there is a parsing error
        return date_str

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
    # print("Headers found:", headers)

    # Extracting data rows from the table
    options_data_notable_options_volume = []
    for row in table.find('tbody').find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == len(headers):
            option = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
            options_data_notable_options_volume.append(option)

    # print("Extracted options data:", options_data_notable_options_volume)

    return headers, options_data_notable_options_volume

def combine_dataframes(new_df, combined_file_name):
    if os.path.isfile(combined_file_name):
        print("Reading existing data...")
        combined_df = pd.read_csv(combined_file_name)
        print('NEW DF ...................................................')
        print(new_df)

        # Convert dates in 'Expiration Date' and 'Report Date' columns if they are in '%Y-%m-%d' format
        print("Converting dates in 'Expiration Date' and 'Report Date' columns...")
        combined_df['Expiration Date'] = combined_df['Expiration Date'].apply(lambda x: convert_date_format(str(x)))
        combined_df['Report Date'] = combined_df['Report Date'].apply(lambda x: convert_date_format(str(x)))

        print('COMBINED DF 1111111111111 ...................................................')
        print(combined_df)

        # Ensure 'Report Date' is in datetime format
        combined_df['Report Date'] = pd.to_datetime(combined_df['Report Date'], format='%m/%d/%Y', errors='coerce')
        # combined_df['Expiration Date'] = pd.to_datetime(combined_df['Expiration Date'], format='%m/%d/%Y', errors='coerce')

        print('COMBINED DF 22222222222222...................................................')
        print(combined_df)

        today_date_str = new_df['Report Date'].iloc[0]
        print(f"Filtering out old data with Report Date: {today_date_str}")

        today_date_dt = pd.to_datetime(today_date_str, format='%m/%d/%Y').date()

        combined_df['Report Date'] = pd.to_datetime(combined_df['Report Date'], format='%m/%d/%Y',
                                                        errors='coerce').dt.date
        combined_df['Expiration Date'] = pd.to_datetime(combined_df['Expiration Date'], format='%m/%d/%Y',
                                                    errors='coerce').dt.date

        print('COMBINED DF 222222222...................................................')
        print(combined_df)

        print("TODAYS DATE TO BE FILTERED OUT FROM COMBINED FILE:")
        print(today_date_dt)

        print("Report date types before filter out check: !?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!")
        print("Today date")
        print(type(today_date_dt))
        print("First cell")
        print(type(combined_df.iloc[0, 0]))


        # Filter out rows with the same Report Date
        combined_df = combined_df[combined_df['Report Date'] != today_date_dt]
        print(f"Filtered data shape: {combined_df.shape}")


        # Concatenate new data
        combined_df = pd.concat([new_df, combined_df], ignore_index=True)
        print(f"Concatenated data shape: {combined_df.shape}")

    else:
        combined_df = new_df

    combined_df.to_csv(combined_file_name, index=False)
    print(f"Options data appended to {combined_file_name}")


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

        page.click('a#formNOA')
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

        print("VERY FIRST DF: ===========================================================")
        print(df)

        # Extract the date from the first row of the first column in the raw data
        raw_date = df.iloc[0, 0][:10]

        # Convert the extracted date to the desired format
        formatted_date = datetime.strptime(raw_date, '%Y-%m-%d').strftime('%m/%d/%Y')

        # Add date column with the formatted date
        df.insert(0, 'Report Date', formatted_date)

        print('DF clean download from SS: ____________________________________________________________')
        print(df)

        combined_file_name = 'combined/noa_combined.csv'

        # Combine new data with existing data
        combine_dataframes(df, combined_file_name)

        # Get the current date and time for timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Creating the CSV file name with the current date and time
        file_name_retrieve_general = f'daily_retrieves/notable_options_activity_data_{timestamp}.csv'
        file_name = f'noa/notable_options_activity.csv'

        # Saving options data to CSV
        df.to_csv(file_name, index=False)
        df.to_csv(file_name_retrieve_general, index=False)

        print(f"Options data saved to {file_name}")

        return