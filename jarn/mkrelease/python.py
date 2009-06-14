from process import WithProcess
from exit import err_exit


class WithPython(object):

    def __init__(self, python=None):
        if python is None:
            self.python = 'python2.6' # FIXME
        else:
            self.python = python


class Python(WithProcess, WithPython):
    """A Python interpreter path that can test itself."""

    def __init__(self, defaults, process=None):
        WithProcess.__init__(self, process)
        WithPython.__init__(self, defaults.python)

    def __str__(self):
        return self.python

    def is_valid_python(self, python=None):
        version = self.get_python_version(python)
        if version and version >= '2.6':
            return True
        return False

    def check_valid_python(self, python=None):
        version = self.get_python_version(python)
        if not version:
            err_exit('Bad interpreter')
        if version < '2.6':
            err_exit('Python >= 2.6 required')

    def get_python_version(self, python=None):
        if python is None:
            python = self.python
        version = self.process.pipe(
            '"%(python)s" -c"import sys; print sys.version[:3]"' % locals())
        return version
