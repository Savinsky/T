# -*- coding: utf-8 -*-
class Point2D():
    def __init__(self, x, y):
        self.coord = [x, y]

    def __str__(self):
        return "Координаты точeк: {}".format(self.coord)

    def __repr__(self):
        return "{}: {}".format(self.__class__, self.coord)

    def __abs__(self):
        return list(map(abs, self.coord))

    def __neg__(self):
        return self.coord[1]

    def __len__(self):
        return len(self.coord)

    def __call__(self, message):
        print(self.coord)
        return True

    def __del__(self):
        del self.coord

    def __getitem__(self, key):
        return self.coord[key]

    def __setitem__(self, key, value):
        self.coord[key] = value

    def __eq__(self, other):
        return (self.coord[0] == other.coord[0])&(self.coord[1] == other.coord[1])


if __name__ == '__main__':
    point1 = Point2D(1, 1)
    point2 = Point2D(1, 2)

    print(point1 == point2)
    print(point1 < point2)
    print(abs(point1))
    print(-- point1)
    print(len(point1))
    print point1, point2
    point1[0] = 4
    point2[1] = 4
    print point1, point2

    del point1, point2
