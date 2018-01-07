class Bus:
    """
    >>> import copy
    >>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    >>> bus2 = copy.copy(bus1)
    >>> bus3 = copy.deepcopy(bus1)
    >>> bus1.drop('Bill')
    >>> bus2.passengers
    ['Alice', 'Claire', 'David']
    >>> bus3.passengers
    ['Alice', 'Bill', 'Claire', 'David']
    >>> bus1.pick('Peter')
    >>> bus2.passengers
    ['Alice', 'Claire', 'David', 'Peter']
    >>> bus3.passengers
    ['Alice', 'Bill', 'Claire', 'David']
    >>> basketball_team = ['Alice', 'Bill', 'Claire', 'David']
    >>> bus = Bus(basketball_team)
    >>> bus.drop('Bill')
    >>> basketball_team
    ['Alice', 'Bill', 'Claire', 'David']
    """
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class HauntedBus:
    """
    >>> bus2 = HauntedBus()
    >>> bus2.pick('Carrie')
    >>> bus2.passengers
    ['Carrie']
    >>> bus3 = HauntedBus()
    >>> bus3.passengers
    ['Carrie']
    >>> bus3.pick('Dave')
    >>> bus2.passengers
    ['Carrie', 'Dave']
    >>> bus2.passengers is bus3.passengers
    True
    """
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class TwilightBus:
    """
    >>> basketball_team = ['Alice', 'Bill', 'Claire', 'David']
    >>> bus = TwilightBus(basketball_team)
    >>> bus.drop('Bill')
    >>> basketball_team
    ['Alice', 'Claire', 'David']
    """
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)