import time


def suspicious_function(param1: str, /, param2: int) -> bool:
    """
    A function in our system that we think is very slow.

    Returns:
    -------
    bool
    """

    # en realidad la función puede llamar una API, procesar un dataset
    # escribir en una BBDD etc
    # en nuestro ejemplo haremos que duerma durante 5 segundos
    time.sleep(1)
    print(f"Executed correctly function1 with {param1=} and {param2=}")

    return True
