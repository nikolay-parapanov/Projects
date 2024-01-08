from bs4 import BeautifulSoup


def get_tickers_from_screen_results_for_current_page(page, ticker_list):
    html_results = page.inner_html('table[width="70%"].roundedCorners')
    # print(html_results)
    soup_results = BeautifulSoup(html_results, 'html.parser')
    soup_results_tickers_buttons_list = soup_results.find_all('button', {'class': 'link-button'})
    # print(soup_results_tickers_buttons_list)
    for button in soup_results_tickers_buttons_list:
        current_id = str(button).split()[3]
        ticker_list.append(current_id)
    # print(soup_results_tickers_buttons_list[1])
    # print(ticker_list)

    return ticker_list

