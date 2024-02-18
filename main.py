from os import getcwd as getcwd
from pprint import pprint


# Переписать на класс
# import pprint
def read_recipes():
    file_path = getcwd() + "/recipes.txt"
    cook_book = {}
    with open(file_path, "r", encoding="utf-8") as file:
        while True:
            recipe = file.readline().strip()
            if recipe == "":
                break
            else:
                cook_book[recipe] = []
            lines = file.readline().strip()
            for i in range(int(lines)):
                ingridient_info = file.readline().strip().split(" | ")
                cook_book[recipe].append({'ingridient_name': ingridient_info[0],
                                          'quantity': int(ingridient_info[1]),
                                          'measure': ingridient_info[2]})
            empty_line = file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book=read_recipes()):
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            shop_list[ingredient['ingridient_name']] = {'measure': ingredient['measure'],
                                                        'quantity': ingredient['quantity'] * person_count}
    return shop_list


def merging_text_files(list_file: list, name_output_file: str):
    text_result = []
    for enum, file_name in enumerate(list_file, start=1):
        file_path = getcwd() + "/" + file_name
        with open(file_path, "r", encoding="utf-8") as file:
            file_text = file.readlines()
            text_result.append((file_name, file_text))
    text_result.sort(key=lambda x: len(x[1]))
    file_path = getcwd() + "/" + name_output_file
    with open(file_path, 'w', encoding="utf-8") as file:
        for tuple_name_and_text in text_result:
            file.write(tuple_name_and_text[0]+"\n")
            file.write(str(len(tuple_name_and_text[1]))+"\n")
            file.writelines(tuple_name_and_text[1])


def main():
    # cook_book = read_recipes()
    # pprint(cook_book)
    #
    # print()
    # shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    # pprint(shop_list)
    merging_text_files(['1.txt', '2.txt', '3.txt'], 'result_file.txt')


if __name__ == "__main__":
    main()
