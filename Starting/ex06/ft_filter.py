def ft_filter(func, iterable)->list:
    """
    Copie de la fonction filter de Python
    args:   func: une fonction qui renvoie un booléen
            iterable: une liste
    return: une liste des éléments de la liste iterable pour lesquels la fonction func renvoie True
    """
    return [item for item in iterable if func(item)]

