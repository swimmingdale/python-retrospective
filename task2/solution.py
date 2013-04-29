from collections import defaultdict
dic = defaultdict(list)

def groupby(func, seq):
    for x in seq:
        if func(x) in dic:
            dic[func(x)].append(x)
        else:
            dic[func(x)].append(x)
    return dict(dic)
