def sell_product(my_dict,my_dict2,historic_all):
    from datetime import date
    sell_quantity = 0
    value_total = 0
    name_product = input("qual produto deseja vender: ").upper()
    if name_product in my_dict:
        sell = int(input("quantos produtos voce gostaria de vender?"))
        if sell <= my_dict[name_product]["amount"] :
            
            my_dict[name_product]["amount"] -= sell
            price_total = my_dict[name_product]["value"] * sell
            historic_all[name_product]["amount update"].append(my_dict[name_product]["amount"])
            print("o valor total foi de:", price_total)
            
            if name_product not in my_dict2:
                my_dict2[name_product] = {"quantidade vendida": sell, "total do valor vendido": price_total, "hora da venda": date.today()}
            else:
                my_dict2[name_product]["hora da venda"] = date.today()
                my_dict2[name_product]["quantidade vendida"] += sell
                my_dict2[name_product]["total do valor vendido"] += price_total
        else:
            print("esse produto esta em falta no estoque")
    else:
        print("esse produto não encontra-se no estoque!")
    return my_dict, my_dict2, historic_all
    
def change_value(my_dict,values_list,historic_all):
    name_product = input("digite o nome do produto que deseja alterar o valor: ").upper()
    if name_product in my_dict:
        
        new_value = float(input("digite um novo valor para o produto: "))
        my_dict[name_product]["value"] = new_value
        values_list.append(new_value)
        historic_all[name_product]["value update"].append(new_value)
    else:
        print("produto nao existe")
    
    return my_dict,values_list,historic_all
