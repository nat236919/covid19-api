import collections.abc
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class ConcreteTotalCasesAggregate(collections.abc.Iterable):
    def __init__(self):
        """
        Fetch the list of covid cases from the database
        This example provides a dummy list of items
        """

        self._data = [
            {
              "location": "US",
              "confirmed": 28605669,
              "deaths": 513091,
              "recovered": 0,
              "active": 28092578
            },
            {
              "location": "India",
              "confirmed": 11112241,
              "deaths": 157157,
              "recovered": 10786452,
              "active": 168632
            },
        ]

    def __iter__(self):
        return TotalCasesIterator(self)


class TotalCasesIterator(collections.abc.Iterator):
    """
    Implement the Iterator interface.
    """

    def __init__(self, concrete_totalcases_aggregate):
        self._concrete_totalcases_aggregate = concrete_totalcases_aggregate
        self.index = 0

    def __next__(self):
    	try:
    		case = self._concrete_totalcases_aggregate._data[self.index]
    	except IndexError:
    		raise StopIteration
    	self.index += 1
    	return case


def main():
    concrete_totalcases_aggregate = ConcreteTotalCasesAggregate()
    for each_case in concrete_totalcases_aggregate:
        """
        Use the list of cases as fit
        """
        print(each_case['location'])


if __name__ == "__main__":
    main()
