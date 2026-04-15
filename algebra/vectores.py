"""
Tercera tarea de APA: Multiplicación de vectores y ortogonalidad
Alumno: Ricard Mula Cañameras

Tests unitarios:
    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> v1 * 2
    Vector([2, 4, 6])
    >>> 2 * v1
    Vector([2, 4, 6])
    >>> v1 * v2
    Vector([4, 10, 18])
    >>> v1 @ v2
    32
    >>> v3 = Vector([2, 1, 2])
    >>> v4 = Vector([0.5, 1, 0.5])
    >>> v3 // v4
    Vector([1.0, 2.0, 1.0])
    >>> v3 % v4
    Vector([1.0, -1.0, 1.0])
"""


class Vector:
    vector = []

    def __init__(self, numeros):
        self.vector = [numero for numero in numeros]

    def __repr__(self):
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        str_ = '[ '
        for componente in self.vector:
            str_ += ' ' + str(componente)
        str_ += ' ]'
        return str_

    def __iter__(self):
        return iter(self.vector)

    def __add__(self, other):
        """
        Suma elemento a elemento dos vectores.

        """
        return Vector(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        """
        Resta elemento a elemento dos vectores.
        """
        return Vector(a - b for a, b in zip(self, other))

    def __mul__(self, other):
        """
        Multiplica el vector por un escalar o calcula el producto de Hadamard.
        """
        if isinstance(other, (int, float)):
            return Vector(a * other for a in self)
        return Vector(a * b for a, b in zip(self, other))

    def __rmul__(self, other):
        """
        Multiplica un escalar por el vector (conmutativa).
        """
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Calcula el producto escalar (dot product) de dos vectores.
        """
        return sum(a * b for a, b in zip(self, other))

    def __floordiv__(self, other):
        """
        Calcula la componente de self paralela (tangencial) a other.
        """
        return (self @ other / (other @ other)) * other

    def __mod__(self, other):
        """
        Calcula la componente de self perpendicular (normal) a other.
        """
        return self - self // other


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)