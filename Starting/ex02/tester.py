from find_ft_type import all_thing_is_obj
from find_ft_type import print_type

# Définition des objets à tester
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Appel de la fonction pour chaque objet
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))  # Imprime le résultat de la fonction

# Appel de la fonction pour chaque objet
print_type(ft_list)
print_type(ft_tuple)
print_type(ft_set)
print_type(ft_dict)
print_type("Brian")
print_type("Toto")
print(print_type(10))  # Imprime le résultat de la fonction
