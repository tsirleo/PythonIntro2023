class Lock:
    def locked(cls):
        cls.locked_sem, cls.semaphors = None, {}

        def delete(self):
            if self.locked_sem in self.semaphors and self.semaphors[self.locked_sem] == self.hash:
                self.semaphors[self.locked_sem] = None

        @property
        def lock(self):
            if self.locked_sem not in self.semaphors:
                return None
            elif self.semaphors[self.locked_sem] is None or self.semaphors[self.locked_sem] == self.hash:
                self.semaphors[self.locked_sem] = self.hash
                return self.locked_sem

        @lock.setter
        def lock(self, name):
            self.locked_sem, self.hash = name, hash(self)
            if self.hash in self.semaphors.values():
                (lambda h, s: s.__setitem__(next(key for key, value in s.items() if value == h), None))(self.hash, self.semaphors)
            if name not in self.semaphors:
                self.semaphors[name] = None

        @lock.deleter
        def lock(self):
            if self.locked_sem in self.semaphors and self.semaphors[self.locked_sem] == self.hash:
                self.semaphors[self.locked_sem] = None

        cls.lock, cls.__del__ = lock, delete

        return cls


# @Lock.locked
# class A(str):
#     pass
#
#
# a, b = A("a"), A("b")
# a.lock = "S"       # Регистрация на семафор S
# b.lock = "S"       # Регистрация на семафор S
# print(a, a.lock)   # Успешный захват семафора S
# print(a, a.lock)   # Семафор S уже захвачен нами
# print(b, b.lock)   # Неуспешный захват семафора S
# del a.lock         # Освобождение семафора S
# print(b, b.lock)   # Успешный захват семафора S
# b.lock = "T"       # Регистрация на семафор T, освобождает предыдущий семафор
# print(b, b.lock)   # Успешный захват семафора T
# del b              # Удаление объекта-носителя освобождает семафор
# a.lock = "T"       # Регистрация на семафор T, освобождает предыдущий семафор
# print(a, a.lock)   # Успешный захват семафора T
