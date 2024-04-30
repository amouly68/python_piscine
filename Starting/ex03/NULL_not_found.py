def NULL_not_found(obj: any) -> int:
    """
    Imprime le type de l'objet NULL en fonction de son nom.

    Args:
        obj (any): L'objet dont le type doit être vérifié.

    Returns:
        int: 0 si tout se passe bien, 1 en cas d'erreur.
    """
    if obj is None:
        print("Nothing:", obj, "<class 'NoneType'>")
    elif isinstance(obj, float) and obj != obj:
        print("Cheese:", obj, type(obj))
    elif isinstance(obj, str) and obj == "":
        print("Empty:", obj, type(obj))
    elif isinstance(obj, bool) and obj is False:
        print("Fake:", obj, type(obj))
    elif isinstance(obj, int) and obj == 0:
        print("Zero:", obj, type(obj))
    else:
        print("Type not Found")
        return 1
    return 0

