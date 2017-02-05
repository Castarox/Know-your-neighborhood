from cities import Cities
from ui import Ui
import os

class Menu:

    @staticmethod
    def run():
        Cities.create_by_csv()
        while True:
            os.system('clear')
            menu_options = ['List statistics', 'Display 3 cities with longest names',
                            'Display county\'s name with the largest number of communities',
                            'Display locations, that belong to more than one category',
                            'Advanced search', 'Exit program']
            Ui.print_text('Menu:')
            Ui.print_menu(menu_options)
            Menu.choose_option()

    @staticmethod
    def choose_option():
        user_choice = Ui.get_input('\nWhich option:')
        if user_choice == '1':
            os.system('clear')
            Ui.print_table(Cities.count_statistic(), 'Małopolska')
            Ui.get_input('Enter to continue:')
        if user_choice == '2':
            os.system('clear')
            name_list = Cities.get_name_list()
            Ui.print_menu(Cities.get_longest_words(name_list))
            Ui.get_input('Enter to continue:')
        if user_choice == '3':
            os.system('clear')
            Ui.print_text(Cities.get_largest_county())
            Ui.get_input('Enter to continue:')
        if user_choice == '4':
            os.system('clear')
            Ui.print_menu(Cities.get_multi_types_objects())
            Ui.get_input('Enter to continue:')
        if user_choice == '5':
            os.system('clear')
            user_input = Ui.get_input('Searching for: ')
            search_result = Cities.search(user_input)
            if search_result:
                Ui.print_text('Fount {}'.format(len(search_result)))
                search_result.insert(0, ['Location', 'Type'])
                Ui.print_table(search_result)
                Ui.get_input('Enter to continue:')
            else:
                Ui.print_text('No match')
                Ui.get_input('Enter to continue:')
        if user_choice == '6':
            exit()