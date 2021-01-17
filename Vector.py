# vector.py
#
# ICS 33 Summer 2013
# Code Example
#
# This is a completed version of our Vector class from lecture.
import math


class Vector:
    length = None

    # Initializing a Vector will require a non-empty tuple, so that
    # the syntax for creating a Vector would look like this:
    #
    #    Vector((1, 2, 3))
    #
    # In a later lecture, we'll learn how to eliminate the tuple and
    # allow the __init__ method to take a variable number of arguments.
    #
    # We initialize the Vector by storing the tuple in an attribute of
    # the Vector so that we can use it later.
    def __init__(self, components):
        if type(components) != tuple or len(components) == 0:
            raise TypeError('components must be a non-empty tuple')

        self._components = components
        self.length = (math.sqrt((components[0] ** 2) + (components[1] ** 2)))

    # The canonical representation of a Vector looks like a call to our
    # Vector constructor.
    def __repr__(self):
        return 'Vector({})'.format(self._components)

    # The length of a Vector is the number of components it has (i.e.,
    # the number of dimensions it's represented in).  So, for example,
    # the length of Vector((5, 7)) would be 2.
    #
    # Writing this method allows us to say this:
    #
    #    len(Vector((1, 2, 3))
    #
    # and get back 3.
    def __len__(self):
        return len(self._components)

    def tuple(self):
        return self._components

    # Consistent with numeric classes in Python, we'll say that a Vector
    # is considered True if it is non-zero (i.e., at least one of its
    # components is something other than zero) and False if it's zero.
    #
    # This allows Vectors to be used as boolean values, the way that most
    # other types in Python can be used.
    def __bool__(self):
        for component in self._components:
            if component != 0:
                return True

        return False

    # Vectors are equal if they have the same components (i.e., the same
    # number of components and the same values in each corresponding
    # component).  So long as we're comparing a Vector to another Vector,
    # all we need to do is compare the _components tuples; tuples already
    # have an == comparison that does what we want.
    def __eq__(self, other):
        if type(other) != Vector:
            return False

        return self._components == other._components

    # Vectors are not equal if they have at least one component that's
    # different, or if they have a different number of components.
    def __ne__(self, other):
        if type(other) != Vector:
            return True

        return self._components != other._components

    # Note that there is no meaningful notion of a vector being "less than"
    # or "greater than" another vector, so we won't implement those operators
    # here.

    # Adding two Vectors is a matter of adding the corresponding components
    # in each one.  It only makes sense to add a Vector to another Vector,
    # and it only makes sense to add them together if they have the same
    # number of components.
    def __add__(self, other):
        if type(other) != Vector:
            raise ValueError('cannot add non-vectors to vectors')
        elif len(self._components) != len(other._components):
            raise ValueError('cannot add vectors of differing dimensions')

        # This loop (and others like it) will be written better later this
        # quarter when we learn a few more things about Python.
        new_components = []

        for i in range(len(self._components)):
            new_components.append(self._components[i] + other._components[i])

        return Vector(tuple(new_components))

    # Subtraction is a lot like addition
    def __sub__(self, other):
        if type(other) != Vector:
            raise ValueError('cannot subtract non-vectors to vectors')
        elif len(self._components) != len(other._components):
            raise ValueError('cannot subtract vectors of differing dimensions')

        new_components = []

        for i in range(len(self._components)):
            new_components.append(self._components[i] - other._components[i])

        return Vector(tuple(new_components))

    # There are three kinds of multiplication we want to support:
    #
    #    Vector((1, 2, 3)) * Vector((4, 5, 6))
    #    Vector((4, 5)) * 3
    #    3 * Vector((4, 5))
    #
    # For the first, we'll calculate a "dot product", which is the sum of
    # the products of corresponding elements (in the example above, it's
    # (1*4) + (2*5) + (3*6) = 32.
    #
    # For the second and third, we'll multiply the integer by each of the
    # components in the Vector, giving Vector((12, 15)) as the result.
    #
    # The first two kinds of multiplication will be implemented using the
    # special method __mul__, because the left-hand operand is a Vector.
    # The third will require __rmul__.

    def __mul__(self, other):
        if type(other) == Vector:
            if len(self._components) != len(other._components):
                raise ValueError('cannot multiply vectors of differing dimensions')

            dot_product = 0

            for i in range(len(self._components)):
                dot_product += self._components[i] * other._components[i]

            return dot_product

        # Note: There are better ways to check if the right-hand operand
        # is a number, but that's a topic for another day.
        elif type(other) in [int, float]:
            new_components = []

            for component in self._components:
                new_components.append(component * other)

            return Vector(tuple(new_components))

        else:
            raise TypeError('unsupported type in vector multiplication')

    def __rmul__(self, other):
        if type(other) in [int, float]:
            new_components = []

            for component in self._components:
                new_components.append(component * other)

            return Vector(tuple(new_components))
        else:
            raise TypeError('cannot multiply vectors by anything other than vectors or numbers')

    # Division is like multiplication, except that there is only one
    # case we need to support:
    #
    #      Vector((10, 20, 30)) / 2
    #
    # which yields:
    #
    #      Vector((5, 10, 15))
    #
    # There are two kinds of division in Python: "true division" and
    # "floor division".  True division is implemented by the "/" operator
    # in Python, while floor division is implemented by "//".  Since we
    # want true division here, we'll implement the special method
    # __truediv__.
    def __truediv__(self, other):
        if type(other) in [int, float]:
            new_components = []

            for component in self._components:
                new_components.append(component / other)

            return Vector(tuple(new_components))
        else:
            raise TypeError('cannot divide vectors by anything other than numbers')

    # The special method __neg__ implements negation, so we can do this:
    #
    #     -Vector((1, 2, 3))
    #
    # and get back this:
    #
    #     Vector((-1, -2, -3))
    def __neg__(self):
        new_components = []

        for component in self._components:
            new_components.append(-component)

        return Vector(tuple(new_components))

    # There is technically a unary + operator in Python, as well.
    #
    #     +Vector((1, 2, 3))
    #
    # would simply evaluate to:
    #
    #     Vector((1, 2, 3))
    #
    # But this operator needs to be implemented or it won't exist.  So
    # we'll implement it here.
    def __pos__(self):
        return self

    def norm(self):
        # print(self._components[0], self._components[1])

        return Vector((self._components[0], self._components[1])) * (1 / self.length)

    def get_length(self):
        return self.length

    def get_angle(self):

        return math.degrees(math.atan2(self._components[1], self._components[0]))
