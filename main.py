import csv
from cities import Cities


def main():
    Cities.create_by_csv()
    print(Cities.city_list)

if __name__ == '__main__':
    main()