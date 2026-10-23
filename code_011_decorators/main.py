import time


def suspicious_function(param1: str, /, param2: int) -> bool:
    """
    A function in our system that we think is very slow.

    Returns:
    -------
    bool
    """

    start = time.time()

    # en realidad la función puede llamar una API, procesar un dataset
    # escribir en una BBDD etc
    # en nuestro ejemplo haremos que duerma durante 5 segundos
    time.sleep(1)
    print(f"Executed correctly in function1 with {param1=} and {param2=}")

    end = time.time()
    total_time = end - start

    print(f"Total time to execute suspicious_function took {total_time}")

    return True


def suspicious_function2(param1: str, /, param2: int, param3: str) -> bool:
    """
    A function in our system that we think is very slow.

    Returns:
    -------
    bool
    """

    # en realidad la función puede llamar una API, procesar un dataset
    # escribir en una BBDD etc
    # en nuestro ejemplo haremos que duerma durante 5 segundos
    time.sleep(5)
    print(f"Executed correctly in function2 with {param1=}, {param2=} and {param3=}")

    return True


if __name__ == "__main__":
    suspicious_function("fast", param2=10)
    suspicious_function2("slow", param2=15, param3="very slow")
