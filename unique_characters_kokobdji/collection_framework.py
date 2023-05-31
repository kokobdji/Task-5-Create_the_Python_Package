from collections import Counter
from functools import wraps
from typing import Callable, List, Set, Tuple, Union

from .exceptions import Error

CACHE_DICT = {}


def cache_check(func) -> Callable[[str], int]:
    @wraps(func)
    def inner(text: str) -> int:
        if not isinstance(text, str):
            raise Error('Only for str')
        if text in CACHE_DICT:
            return CACHE_DICT[text]
        counter = func(text)
        CACHE_DICT[text] = counter
        return counter
    return inner


@cache_check
def counter_unique_characters(text: str) -> int:
    counter_dict = Counter(text)
    counter = len([num for num in counter_dict.values() if num == 1])
    return counter


def list_input(sequence_data: Union[List[str], Set[str],
                                    Tuple[str]]) -> List[int]:
    if not isinstance(sequence_data, (list, set, tuple)):
        raise Error('Only for list, tuple, set')
    return list(map(counter_unique_characters, sequence_data))
