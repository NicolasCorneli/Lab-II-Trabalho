#Imagine que você está criando um programa para gerenciar o estoque de produtos em uma loja. Você pode usar um dicionário para rastrear os produtos, suas quantidades e preços.
    
def main():
    from paste_menu import menu
    from stock import add_product
    from historic import search_product
    from sales import sell_product
    from historic import sales_report
    from stock import search_by_category
    from stock import dell_product
    from sales import change_value
    
    historic_all = {}
    values_list = []
    my_dict = {}
    my_dict2 = {}
    while True:
        opt = menu()
        if opt == 1:
            my_dict,values_list, historic_all = add_product(my_dict,values_list,historic_all)
        elif opt == 2:
            search_product(my_dict)
        elif opt == 3:
            print(my_dict)
        elif opt == 4:
            my_dict, my_dict2, historic_all = sell_product(my_dict, my_dict2, historic_all)
        elif opt == 5:
            sales_report(my_dict2)
        elif opt == 6:
            search_by_category(my_dict)
        elif opt == 7:
            my_dict,historic_all = dell_product(my_dict,historic_all)
        elif opt == 8:
            my_dict,values_list,historic_all = change_value(my_dict,values_list,historic_all)
        elif opt == 9:
            break
    
main()
