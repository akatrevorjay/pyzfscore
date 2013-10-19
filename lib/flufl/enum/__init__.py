# Copyright (C) 2004-2013 by Barry A. Warsaw
#
# This file is part of flufl.enum
#
# flufl.enum is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# flufl.enum is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with flufl.enum.  If not, see <http://www.gnu.org/licenses/>.

"""Package init."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'Enum',
    'IntEnum',
    'BitMaskEnum',
    '__version__',
    'make',
    ]


__version__ = '4.0'

from ._enum import Enum, IntEnum, BitMaskEnum, make
