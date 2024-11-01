array = [10,6,90,2,40,8,40,6,75,3,7,49]
s = set([v for v in array if array.count(v) > 1])
print(*(s if len(s) > 0 else ['отсутствуют']))