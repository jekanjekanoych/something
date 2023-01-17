import json                               # first_class


class JsonParser:
    def __init__(self, _res):
        self.res = _res
        self.file = None
        # a = json.loads(self.res)

    def __enter__(self):
        self.file = self.res

        _res = json.loads(self.res)
        return _res

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return self


if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}


class Point:                                    # second_class
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor


class Rectangle:
    def __init__(self, _start_point, _end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __ge__(self, other):
        assert isinstance(other, Rectangle)
        return self.start_point >= other.start_point

    def __eq__(self, other):
        assert isinstance(other, Rectangle)
        return self.start_point == other.start_point

    def contains(self, point):

        if self.start_point.x_coor <= point.x_coor <= self.end_point.x_coor:
            if self.start_point.y_coor \
                    <= point.y_coor <= self.end_point.y_coor:
                return True

        return False


if __name__ == '__main__':
    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
