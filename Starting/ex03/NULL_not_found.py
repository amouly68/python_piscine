def NULL_not_found(obj: any) -> int:
    """
    Imprime le type de l'objet NULL en fonction de son nom.

    Args:
        obj (any): L'objet dont le type doit être vérifié.

    Returns:
        int: 0 si tout se passe bien, 1 en cas d'erreur.
    """
    if obj is None:
        print(obj, "<class 'NoneType'>")
    elif isinstance(obj, float) and obj != obj:
        print("Garlic:", obj, "<class 'float'>")
    elif obj == 0:
        print("Zero:", obj, "<class 'int'>")
    elif isinstance(obj, str) and obj == "":
        print("Empty:", obj, "<class 'str'>")
    elif isinstance(obj, bool):
        print(obj, ":", obj, "<class 'bool'>")
    else:
        print("Type not Found")
        return 1
    return 0

