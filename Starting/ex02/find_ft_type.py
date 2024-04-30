def all_thing_is_obj(obj: any) -> int:
    """
    Imprime le type de l'objet donné et retourne toujours 42.

    Args:
        obj (any): L'objet dont le type doit être imprimé.

    Returns:
        int: Toujours 42.
    """
  
    obj_type = type(obj).__name__
    if obj_type == "str":
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif obj_type in ["list", "tuple", "set", "dict"]:
        print(f"{obj_type.capitalize()} : {type(obj)}")
    else:
        print("Type not found")
    
    return 42


def print_type(obj: any) -> int:
    """
    Imprime le type de l'objet donné.

    Args:
        obj (any): L'objet dont le type doit être imprimé.

    Returns:
        int: Toujours 42.
    """
    print(type(obj))
    return 42