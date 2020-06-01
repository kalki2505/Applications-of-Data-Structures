"""
Question: Given the arrival and departures of trains in two different arrays in unsorted forms,
find the minimum number of platforms required at a railway station
-------------------------------------------------------------------------------------------------------------------

My assumptions:
1. Input data is clean. That is when there are no trains on a platform, departures can not happen
   Hence, number of arrivals > number of departures

2. Here, we considered 24 hr format of time. "00:00" to "23:59"

3. Arrivals and departures are unsorted in the list

4. Here input is
arrivals = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departures = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
Note that "9:00" is different to "09:00". And the reason is the we considered as a string and not integer.
It is simple to use "09:00" and compare rather than using separate variables like hours and minutes separately.

5. It arrival_time == departure_time then first departure occurs followed by the arrival of
   another train

6. Here we don't consider the number of people on a platform

7. Here the stack used is not of fixed length. The length is infinite (probably according the the memory of RAM)
    If you consider the stack length, the max length = len(arrivals) since
    number of arrivals can not be greater than number number of departures


"""


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False

    def push(self, data):
        self.stack += [data]
        self.top += 1

    def pop(self):
        if not self.is_empty():
            popcorn = self.stack[self.top]
            self.stack = self.stack[:self.top]
            self.top -= 1
            return popcorn
        else:
            print('\nERROR: Total departures are greater than total arrivals!')

    def print(self):
        print('\t\t>>Your stack <<<')
        print('\tTotal elements: ', self.top + 1)
        for i in range(self.top, -1, -1):
            print('\ti = ', i, '\t', self.stack[i])

    def pops(self, times):
        if times <= (self.top + 1):
            for _ in range(times):
                self.pop()
        else:
            print('\nERROR: Total departures are greater than total arrivals!')


def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    max_top = -1
    na = len(arrivals)  # total arrivals
    nd = len(departures)  # total departures
    ai = 0  # index of arrivals list
    di = 0  # index of departures list
    platform = Stack()
    while ai < na and di < nd:
        print('\n\t>>>    Arrival time:', arrivals[ai], '\tDeparture time: ', departures[di])
        if arrivals[ai] < departures[di]:
            platform.push(arrivals[ai])
            ai += 1
        elif arrivals[ai] > departures[di]:
            platform.pop()
            di += 1
        else:
            platform.pop()
            di += 1
            platform.push(arrivals[ai])
            ai += 1
        max_top = max(max_top, platform.top)
        platform.print()
    print('\n\n\tMinimum platforms required = ', max_top + 1)


arrivals = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departures = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
min_platforms(arrivals, departures)
