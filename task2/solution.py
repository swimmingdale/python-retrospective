from collections import defaultdict
from collections import OrderedDict


def groupby(func, seq):
    dic = defaultdict(list)
    for x in seq:
        dic[func(x)].append(x)
    return dict(dic)


def compose(func1,func2):
    return lambda x: func1(func2(x))


def iterate(func):
    result = lambda x: x
    while True:
        yield result
        result = compose(func, result)


def zip_with(func, *iterables):
    for x in (zip(*iterables)):
        yield func(*x)
        


def cache(func, cache_size):
    cache = OrderedDict()
    if cache_size <= 0:
        return func
    
    def func_cached(*args):
        if args in cache:
              return cache[args]
        if cache_size:
            if len(cache) >= cache_size:
                cache.popitem(False)
            cache[args] = func(*args)
        return cache[args]
        
    return func_cached
        
        

