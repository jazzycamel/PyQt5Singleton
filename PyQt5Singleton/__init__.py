try: from PyQt5.QtCore import pyqtWrapperType
except ImportError:
    from sip import wrappertype as pyqtWrapperType

class Singleton(pyqtWrapperType, type):
    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        cls.instance=None

    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance=super().__call__(*args, **kw)
        return cls.instance

if __name__=="__main__":
    from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty

    class MyObject(QObject, metaclass=Singleton):
        def __init__(self, parent=None, **kwargs):
            super().__init__(parent, **kwargs)

            self._x=0

        def x(self): return self._x

        @pyqtSlot(int)
        def setX(self, x): self._x=x

        x=pyqtProperty(int, x, setX)

    print(MyObject().x)
    MyObject().x=1
    print(MyObject().x)
