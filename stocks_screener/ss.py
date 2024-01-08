from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

import shortable_stocks.get_tickers_screen_results_current_page_pagination

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.shortablestocks.com/login.cgi', timeout=0)
    page.fill('input[name="Username"]', 'x')
    page.fill('input[name="Password"]', 'x')
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

 