

class FlatIterator:

    def __init__(self, nested_list):
        self.i1 = 0
        self.i2 = -1
        self.list = nested_list

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.list[self.i1]) > 1:
            self.i2 += 1
            if self.i2 == len(self.list[self.i1]):
                self.i1 += 1
                self.i2 = 0
                pass
            if self.i1 == len(self.list):
                raise StopIteration
            return self.list[self.i1][self.i2]

def flat_generator(nested_list):
    i1 = 0
    i2 = -1
    while True:
        if len(nested_list[i1]) > 1:
            i2 += 1
            if i2 == len(nested_list[i1]):
                i1 += 1
                i2 = 0
            if i1 == len(nested_list):
                break
            yield nested_list[i1][i2]



