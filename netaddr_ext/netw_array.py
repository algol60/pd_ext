import pandas as pd
from pandas.core.arrays import ExtensionArray
from pandas._typing import ArrayLike, Dtype, Ordered, Scalar
from pandas.core.algorithms import take

import numpy as np
import sys

from netaddr import IPNetwork as IPNetwork_
from . import NetwType

class IPNetwork(IPNetwork_):
    def __init__(self, addr, implicit_prefix=False, version=None, flags=0):
        super().__init__(addr, implicit_prefix, version, flags)

    __init__.__doc__ = IPNetwork_.__init__.__doc__

    # def __iter__(self):
    #     raise TypeError("'IPNetwork' object is not iterable")

    def addresses(self):
        return super().__iter__()

    def __repr__(self):
        # return f"Fake_repr-{self.__class__.__name__}('{super().__repr__()}')"
        return super().__repr__()

    def __str__(self):
        # return f"Fake_str-{self.__class__.__name__}('{super().__str__()}')"
        return super().__str__()
    __len__ = None
    __iter__ = None

NULL_NET = IPNetwork('0.0.0.0')

def _value(addr):
    if isinstance(addr, IPNetwork):
        return addr
    elif addr is None or addr=='':
        return NULL_NET

    return IPNetwork(addr)

