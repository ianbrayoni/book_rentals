import functools
import re


def error_handler(func):
    """
    Centralize try...except handling
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            f = func(*args, **kwargs)
            return f
        except Exception as e:
            # Handle error-handling
            raise e

    return wrapper


def camelize(word, uppercase_first_letter=True):
    """
    Convert strings to CamelCase.

    Examples:

        >>> camelize("device_type")
        'DeviceType'
        >>> camelize("device_type", False)
        'deviceType'
    """
    if uppercase_first_letter:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), word)
    else:
        return word[0].lower() + camelize(word)[1:]


def underlize(word):
    """
    Make an underscored, lowercase form from the expression in the string.

    Example:

        >>> underscore("DeviceType")
        'device_type'
    """
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", word)
    word = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", word)
    word = word.replace("-", "_")
    return word.lower()
