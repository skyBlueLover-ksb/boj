a = [1, 2, 3]
len(a)
a[1:2]
a.count(1)
a.index(1)
a.append(4)
a.pop()
a.pop(0)
try:
    del a[0]
except IndexError:
    print('nn')
a.remove(0)
a.sort()
min(a)
max(a)
a.reverse()

b = {k1: v1}
len(b)
b[k1]
b[k1] = v1_new
print(k1 in a)
try:
    print(a['false_key'])
except KeyError:
    print('nn')
c = collections.defaultdict(int)
d = collections.Counter(a)
d.most_common(2)
e = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1})
