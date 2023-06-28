# class ManagedFile:
#     def __init__(self, filename):
#         print('init', filename)
#         self.filename = filename
#
#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename, 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if self.file:
#             self.file.close()
#         print('exc:', exc_type, exc_value)
#         print('exit')
#
# # No exception
# with ManagedFile('notes.txt') as f:
#     print('doing stuff...')
#     f.write('some todo...')
# print('continuing...')
#
# print()
#
# # Exception is raised, but the file can still be closed
# with ManagedFile('notes2.txt') as f:
#     print('doing stuff...')
#     f.write('some todo...')
#     # f.do_something()
# print('continuing...')



"""
Instead of writing a class, we can also write a generator function and decorate it with the contextlib.contextmanager decorator.
"""

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo...')