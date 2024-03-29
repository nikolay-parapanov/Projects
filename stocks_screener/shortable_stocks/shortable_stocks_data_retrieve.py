from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import shortable_stocks.get_tickers_screen_results_current_page_pagination
import general_functions.save_list_to_csv_file


def ss_data_retrieve_code():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto('https://www.shortablestocks.com/login.cgi', timeout=0)
        page.fill('input[name="Username"]', 'petar.petrof@gmail.com')
        page.fill('input[name="Password"]', 'slepha2')
        page.click('input[type="submit"]')
        # page.wait_for_load_state("load")
        # print("form was submitted")

        page.click('a[href="javascript:openScreener();"]', timeout=0)
        print('js was clicked')
        # is_visible = page.is_visible('div#screen_results', timeout=0)

        html_scrollable = page.inner_html('div.scrollable')
        # print(html_scrollable)

        soup_scrollable = BeautifulSoup(html_scrollable, 'html.parser')
        # for button in soup_scrollable:
        #     items = button.split(' ')
        soup_scrollable_buttons_list = soup_scrollable.find_all('button', {'class': 'link-button-left'})
        scroll_pages = []

        for button in soup_scrollable_buttons_list:
            current_id_long = str(button).split()[2]
            current_id = current_id_long[4:-1]

            current_name_list = str(button).split()[5:-1]
            current_name_str = '_'.join(current_name_list)

            # Scroll pages list of tuples: ex, ('screen0', '52 Week Highs at latest close')
            scroll_pages.append(['button#' + current_id, current_name_str])
        print(scroll_pages)

        for current_page in scroll_pages:
            page.click(current_page[0])

            ticker_list = []
            ticker_list = shortable_stocks.get_tickers_screen_results_current_page_pagination.get_tickers_from_screen_results_for_current_page(
                page, ticker_list)

            next_button_exists = page.query_selector('button.link-button:has-text("Next")')
            if next_button_exists == 0:
                continue
            else:
                while next_button_exists:
                    print("Pagination button with text 'Next' exists.")
                    page.click('button.link-button:has-text("Next")')
                    ticker_list = shortable_stocks.get_tickers_screen_results_current_page_pagination.get_tickers_from_screen_results_for_current_page(
                        page, ticker_list)
                    next_button_exists = page.query_selector('button.link-button:has-text("Next")')

            print('ticker_list len: ', len(ticker_list))
            print(ticker_list)

            current_page.append(ticker_list)

        print('++++++++++++++++++++++++++++++++++++++++')
        print('++++++++++++++++++++++++++++++++++++++++')
        print('RESULT :')
        for item in scroll_pages:
            print(item)

        # page.click('button#screen1')
        general_functions.save_list_to_csv_file.save_list_to_csv_file_code(scroll_pages,
                                                                          'database/shortable_stocks/shortable_stocks_initial_screener_db.csv')

    return print('retrieve is done')
