#!/usr/bin/env python3
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
