"""
this is useless, since buffering is implemented in the under layer

class BufferedFileIterator(object):
    def __init__(self, fname: str, skip: int):
        self.fd = open(fname)
        self.skip = skip
        self.offset = 0
        self.bufsiz = 1024
        self.buflen = 0
        self.buf = ''

    def __iter__(self):
        self.fd.seek(self.skip, 0)
        return self

    def __next__(self):
        if self.offset == self.buflen:
            self.buf = self.fd.read(self.bufsiz)
            self.buflen = len(self.buf)
            self.offset = 0
            if self.buf == '':
                self.fd.close()
                raise StopIteration

        res = self.buf[self.offset]
        self.offset += 1

        return res
"""


class FileIterator(object):
    def __init__(self, fname: str, skip: int):
        self.fd = open(fname)
        self.skip = skip

    def __iter__(self):
        self.fd.seek(self.skip, 0)
        return self

    def __next__(self):
        c = self.fd.read(1)
        if c == '':
            self.fd.close()
            raise StopIteration

        return c


def stop_after_n_distinct(fname: str, n: int) -> int:
    streams = [FileIterator(fname, i) for i in range(n)]
    window = zip(*streams)
    i = 0

    for candidate in window:
        if len(set(candidate)) == n:
            return i + n
        i += 1
