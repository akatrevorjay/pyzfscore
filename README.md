Python libzfs/libzpool/libnvpair CFFI bindings.

Works great, but code is in need of a cleanup.

There are some functions missing, but this allows you to do most simple tasks (property management, dataset creation, snapshot management, traversing, etc) very easily, and *without* any damn command output parsing.

Check out zfs.py for the API ;)
