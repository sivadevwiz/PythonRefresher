# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

text = "aaaaabbbcccccc"

my_counter = Counter(text)
print(my_counter)  # Counter({'c': 6, 'a': 5, 'b': 3})
print(my_counter.items())  # dict_items([('a', 5), ('b', 3), ('c', 6)])
print(my_counter.keys())  # dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # dict_keys(['a', 'b', 'c'])
print(my_counter.most_common(1))  # [('c', 6)]
print(my_counter.most_common(2))  # [('c', 6), ('a', 5)]
print(list(my_counter.elements()))

print(type(my_counter))  # <class 'collections.Counter'>
print(type(my_counter.items()))  # <class 'dict_items'>
print(type(my_counter.keys()))  # <class 'dict_keys'>
print(type(my_counter.values()))  # <class 'dict_values'>
print(type(my_counter.most_common(1)))  # <class 'list'>

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt.x, pt.y)

ordered_dict = OrderedDict()  # not required for Python 3.7 and later

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)
print(ordered_dict['c'])

normal_dict = {}

normal_dict['a'] = 1
normal_dict['b'] = 2
normal_dict['c'] = 3
normal_dict['d'] = 4

print(normal_dict)
# print(normal_dict['e']) # KeyError: 'e'

d = defaultdict(int)

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)
print(d['b'])
print(d['d'])

deque_test = deque()

deque_test.append(1)
deque_test.append(2)

print(deque_test)

deque_test.appendleft(3)
# deque_test.appendright(3) # it does not exist as the default one adds to the right

print(deque_test)  # deque([3, 1, 2])

deque_test.pop()
print(deque_test)  # deque([3, 1])

deque_test.popleft()
print(deque_test)  # deque([1])

deque_test.clear()
print(deque_test)  # deque([])

deque_test.extend([4, 5, 6])
print(deque_test)  # deque([4, 5, 6])

deque_test.extendleft([7, 8, 9])
print(deque_test)  # deque([9, 8, 7, 4, 5, 6]) # note the order it's added. one by one

deque_test2 = deque([1,2,3,4,5])
print(deque_test2)

deque_test2.rotate(2)
print(deque_test2) # deque([4, 5, 1, 2, 3]) # moves 2 places to right

deque_test2.rotate(-2)
print(deque_test2) # deque([1, 2, 3, 4, 5]) # moves 2 places to left
