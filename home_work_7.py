import json                               # first_class


class JsonParser:
    def __init__(self, res):
        self.res = res
        self.file = None
        # a = json.loads(self.res)



    def __enter__(self):
        self.file = self.res

        res = json.loads(self.res)
        return res

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return self



    # def res(a):
    #     r = json.load(a)
    #     print(r)
    #     return res




if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}


class Point:                                    # second_class
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point


class Rectangle(Point):
    # def __init__(self, start_point, end_point):
    #     self.start_point = start_point
    #     self.end_point = end_point

    def contains(self, start_point):
        if self.start_point(start_point) <= start_point(start_point) or self.end_point(start_point) >= start_point(start_point):
            return start_point
        elif self.start_point(start_point) < Point.start_point or self.end_point(start_point) > Point.start_point:
            return
        else:
            return


if __name__ == '__main__':
    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
