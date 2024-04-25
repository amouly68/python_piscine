def ft_filter(func, iterable) -> list:
    """
    Copie de la fonction filter de Python
    args:   func: une fonction qui renvoie un booléen
            iterable: une liste
    return: liste des éléments de iterable pour lesquels func renvoie True
    """
    if func is None:
        return [item for item in iterable if item]
    elif not callable(func):
        raise TypeError("TypeError: the first argument must be a function")
    elif not hasattr(iterable, "__iter__"):
        raise TypeError("TypeError: the second argument must be an iterable")
    elif not isinstance(func(iterable[0]), bool):
        raise TypeError("TypeError: function does not return a boolean")
    return [item for item in iterable if func(item)]
    # return [item for item in iterable ]
