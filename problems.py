Дано число N. За ним N значений, имя и оценка в семестре. Нужно вывести имена
учеников со вторым наименьшим результатом, если таких несколько вывести в алфавитном порядке.

кол-во учеников = N
кол-во записей  = M

оценки могут повторятся для ученов
оценки могут быть в диапозоне от 0 до 100 (0 <= mark <= 100)

{
    "И": 100,
    "М": 78,
    "Л": 78
    "С": 70,
    "д": 70,
}


min_1 = h[0]
min_2 = h[1]

min_1 = 7
min_2 = 4

# double check
if current > min_2 and current < min_1:
    min_1 = current
elif current < min_2 and current < min_1:
    min_1 = min_2
    min_2 = current

Time O(n), n - amount of records (students) 
Space O(1)

{
    "min_1",
    "min_2"
}


def foo(records: List[dict]) -> List[str]:
    slice = list(records)[:2]
    min_1 = max(slice)
    min_2 = min(slice)

    for key in enumerate(2, records):
        current = records[key]
        if current > min_2 and current < min_1:
            min_1 = current
        elif current < min_2 and current < min_1:
            min_1 = min_2
            min_2 = current
        
    for key, value in records:
        if value == min_2:
            return key




res = []
value = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    res.append([name, score])
    value.append(score)

res.sort()
result = sorted(list(set(value)))
for i in range(len(res)):
    if res[i][1] == result[1]:
        print(res[i][0])



find max
find 2 last max elements


find min
find 2 last min elements


max_1
max_2

current


def second_gratest_element(array) -> int:
    print(array)
    if bool(array) is False or len(array) == 1:
        return
    elif len(array) == 2:
        return max(array[0], array[1])
    else:
        first_max, second_max = max(array[0], array[1]), min(array[0], array[1])
        for idx in range(2, len(array)):
            # case value grater both
            # case value grater second max but less first max
            value = array[idx]
            if second_max < value < first_max:
                second_max = value
            elif second_max < value > first_max:
                second_max = first_max
                first_max = value
        return second_max