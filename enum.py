
from ctypes import *


class EnumerationType(type(c_uint)):
    def __new__(metacls, name, bases, dictionary):
        if not "_members_" in dictionary:
            _members_ = {}
            for key, value in dictionary.iteritems():
                if not key.startswith("_"):
                    _members_[key] = value
            dictionary["_members_"] = _members_

        elif isinstance(dictionary['_members_'], list):
            start = dictionary.get('_members_start_', 0)
            dictionary['_members_'] = dict([
                (m, start + x) for x, m in enumerate(dictionary['_members_'])
            ])
            #print dictionary['_members_']

        cls = type(c_uint).__new__(metacls, name, bases, dictionary)
        for key, value in cls._members_.iteritems():
            #globals()[key] = value
            setattr(cls, key, value)

        return cls

    def __contains__(self, value):
        return value in self._members_.values()

    def __repr__(self):
        return "<Enumeration %s>" % self.__name__


class Enumeration(c_uint):
    __metaclass__ = EnumerationType
    _members_ = {}

    def __init__(self, value):
        #super(Enumeration, self).__init__(self, value)
        c_uint.__init__(self, value)

        if value in self._members_.values():
            for k, v in self._members_.iteritems():
                if v == value:
                    self.name = k
                    break
        else:
            raise ValueError("No enumeration member with value %r" % value)

    @classmethod
    def from_param(cls, param):
        if isinstance(param, Enumeration):
            if param.__class__ != cls:
                raise ValueError("Cannot mix enumeration members")
            else:
                return param
        else:
            return cls(param)

    def __repr__(self):
        return "<member %s=%d of %r>" % (
            getattr(self, 'name', None),
            getattr(self, 'value', None),
            self.__class__,
        )
