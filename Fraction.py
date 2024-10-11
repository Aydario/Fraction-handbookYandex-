from typing import Union

class Fraction:
    """
    Класс для представления дробей.

    :param num: Числитель или строка, представляющая дробь (например, "3/4").
    :param denom: Знаменатель (по умолчанию None). Если не указан, предполагается, что это целое число.
    """

    def __init__(self, num: Union[int, str], denom: int = None):
        if isinstance(num, str):
            if '/' in num:
                self.numer, self.denomin = map(int, num.split('/'))
            else:
                self.numer, self.denomin = int(num), 1
        else:
            if denom:
                self.numer, self.denomin = num, denom
            else:
                self.numer, self.denomin = num, 1
        self._identify_sign()
        self._shorten()
    
    def _shorten(self):
        """
        Сокращает дробь до наименьших членов.
        """
        if self.numer == 0:
            self.denomin = 1
        else:
            gcd = self._gcd(self.numer, self.denomin)
            self.numer //= gcd
            self.denomin //= gcd
                    
    def _gcd(self, a: int, b: int) -> int:
        """
        Вычисляет наибольший общий делитель (НОД) двух чисел.

        :param a: Первое число.
        :param b: Второе число.
        :return: НОД чисел a и b.
        """
        while b:
            a, b = b, a % b
        return a

    def _identify_sign(self):
        """
        Определяет знак дроби и нормализует его.
        """
        if self.numer < 0 and self.denomin < 0:
            self.numer, self.denomin = -self.numer, -self.denomin
        elif self.denomin < 0:
            self.numer, self.denomin = -self.numer, -self.denomin

    def __add__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Складывает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: Результат сложения.
        """
        if isinstance(other, Fraction):
            return Fraction((self.numer * other.denomin) + (other.numer * self.denomin), self.denomin * other.denomin)
        return Fraction(self.numer + (other * self.denomin), self.denomin)

    def __iadd__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Складывает текущую дробь с другой дробью или целым числом и сохраняет результат в текущей дроби.

        :param other: Другая дробь или целое число.
        :return: Текущая дробь с обновленными значениями.
        """
        if isinstance(other, Fraction):
            self.numer = (self.numer * other.denomin) + (other.numer * self.denomin)
            self.denomin = self.denomin * other.denomin
            self._shorten()
            return self
        self.numer = self.numer + (other * self.denomin)
        self._shorten()
        return self

    def __radd__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Складывает текущую дробь с другой дробью или целым числом справа.

        :param other: Другая дробь или целое число.
        :return: Результат сложения.
        """
        if isinstance(other, Fraction):
            return Fraction((self.numer * other.denomin) + (other.numer * self.denomin), self.denomin * other.denomin)
        return Fraction(self.numer + (other * self.denomin), self.denomin)

    def __sub__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Вычитает другую дробь или целое число из текущей дроби.

        :param other: Другая дробь или целое число.
        :return: Результат вычитания.
        """
        if isinstance(other, Fraction):
            return Fraction((self.numer * other.denomin) - (other.numer * self.denomin), self.denomin * other.denomin) 
        return Fraction(self.numer - (other * self.denomin), self.denomin)

    def __isub__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Вычитает другую дробь или целое число из текущей дроби и сохраняет результат в текущей дроби.

        :param other: Другая дробь или целое число.
        :return: Текущая дробь с обновленными значениями.
        """
        if isinstance(other, Fraction):
            self.numer = (self.numer * other.denomin) - (other.numer * self.denomin)
            self.denomin = self.denomin * other.denomin
            self._shorten()
            return self
        self.numer = self.numer - (other * self.denomin)
        self._shorten()
        return self

    def __rsub__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Вычитает текущую дробь из другой дроби или целого числа справа.

        :param other: Другая дробь или целое число.
        :return: Результат вычитания.
        """
        if isinstance(other, Fraction):
            return Fraction((other.numer * self.denomin) - (self.numer * other.denomin), self.denomin * other.denomin)
        return Fraction((other * self.denomin) - self.numer, self.denomin)

    def __mul__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Умножает текущую дробь на другую дробь или целое число.

        :param other: Другая дробь или целое число.
        :return: Результат умножения.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numer * other.numer, self.denomin * other.denomin)
        return Fraction(self.numer * other, self.denomin)

    def __imul__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Умножает текущую дробь на другую дробь или целое число и сохраняет результат в текущей дроби.

        :param other: Другая дробь или целое число.
        :return: Текущая дробь с обновленными значениями.
        """
        if isinstance(other, Fraction):
            self.numer = self.numer * other.numer
            self.denomin = self.denomin * other.denomin
            self._shorten()
            return self
        self.numer = self.numer * other
        self._shorten()
        return self

    def __rmul__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Умножает текущую дробь на другую дробь или целое число справа.

        :param other: Другая дробь или целое число.
        :return: Результат умножения.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numer * other.numer, self.denomin * other.denomin)
        return Fraction(self.numer * other, self.denomin)

    def __truediv__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Делит текущую дробь на другую дробь или целое число.

        :param other: Другая дробь или целое число.
        :return: Результат деления.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numer * other.denomin, self.denomin * other.numer)
        return Fraction(self.numer, self.denomin * other)

    def __itruediv__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Делит текущую дробь на другую дробь или целое число и сохраняет результат в текущей дроби.

        :param other: Другая дробь или целое число.
        :return: Текущая дробь с обновленными значениями.
        """
        if isinstance(other, Fraction):
            self.numer = self.numer * other.denomin
            self.denomin = self.denomin * other.numer
            self._shorten()
            return self
        self.denomin = self.denomin * other
        self._shorten()
        return self

    def __rtruediv__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Делит другую дробь или целое число на текущую дробь справа.

        :param other: Другая дробь или целое число.
        :return: Результат деления.
        """
        if isinstance(other, Fraction):
            return Fraction(other.numer * self.denomin, other.denomin * self.numer)
        return Fraction(self.denomin * other, self.numer)

    def __neg__(self) -> 'Fraction':
        """
        Возвращает дробь с противоположным знаком.

        :return: Дробь с противоположным знаком.
        """
        return Fraction(-self.numer, self.denomin)

    def __lt__(self, other: Union['Fraction', int]) -> bool:
        """
        Сравнивает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: True, если текущая дробь меньше, иначе False.
        """
        if isinstance(other, Fraction):
            return self.numer * other.denomin < other.numer * self.denomin
        return self.numer < other * self.denomin

    def __le__(self, other: Union['Fraction', int]) -> bool:
        """
        Сравнивает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: True, если текущая дробь меньше или равна, иначе False.
        """
        if isinstance(other, Fraction):
            return self.numer * other.denomin <= other.numer * self.denomin
        return self.numer <= other * self.denomin

    def __eq__(self, other: Union['Fraction', int]) -> bool:
        """
        Сравнивает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: True, если текущая дробь равна, иначе False.
        """
        if isinstance(other, Fraction):
            return self.numer * other.denomin == other.numer * self.denomin
        return self.numer == other * self.denomin

    def __ne__(self, other: Union['Fraction', int]) -> bool:
        """
        Сравнивает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: True, если текущая дробь не равна, иначе False.
        """
        if isinstance(other, Fraction):
            return self.numer * other.denomin != other.numer * self.denomin
        return self.numer != other * self.denomin

    def __gt__(self, other: Union['Fraction', int]) -> bool:
        """
        Сравнивает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: True, если текущая дробь больше, иначе False.
        """
        if isinstance(other, Fraction):
            return self.numer * other.denomin > other.numer * self.denomin
        return self.numer > other * self.denomin

    def __ge__(self, other: Union['Fraction', int]) -> bool:
        """
        Сравнивает текущую дробь с другой дробью или целым числом.

        :param other: Другая дробь или целое число.
        :return: True, если текущая дробь больше или равна, иначе False.
        """
        if isinstance(other, Fraction):
            return self.numer * other.denomin >= other.numer * self.denomin
        return self.numer >= other * self.denomin

    def reverse(self) -> 'Fraction':
        """
        Возвращает дробь, где числитель и знаменатель поменяны местами.

        :return: Дробь с поменянными местами числителем и знаменателем.
        """
        self.numer, self.denomin = self.denomin, self.numer
        self._identify_sign()
        self._shorten()
        return self

    def numerator(self, number: int = None) -> Union[int, None]:
        """
        Устанавливает или возвращает числитель дроби.

        :param number: Новое значение числителя (опционально).
        :return: Текущий числитель, если параметр не указан.
        """
        if number is not None:
            if self.numer < 0:
                self.numer = -1 * number
            else:
                self.numer = number
            self._identify_sign()
            self._shorten()
        else:
            return abs(self.numer)
        
    def denominator(self, number: int = None) -> Union[int, None]:
        """
        Устанавливает или возвращает знаменатель дроби.

        :param number: Новое значение знаменателя (опционально).
        :return: Текущий знаменатель, если параметр не указан.
        """
        if number is not None:
            self.denomin = number
            self._identify_sign()
            self._shorten()
        else:
            return abs(self.denomin)

    def __str__(self) -> str:
        """
        Возвращает строковое представление дроби.

        :return: Строковое представление дроби.
        """
        return f'{self.numer}/{self.denomin}'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление дроби, подходящее для воссоздания объекта.

        :return: Строковое представление дроби.
        """
        return f"Fraction('{self.numer}/{self.denomin}')"
