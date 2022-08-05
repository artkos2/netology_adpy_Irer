from Iterator import FlatIterator, flat_generator

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
	    print(item)
if __name__ == '__main__':
    print([item for item in FlatIterator(nested_list)])
if __name__ == '__main__':
    for item in  flat_generator(nested_list):
	    print(item)

