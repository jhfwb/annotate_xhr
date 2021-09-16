import inspect
from types import FunctionType

from pyPacking_xhr import PackingTool
from annotate_xhr import singleObj, threadingRun
from annotate_xhr.err import OverloadException


class banOverLoad(type):
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
        # for item in dir(cls):  # 获得cls(class sonTest)的所有属性
        # for item in dir(cls):  # 获得cls(class sonTest)的所有属性
        #     if hasattr(getattr(cls, item), '-banOverLoad'):  # 当其属性对象中有-ffs属性的时
        #         if hasattr(cls,'_banOverLoad_funcs'):
        #             getattr(cls,'_banOverLoad_funcs').append(item)
        #         else:
        #             setattr(cls,'_banOverLoad_funcs',[item])
        # if len(cls_bases)!=0:
        #     for cls_base in cls_bases:
        #         if hasattr(cls_base,'_banOverLoad_funcs'):
        #             _banOverLoad_funcs=getattr(cls_base,'_banOverLoad_funcs')
        #             print(_banOverLoad_funcs)
        #子类：




        # if len(cls_bases) != 0:  # 基类不为空
        #     for item in dir(cls):  # 获得cls(class sonTest)的所有属性
        #         if hasattr(getattr(cls, item), '-banOverLoad'):  # 当其属性对象中有-ffs属性的时
        #             print(True)

        super().__init__(cls_name, cls_bases, cls_dict)
    def func(func):
       setattr(func,'-banOverLoad',True)
       return func
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


# setattr(a,'name',['张三'])
# arr=getattr(a,'name')
# arr.append('李四')
# print(getattr(a,'name'))

