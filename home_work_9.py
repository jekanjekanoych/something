from dataclasses import dataclass


@dataclass
class Date:
    year: int
    month: int
    day: int


@dataclass
class DateRange:
    beginning_date: Date
    ending_date: Date


def get_ranges_wo_insurance(insurance_periods: list[DateRange]) -> list[DateRange]:
    for date in insurance_periods:
        list_1 = []
        list_2 = []
        list_1.append(date.ending_date.month)
        list_2.append(date.beginning_date.month)
        list_1.append(date.ending_date.day)
        list_2.append(date.beginning_date.day)
        if list_1 > list_2:
            print(list_1)
            print(list_2)
        return []


if __name__ == '__main__':
    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 6, 25)),
        DateRange(Date(2020, 7, 1), Date(2020, 8, 31)),
        DateRange(Date(2020, 6, 29), Date(2020, 7, 31)),
        DateRange(Date(2020, 10, 1), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == [
        DateRange(Date(2020, 6, 25), Date(2020, 6, 29)),
        DateRange(Date(2020, 8, 31), Date(2020, 10, 1)),
    ]
    #
    # assert get_ranges_wo_insurance([]) == []
    #
    # _insurances = [
    #     DateRange(Date(2020, 1, 1), Date(2020, 7, 15)),
    #     DateRange(Date(2020, 7, 1), Date(2020, 12, 31)),
    # ]
    # assert get_ranges_wo_insurance(_insurances) == []