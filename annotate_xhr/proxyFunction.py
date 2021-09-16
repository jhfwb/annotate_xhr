from types import FunctionType

from annotate_xhr.common import getAnnotateSite
from annotate_xhr.err import AnnotateSiteException, AnnotateException


def proxy(proxy_func, filter_funcNames=None,proxy_funcNames=None):
    """
    实现aop编程的代理方法:在类的上方使用该注解。注意:
    注意:一旦方法名前面加上_则不会触发代理。
    :param function proxy_func : 这是代理方法，详细见例子中的自定义方法proxy_f()
    :param list filter_funcNames : 用来限定代理对象，filter_funcNames为None的时候，默认不开启该方法。filter_funcNames中的方法名，表示该
    方法名会被拦截，不会触发代理
    :param list proxy_funcNames :这是用来限定代理对象的。当proxy_funcNames为None的时候，默认所有方法都会被代理。反之则只会代理限定方法
    usege:

    >>> def proxy_f(func):#此为代理的方法。
    >>>     def newFunc(*args, **kwargs):
    >>>         print('此为前置方法')
    >>>         func(*args, **kwargs)#此为原方法
    >>>         print('此为后置方法')
    >>>     return newFunc

    >>> # @proxy(proxy_func=proxy_f) #当filter_funcNames没有传入参数时，则默认所有方法都会触发代理
    >>> @proxy(proxy_func=proxy_f, filter_funcNames=['haha'],proxy_funcNames=['xixi'])#只会触发xixi方法的代理,不触发haha代理
    >>> class dog:
    >>>     def xixi(self):
    >>>         print('嘻嘻')
    >>>     def haha(self):
    >>>         print('哈哈')
    >>> dog().xixi() #此方法触发代理
    >>> dog().haha() #此方法不触发代理


    """
    def new_func(obj):
        if getAnnotateSite(obj) != 'class':
            raise AnnotateSiteException('注解的位置错误:该注解只能位于类的上方')
        if filter_funcNames!=None and proxy_funcNames!=None:
            for filter_funcName in filter_funcNames:
                if filter_funcName in proxy_funcNames:
                    raise ValueError('@proxy方法中出现参数异常：存在参数相同(此冲突方法名为:'+filter_funcName+')的方法，既被要求代理，也被要求过滤(不被代理)')
        if proxy_funcNames == None:
            for item in dir(obj):
                if isinstance(getattr(obj, item), FunctionType) and not item.startswith('_'):
                    if filter_funcNames!=None:
                        if item not in filter_funcNames:
                            setattr(obj, item, proxy_func(getattr(obj, item)))
                    else:
                        setattr(obj, item, proxy_func(getattr(obj, item)))
        else:
            for funcName in proxy_funcNames:
                if hasattr(obj, funcName):
                    if filter_funcNames != None:
                        if funcName not in filter_funcNames:
                            setattr(obj, funcName, proxy_func(getattr(obj, funcName)))
                    else:
                        setattr(obj, funcName, proxy_func(getattr(obj, funcName)))
        return obj

    return new_func

if __name__ == '__main__':
    def proxy_f(func):
        def newFunc(*args, **kwargs):
            print('此为前置方法')
            func(*args, **kwargs)
            print('此为后置方法')
        return newFunc

    # @proxy(proxy_func=proxy_f) #当filter_funcNames没有传入参数时，则默认所有方法都会触发代理
    @proxy(proxy_func=proxy_f,filter_funcNames=['xixi'],proxy_funcNames=['xixi'])
    class dog:
        def xixi(self):
            print('嘻嘻')
        def haha(self):
            print('哈哈')
    dog().xixi() #此方法触发代理
    dog().haha() #此方法不触发代理

