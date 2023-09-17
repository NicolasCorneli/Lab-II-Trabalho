def add_product(my_dict,values_list,historic_all):
    name_product = input("digite o nome de algum produto: ").upper()
    category = input("digite a categoria do produto adicionado: ").upper()
    
    if name_product not in my_dict:
        value = float(input("digite o valor do seu produto: "))
        values_list.append(value)
        amount = int(input("digite quantos deseja adicionar no estoque: "))
        my_dict[name_product] = {"value": value, "amount": amount, "category": category}
        historic_all[name_product] = {"amount update":  [amount], "value update": [value]}
        print("seu produto foi adicionado com sucesso")
    else:
        print("o produto ja esta em estoque!, quantos voce gostaria de adicionar? ")
        amount = int(input("digite a quantidade que voce deseja adicionar a mais: "))
        my_dict[name_product]["amount"] = my_dict[name_product]["amount"] + amount
        historic_all[name_product]["amount update"].append(my_dict[name_product]["amount"])
    return my_dict,values_list, historic_all
    
def search_by_category(my_dict):
    category = input("digite qual categoria Você gostaria de vizualisar: ").upper()
    for key, product in my_dict.items():
        if product["category"] == category:
            print("Produto:", key)
            print("Valor:", product["value"])
            print("Estoque:", product["amount"])
            print("Categoria:", product["category"])
            
def dell_product(my_dict, historic_all):
    name_product = input("digite o nome do produto que deseja deletar: ").upper()
    if name_product in my_dict:
        my_dict.pop(name_product)
        historic_all[name_product]["deleted products"] = []
        historic_all[name_product]["deleted products"].append(name_product)
    else:
        print("produto nao existe")
    return my_dict, historic_all
