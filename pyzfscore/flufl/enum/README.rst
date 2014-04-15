=========================================
flufl.enum - A Python enumeration package
=========================================

*This package has been modified to support start=X on IntEnum ~trevorj*

This package is called ``flufl.enum``, a Python enumeration package.

The goals of ``flufl.enum`` are to produce simple, specific, concise semantics
in an easy to read and write syntax.  ``flufl.enum`` has just enough of the
features needed to make enumerations useful, but without a lot of extra
baggage to weigh them down.  This work grew out of the Mailman 3.0 project and
it is the enum package used there.  This package was previously called
``munepy``.

``flufl.enum`` is an implementation of the standard library enumeration
package described in `PEP 435`_ for `Python 3.4`_.  It is available as a
separate package for use in older Python versions.


Requirements
============

``flufl.enum`` requires Python 2.7 or newer, and is compatible with Python 3.2
and later.


Documentation
=============

A `simple guide`_ to using the library is available within this package.  The
manual is also available online at:

    http://package.python.org/flufl.enum


Project details
===============

The project home page is:

    http://launchpad.net/flufl.enum

You should report bugs at:

    http://bugs.launchpad.net/flufl.enum

You can download the latest version of the package either from the Cheeseshop:

    http://pypi.python.org/pypi/flufl.enum

or from the Launchpad page above.  Of course you can also just install it with
``pip`` or ``easy_install`` from the command line::

    % sudo pip install flufl.enum
    % sudo easy_install flufl.enum

You may want to use `virtualenv`_ instead of installing the package into the
system Python.

You can grab the latest development copy of the code using Bazaar, from the
Launchpad home page above.  See http://bazaar-vcs.org for details on the
Bazaar distributed revision control system.  If you have Bazaar installed, you
can grab your own branch of the code like this::

     bzr branch lp:flufl.enum

You may contact the author via barry@python.org.


Copyright
=========

Copyright (C) 2004-2013 Barry A. Warsaw

This file is part of flufl.enum.

flufl.enum is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

flufl.enum is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License along
with flufl.enum.  If not, see <http://www.gnu.org/licenses/>.


Table of Contents
=================

.. toctree::

    docs/using.rst
    NEWS.rst

.. _`simple guide`: docs/using.html
.. _`virtualenv`: http://www.virtualenv.org/en/latest/index.html
.. _`PEP 435`: http://www.python.org/dev/peps/pep-0435/
.. _`Python 3.4`: http://www.python.org/dev/peps/pep-0429/
