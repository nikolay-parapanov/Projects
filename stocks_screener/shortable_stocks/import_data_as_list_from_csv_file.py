import csv


def import_data_as_list_from_csv_file_code(path):
    csv_file_path = path

    data_list = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)  # Assuming tab-separated values

        for row in csv_reader:
            button = row[0]
            screener = row[1]
            tickers = row[2][2:-2].split('\', \'')
            # button = row_as_list[0][2:]
            # screener = row_as_list[1]
            # tickers = row_as_list[2][2:-1].split(', ')
            screen_info = [button, screener, tickers]

            data_list.append(screen_info)

    # Print the combined data
    # for screen_info in data_list:
    #     print(screen_info)

    return data_list
