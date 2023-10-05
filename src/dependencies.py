from typing import Tuple


def set_pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    """returns params for pagination
    limit - number of objects on a page,
    skip - number of object to omit before the beginning of the result"""
    return skip, limit
