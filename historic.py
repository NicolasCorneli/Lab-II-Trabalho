def sales_report(my_dict2):
     for key, product in my_dict2.items():
        print("Produto:", key)
        print("Quantidade vendida:", product["quantidade vendida"])
        print("Total do valor vendido:", product["total do valor vendido"])
        print("Hora da venda:", product["hora da venda"])
        
        
def search_product(my_dict):
    name_product = input("qual produto deseja buscar: ").upper()
    
    if name_product in my_dict:
        print("produto:" , name_product)
        print("valor:" , my_dict[name_product]["value"])
        print("estoque:", my_dict[name_product]["amount"])
        print("categoria:", my_dict[name_product]["category"])
        return True
    else:
        print("o ", name_product, "nao foi buscado")
        return False
