from annotate_xhr.common import getAnnotateSite
from annotate_xhr.err import AnnotateSiteException


def singleObj(classT):
    """实现类的单例化;

    使用位置用在类的标签上，当创建该类的时候。如果该类被创建过，则不会再创建一次。

    usege:
        >>> @singleObj
        ... class H:
        ...     pass
    """
    def run(*args, **kwargs):
        if getAnnotateSite(classT)!='class':
            raise AnnotateSiteException('注解的位置错误:该注解只能位于类的上方')
        if hasattr(classT,'_instance')==False:
            setattr(classT,'_instance',object.__new__(classT,*args, **kwargs))
            getattr(classT, '_instance').__init__(*args, **kwargs)
        return getattr(classT,'_instance')
    return run