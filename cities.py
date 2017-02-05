import csv

class Cities():
    city_list = []

    def __init__(self, province, county, community, rgmi, name, type):
        self.province = province
        self.county = county
        self.community = community
        self.rgmi = rgmi
        self.name = name
        self.type = type


    @staticmethod
    def create_by_csv():
        city_table = Cities.read_from_csv('malopolska.csv')
        for row in city_table:
            new_object = Cities(row[0],row[1],row[2],row[3],row[4],row[5])
            Cities.city_list.append(new_object)

    @staticmethod
    def read_from_csv(file_name):
        new_table = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                new_table.append(row)
        return new_table

    @classmethod
    def count_statistic(cls):
        statistic = [['województwo', 0], ['powiat', 0], ['gmina miejska', 0], ['gmina wiejska', 0],
                     ['gmina miejsko-wiejska', 0], ['obszar wiejski', 0], ['miasto', 0],
                     ['miasto na prawach powiatu', 0], ['delegatura', 0]]
        for item in cls.city_list:
            statistic = Cities.change_statistic_value(item, statistic)
        return statistic


    @staticmethod
    def change_statistic_value(object_to_check, statistic_list):
        for item in statistic_list:
            if object_to_check.type == item[0]:
                item[1] += 1
        return statistic_list

    @classmethod
    def get_name_list(cls):
        name_list = []
        for item in cls.city_list:
            name_list.append(item.name)
        return  name_list

    @staticmethod
    def get_longest_words(words_list, amount = 3):
        words.list.sort(key = len, reverse = True)
        print(words_list[:amount])


    def __str__(self):
        return self.type + ' ' + self.name
