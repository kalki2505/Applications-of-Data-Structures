"""
Question: Given the arrival and departures of trains in two different arrays in unsorted forms,
find the minimum number of platforms required at a railway station

My assumptions:
1. Input data is clean. That is when there are no trains on a platform, depratures can not happen
2. number of arrivals > number of departures
3. It arrival_time == departure_time then first departure occurs followed by the arrival of
   another train
4. Here we don't consider the number of people on a platform
5. Here the stack used is not of fixed length. The length is infinite (probably according the the memory of RAM)
    If you consider the stack length, the max length = len(arrivals) since
    number of arrivals can not be greater than number number of departures
6. Here input is
arrivals = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departures = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
Note that "9:00" is different to "09:00". And the reason is the we considered as a string and not integer.
It is simple to use "09:00" and compare rather than using separate variables like hours and minutes separately.

7. Here, we considered 24 hr format of time. "00:00" to "23:59"
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
            print('\nERROR: Elements from an empty stack can not be popped out!')

    def print(self):
        print('\t\t>>Your stack <<<')
        print('\tTotal elements: ', self.top + 1)
        for i in range(self.top, -1, -1):
            print('\ti = ', i, '\t', self.stack[i])

    def pops(self, times):
        if times <= (self.top+1):
            for _ in range(times):
                self.pop()
        else:
            print('\nError: Elements to be popped are greater than total elements in the stack!')


arrivals = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departures = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
maxtop = -1
na = len(arrivals)
nd = len(departures)
n = max(na, nd)
i = 0
ai = 0
di = 0
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
    maxtop = max(maxtop, platform.top)
    platform.print()
print('\n\n\tMinimum platforms required = ', maxtop+1)