import pandas as pd
import numpy as np
from netaddr_ext import NetwArray

def f():
    nets = NetwArray(['16.0.0.0/8', '192.168.0.0/24'])
    # nets = NetwArray(['192.168.11.0/14', '192.168.0.0/29'])
    df = pd.DataFrame({
        'A':['a','b'],
        'B':[1, 2],
        'net':nets
    })
    # import pdb; pdb.set_trace()
    print(df)
    print('========a')
    print(df['net'])
    print('========b')

    vals = df['net']
    print(f'VALS {type(vals)}\n{vals}')
    print('========c')
    print([v for v in vals])
    print('========d')
    # net = vals[0]
    # for addr in net.addresses():
    #     print(addr)

class Foo:
    """Demonstrate that values that are iterable are iterated over when printed.

    We don't want this to happen (because netaddr.IPNetwork is iterable).
    """

    def __init__(self, n):
        self.n = n

    def __next__(self):
        """See pandas.io.formats.printing.pprint_thing().

        If __next__ is defined, it just returns str(thing)."""

        pass

    def __len__(self):
        print('Foo __len__')
        # import pdb; pdb.set_trace()
        return 3

    def __getitem__(self, i):
        print(f'Foo __getitem__ {i}')
        # import pdb; pdb.set_trace()
        return (i+1)*self.n

    def __repr__(self):
        return f'Foo_repr({self.n})'

    def __str__(self):
        return f'Foo_str({self.n})'

def g():
    N = 2
    nets = np.empty([N], dtype=object)
    for i,f in enumerate([Foo(1), Foo(2)]):
        nets[i] = f
    print(nets)
    df = pd.DataFrame({
        'A':['a','b'],
        'B':[1, 2],
        'net':nets
    })
    print(df)

f()

