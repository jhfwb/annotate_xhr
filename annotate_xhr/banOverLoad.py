import inspect
from types import FunctionType

from pyPacking_xhr import PackingTool
from annotate_xhr import singleObj, threadingRun
from annotate_xhr.err import OverloadException
class banOverLoad(type):
    """
    该类禁止方法被覆写。
    """
    def __init__(cls, cls_name, cls_bases, cls_dict):
        if len(cls_bases)!=0:
            arr=[]
            for cls_base in cls_bases:
                for item in dir(cls_base):
                    if hasattr(getattr(cls_base, item), '-banOverLoad'):  # 当其属性对象中有-ffs属性的时
                       arr.append(item)
            for cl in dir(cls):
                if cl in arr:
                    func=getattr(cls,cl)
                    if not hasattr(func,'-banOverLoad'):
                        raise OverloadException('在类中{}。该方法{}禁止覆写'.format(cls,func))
        super().__init__(cls_name, cls_bases, cls_dict)
    def func(func):
        """
        该类禁止方法被覆写
        usage:
        >>>
        >>>class haha(metaclass=banOverLoad): #继承一个元类
        >>>     @banOverLoad.func
        >>>     def xixi(self):pass

        如此一来，当子类对象使用xixi的时候就会报错
         """
        setattr(func,'-banOverLoad',True)
        return func


if __name__ == '__main__':
    class haha(metaclass=banOverLoad):
        def didi(self):
            print('didi')
        @banOverLoad.func
        def xixi(self):
            print('方法运行')
        @banOverLoad.func
        def haha(self):
            print('方法运行')
    class xixi(haha):
        def haha(self):
            print('方法运行12')
    xixi().xixi()

