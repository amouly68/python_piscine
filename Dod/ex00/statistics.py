
def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the statistics of a given list of numbers"""

    if not args:
        print("ERROR - No input provided")
        return

    if not all(isinstance(x, (int, float)) for x in args):
        print("ERROR - Invalid input provided")
        return

    args = [float(x) for x in args]
    args = sorted(args)
    n = len(args)
    total = sum(args)
    mean = total / n

    if (n % 2):
        median = args[n // 2]
    else:
        median = (args[n // 2 - 1] + args[n // 2]) / 2
    
    if (n % 4):
        quart1 = args[n // 4]
        quart3 = args[3 * n // 4]
    else:
        quart1 = (args[n // 4 - 1] + args[n // 4]) / 2
        quart3 = (args[3 * n // 4 - 1] + args[3 * n // 4]) / 2
    quartile = [quart1, quart3]
    variance = sum((x - mean) ** 2 for x in args) / n
    standard_deviation = variance ** 0.5

    for key, value in kwargs.items():
        if value == "mean":
            print(f"mean : {mean}")
        if value == "median":
            if median.is_integer():
                print(f"median : {int(median)}")
            else:
                print(f"median : {median}") 
        if value == "quartile":
            print(f"quartile : {quartile}")
        if value == "std":
            print(f"std : {standard_deviation}")
        if value == "var":
            print(f"var : {variance}")
