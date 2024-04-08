def file_cook(file): #Чтение файла для cook_book (Задача 1)
    cook_book = {} 
    with open(file, encoding='utf-8') as file:
        for i in file:
            dish_name = i.strip() #Омлет
            num_ing = int(file.readline()) #3
            for l in range(num_ing):
                list_ing = (file.readline()).split('|') #ингридиенты и ед.изм.
                dict_ing = {'ingredient_name' : (list_ing[0].strip()), #Словарь по ингредиентам
                            'quantity' : int(list_ing[1].strip()),
                            'measure' : list_ing[2].strip()}
                if dish_name in cook_book:
                    cook_book[dish_name] += [dict_ing]
                else:
                    cook_book[dish_name] = [dict_ing]
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count): #Рассчёт ингридиентов для персон (Задача 2)
    dishes_persons = {}
    cook_book = file_cook('recipes.txt') #Словари из задания 1
    for dish in dishes: #Цикл по входящему списку
        list_ing = cook_book[dish] #Список со словарями
        for dict_dish in list_ing:
            if dict_dish['ingredient_name'] in dishes_persons:
                pass
            else:    
                dishes_persons[dict_dish['ingredient_name']] = {'measure': dict_dish['measure'],
                                                             'quantity': dict_dish['quantity'] * person_count}
    return dishes_persons                                                 
        
(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



def write_file(list_file): #Задача 3
    final_lst = []
    for file in list_file:
        with open(file, encoding='utf-8') as f:  
            str_lst = f.readlines() #Список строк
            list_ = [str(len(str_lst)),f.name,str_lst]
            final_lst.append(list_)
    sorted(final_lst)
    with open('result.txt', 'w') as f:
        for i in sorted(final_lst):
            f.write(i[1] + '\n')
            f.write(i[0] + '\n')
            f.write(''.join(i[2]) + '\n')

write_file(['1.txt', '2.txt', '3.txt'])

            
        
    
    




    
    
    




                   