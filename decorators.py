def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format. Please use: command [name] [phone]"
        except IndexError:
            return "Not enough arguments. Please provide required data."
    return wrapper