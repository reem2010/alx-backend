#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination"""
        indexes = list(self.__indexed_dataset.keys())
        assert index is not None and index <= int(indexes[-1])
        ran = index + page_size
        count = index
        data = []
        while len(data) < page_size:
            if (count > indexes[-1]):
                break
            if (count in indexes):
                data.append(self.__indexed_dataset[count])
            count = count + 1

        res = {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': ran
        }
        return res
