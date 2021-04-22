from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    """
    Get current records for total cases
    Dummy data below
    """
    subject_cases_count: int = 46547

    observer_list: List[Observer] = []

    def attach(self, the_observer):
        print("Subscribed.")
        self.observer_list.append(the_observer)

    def detach(self, the_observer):
        self.observer_list.remove(the_observer)

    def notify(self):
        print("Sending updates to all Observers\n")
        for each_observer in self.observer_list:
            each_observer.update(self)

    def update_records(self):
        """
        Fetch records from database
        Update records with new values
        """
        print("\nFetching Records...\nUpdating Records...")
        self.subject_cases_count += randrange(0, 1000)

        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class ConcreteObserver1(Observer):
    def update(self, subject):
        if subject.subject_cases_count > 0:
            print(f"Current Cases Received by Observer 1: {subject.subject_cases_count}")


class ConcreteObserver2(Observer):
    def update(self, subject):
        if subject.subject_cases_count > 0 and subject.subject_cases_count < 100000:
            print(f"Current Cases For Observer 2: {subject.subject_cases_count}. Still at less than 1,000,000")


if __name__ == "__main__":

    subject = ConcreteSubject()

    observer_1 = ConcreteObserver1()
    subject.attach(observer_1)

    observer_2 = ConcreteObserver2()
    subject.attach(observer_2)

    subject.update_records()

    print("\nRemoving Observer 1")
    subject.detach(observer_1)

    subject.update_records()