class NetwArray(ExtensionArray):
    """netaddr.IPNetwork ExtensionArray.

    See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray.
    """

    dtype = NetwType()

    def __repr__(self):
        return '**plugh**'

    def __init__(self, addrs):
        """Accept a list of IP networks."""
        # print(f'@@ AA init {addrs}')

        # print('^^', addrs)
        # print('%%1', [_value(i) for i in addrs])
        # print('%%1a')
        # zz = np.array([_value(i) for i in addrs], dtype=NetwType)
        # print('%%1b')
        # print('%%2', np.array([_value(i) for i in addrs]))

        # IPNetwork instances are iterable.
        # If we just feed them to np.array, they will be iterated over
        # and the array will contain all of the addresses in the nework,
        # which is definitely bad, especially for large networks.
        # Therefore we have to muck around.
        # Stackoverflow says '''arr.empty(); arr[:] = [values]''',
        # but that hangs as well.
        #
        arr = np.empty([len(addrs)], dtype=object)
        for i, addr in enumerate(addrs):
            arr[i] = IPNetwork(addr)

        self.data = arr
        # self.data = np.array([_value(i) for i in addrs])
        # print(f'@@ INIT shape {self.data.ndim} {self.data.shape}')
        # self.data = np.array(self.data])
        # print('&&', self.data)
        if self.data.ndim!=1:
            raise AttributeError('Only one dimension')

        # print('ZZ')

        # lonlats = [tuple(row) for row in lonlats]
        # self.data = np.array(lonlats, dtype=geo_dtype.GeoType._record_type)
        # # print('@@', type(self.data), self.dtype, self.data.ndim, self.data)
        # # print('@@SHAPE', type(self.data.shape), self.data.shape, self.data.shape[0])
        # if self.data.ndim!=1:
        #     raise AttributeError('Only one dimension')
        # # if self.data.shape[0]!=2:
        # #     raise AttributeError('Only longitude/latitude pairs')

    # Begin: must implement.
    #

    @classmethod
    def _from_sequence(cls, scalars, dtype=None, copy=False):
        print(f'@@ _from_sequence {cls} {scalars} {dtype} {copy}')
        return np.array([_value(i) for i in scalars])

    @classmethod
    def _from_factorized(cls, uniques, original):
        print(f'@@ _from_factorized {cls} {uniques} {original}')
        pass

    def __getitem__(self, key):
        # print(f'@@ getitem {key}')
        # """
        # Return an item.
        # """
        # if isinstance(key, (int, np.integer)):
        #     i = self._codes[key]
        #     if i == -1:
        #         return np.nan
        #     else:
        #         return self.categories[i]

        # key = check_array_indexer(self, key)

        # result = self._codes[key]
        # if result.ndim > 1:
        #     deprecate_ndim_indexing(result)
        #     return result
        # return self._constructor(result, dtype=self.dtype, fastpath=True)
        ip = self.data[key]

        return ip

    def __len__(self) -> int:
        """
        The length of this array.
        """
        return len(self.data)

    # @property
    # def dtype(self) -> netaddr.IPAddress:
    #     """
    #     The :class:`~pandas.api.types.CategoricalDtype` for this instance.
    #     """
    #     return self._dtype

    @property
    def nbytes(self):
        return sum(sys.getsizeof(i) for i in self.data)

    def isna(self):
        """
        Detect missing values

        Missing values (-1 in .codes) are detected.

        Returns
        -------
        a boolean array of whether my values are null

        See Also
        --------
        isna : Top-level isna.
        isnull : Alias of isna.
        Categorical.notna : Boolean inverse of Categorical.isna.

        """

        na = self.data==NULL_NET

        return na

    def take(self, indexer, allow_fill:bool=False, fill_value=None):
        """Take elements from the array.

        ExtensionArray.take is called by Series.__getitem__, .loc, iloc, when indices is a
        sequence of values. Additionally, it's called by Series.reindex(), or any other method
        that causes realignment, with a fill_value.

        Parameters
        ----------
        indexer : sequence of int
            The indices in `self` to take. The meaning of negative values in
            `indexer` depends on the value of `allow_fill`.
        allow_fill : bool, default False
            How to handle negative values in `indexer`.

            * False: negative values in `indices` indicate positional indices
              from the right. This is similar to
              :func:`numpy.take`.

            * True: negative values in `indices` indicate missing values
              (the default). These values are set to `fill_value`. Any other
              other negative values raise a ``ValueError``.

            .. versionchanged:: 1.0.0

               Default value changed from ``True`` to ``False``.

        fill_value : object
            The value to use for `indices` that are missing (-1), when
            ``allow_fill=True``. This should be the category, i.e. a value
            in ``self.categories``, not a code.

        Returns
        -------
        Categorical
            This Categorical will have the same categories and ordered as
            `self`.

        See Also
        --------
        Series.take : Similar method for Series.
        numpy.ndarray.take : Similar method for NumPy arrays.

        Examples
        --------
        >>> cat = pd.Categorical(['a', 'a', 'b'])
        >>> cat
        [a, a, b]
        Categories (2, object): [a, b]

        Specify ``allow_fill==False`` to have negative indices mean indexing
        from the right.

        >>> cat.take([0, -1, -2], allow_fill=False)
        [a, b, a]
        Categories (2, object): [a, b]

        With ``allow_fill=True``, indices equal to ``-1`` mean "missing"
        values that should be filled with the `fill_value`, which is
        ``np.nan`` by default.

        >>> cat.take([0, -1, -1], allow_fill=True)
        [a, NaN, NaN]
        Categories (2, object): [a, b]

        The fill value can be specified.

        >>> cat.take([0, -1, -1], allow_fill=True, fill_value='a')
        [a, a, a]
        Categories (3, object): [a, b]

        Specifying a fill value that's not in ``self.categories``
        will raise a ``TypeError``.
        """
        # print(f'@@take {indexer}, {allow_fill}, {fill_value}')
        indexer = np.asarray(indexer, dtype=np.intp)

        # dtype = self.dtype

        if pd.isna(fill_value):
            fill_value = NULL_NET
        # elif allow_fill:
        #     # convert user-provided `fill_value` to codes
        #     if fill_value in self.categories:
        #         fill_value = self.categories.get_loc(fill_value)
        #     else:
        #         msg = (
        #             f"'fill_value' ('{fill_value}') is not in this "
        #             "Categorical's categories."
        #         )
        #         raise TypeError(msg)

        items = take(self.data, indexer, allow_fill=allow_fill, fill_value=fill_value)
        return items

    def copy(self) -> "Categorical":
        """
        Copy constructor.
        """
        return self._constructor(
            values=self._codes.copy(), dtype=self.dtype, fastpath=True
        )

    @classmethod
    def _concat_same_type(self, to_concat):
        from pandas.core.dtypes.concat import concat_categorical

        return concat_categorical(to_concat)

    #
    # End: must implement.

    # def astype(self, dtype: Dtype, copy: bool = True) -> ArrayLike:
    #     print(f'@@ astype {dtype}, {copy}')
    #     return np.array(None if i is None else netaddr.IPAddress(i) for i in scalars)

    # def __repr__(self) -> str:
    #     """
    #     String representation.
    #     """
    #     print('__repr__')
    #     s = ' '.join('null' if i is NULL_NET else str(i) for i in self.data)
    #     return f'NetwArray({s})'

    #     # a = ', '.join(f'({lon},{lat})' for lon,lat in self.data)
    #     # return f'GeoArray({a})])'

    #     # _maxlen = 10
    #     # if len(self._codes) > _maxlen:
    #     #     result = self._tidy_repr(_maxlen)
    #     # elif len(self._codes) > 0:
    #     #     result = self._get_repr(length=len(self) > _maxlen)
    #     # else:
    #     #     msg = self._get_repr(length=False, footer=True).replace("\n", ", ")
    #     #     result = f"[], {msg}"

    #     # return result

    # def __str__(self) -> str:
    #     return 'xyzzy'

    # def _formatter(self, boxed=False):
    #     # Defer to CategoricalFormatter's formatter.
    #     print('**\n** _formatter', boxed)
    #     nets = '|'.join([str(net) for net in self.data])
    #     # print('@@', nets)
    #     # import pdb; pdb.set_trace()
    #     return lambda v: repr(v)

    # ------------------------------------------------------------------------
    # Ops
    # ------------------------------------------------------------------------

    def __eq__(self, other):
        # TDOO: scalar ipaddress
        if not isinstance(other, NetwArray):
            return NotImplemented
        mask = self.isna() | other.isna()
        result = self.data == other.data
        result[mask] = False
        return result
