#!/usr/bin/env python3
import csv
import math
from typing import List

"""helper module"""


def index_range(page: int, page_size: int) -> tuple:
    """helper funtion
    Args:
        page: page number
        page_size: size of the page
    Returns:
        the index range
    """
    start = (page - 1) * page_size
    end = start + page_size
    ind_range = (start, end)
    return ind_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page function
            Args:
                page: page number
                page_size: size of the page
            Returns:
                the page
            """
        assert type(page_size) is int and page_size > 0
        assert type(page) is int and page > 0
        index = index_range(page, page_size)
        res = self.dataset()[index[0]: index[1]]
        return res
