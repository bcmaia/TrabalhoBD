class App:
    def __init__(self) -> None:
        self.cmds : dict[str, callable] = dict()

    def custom_decorator(func):
        def wrapper(*args, **kwargs):
            # Code to run before the decorated function
            print("Before function execution")

            # Call the decorated function
            result = func(*args, **kwargs)

            # Code to run after the decorated function
            print("After function execution")

            # Return the result of the decorated function
            return result

        # Return the wrapper function as the decorated function
        return wrapper
