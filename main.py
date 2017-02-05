import csv
from cities import Cities
from ui import Ui


def main():
    Cities.create_by_csv()
    table = Cities.count_statistic()
    Ui.print_table(Cities.count_statistic(), 'kino')

if __name__ == '__main__':
    main()