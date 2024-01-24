import csv

def save_list_to_csv_file_code(list, path):
    print(list)
    csv_file_path = path

    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the list to the CSV file
        csv_writer.writerows(list)

    print(f'The list has been successfully saved to {csv_file_path}.')

    return