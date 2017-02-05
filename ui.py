class Ui:
    @staticmethod
    def get_input(title):
        user_input = input('{}'.format(title))
        return user_input

    @staticmethod
    def print_table(table, Head = None):
        cell_size = Ui.count_table_size(table)
        table_lenght = 0
        for item in cell_size:
            table_lenght += item
        print(table_lenght)
        print('/' + '-' * (table_lenght + len(table[0]) - 1) + '\\')
        if Head:
            print('|{:^{}}|'.format(Head, table_lenght + 1))
            print('-' * (table_lenght + len(table[0]) + 1))
        for item_number in range(len(table)):
            for i, item in enumerate(table[item_number]):
                if i == 0:
                    print('|', end="")
                print('{:^{}}|'.format(str(item), cell_size[i]), end="")

            print()
            if item_number == len(table) - 1:
                print('\\' + '-' * (table_lenght + len(table[0]) - 1) + '/')
            else:
                print('-' * (table_lenght + len(table[0]) + 1))

    @staticmethod
    def count_table_size(table):
        cell_size = []
        for i in range(len(table[0])):
            cell_size.append(len(str(table[0][i])))

        for item in table:
            for j in range(len(item)):
                if len(str(item[j])) > cell_size[j]:
                    cell_size[j] = len(str(item[j]))

        for k in range(len(cell_size)):
            cell_size[k] += 4
        return cell_size

    @staticmethod
    def print_text(text):
        print(text)

    @staticmethod
    def print_menu(menu):
        for idx in range(len(menu)):
            print('\t({}). {}'.format(idx + 1, menu[idx]))