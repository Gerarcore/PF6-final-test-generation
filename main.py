import requests
# Traer la lista de platos tipicos de Colombia

def dish_fetch(num):

    url = "https://api-colombia.com/api/v1/TypicalDish"
    response = requests.get(url)
    dishes = response.json()
    dish = dishes[num]
    dish_info = {
        "name": dish["name"],
        "description": dish["description"]
    }
    return dish_info

# Seleccionar un plato del menú:
def main():
  numero = int(input("Ingresa el número de la lista de platos:"))
  dish =dish_fetch(numero)
  print (dish)

#Resultado final
if __name__=="__main__":
  main()
