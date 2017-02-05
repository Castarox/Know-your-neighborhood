import csv
from cities import Cities


def main():
    Cities.create_by_csv()
    table = Cities.count_statistic()
    for item in table:
        print(item)

if __name__ == '__main__':
    main()