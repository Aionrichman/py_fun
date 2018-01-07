import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回。
        如果实例为空，抛出`LookupError`"""

    def loaded(self):
        """如果至少一个元素，返回`True`"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个由当前元素组成的有序元祖"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
