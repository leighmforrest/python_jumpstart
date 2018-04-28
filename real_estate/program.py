import csv
import os
try:
    import statistics
except:
    print('Unable. Malfunction')

from data_types import Purchase


def print_header():
    print('--------------------------------------------------')
    print("                   REAL ESTATE APP")
    print('--------------------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'transactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    for purchase in purchases:
        print(purchase.__dict__)
    return purchases

# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print(f'found header: {header}')
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#     for line in lines[:5]:
#         print(line)


def query_data(data):

    # sort data by price
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print(f'The most expensive house is ${high_purchase.price:,} with {high_purchase.beds} beds and '
          + f'{high_purchase.baths} baths.')

    low_purchase = data[0]
    print(
        f'The most expensive house is ${low_purchase.price:,} with {low_purchase.beds} beds '
         + f'and {low_purchase.baths} baths.')

    three_beds = [
        p.price for p in data
        if p.beds == 3
    ]

    two_beds = [
        p.price for p in data
        if p.beds == 2
    ]

    # average price for three-bedrooms
    mean = statistics.mean(three_beds)
    print(f'The average house price of a three-bedroom house is ${mean}')

    # average price for two-bedrooms
    mean = statistics.mean(two_beds)
    print(f'The average house price of a two-bedroom house is ${mean}')


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


if __name__ == '__main__':
    main()