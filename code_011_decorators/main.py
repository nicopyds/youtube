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
    # en nuestro ejemplo haremos que duerma durante 1 segundos
    time.sleep(1)
    print(f"Executed correctly function1 with {param1=} and {param2=}")

    end = time.time()

    total_time = end - start
    print(f"Total time to execute took {total_time}")

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
    print(f"Executed correctly function2 with {param1=}, {param2=} and {param3=}")

    return True


def timer(func):
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        total_time = end - start
        print(f"Total time to execute {func.__name__} took {total_time}")

        return result

    return wrapper


suspicious_function2 = timer(func=suspicious_function2)


@timer
def suspicious_function3(param1: str, /, param2: int, param3: str) -> bool:
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
    print(f"Executed correctly function2 with {param1=}, {param2=} and {param3=}")

    return True


if __name__ == "__main__":
    suspicious_function("slow", param2=10)
    print("-" * 50)
    suspicious_function2("slow", param2=10, param3="decorator")
    print("-" * 50)
    suspicious_function3("slow", param2=10, param3="decorator")
