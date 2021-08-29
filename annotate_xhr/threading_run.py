# 用于多线程
import threading

from annotate_xhr.common import getAnnotateSite
from annotate_xhr.err import AnnotateSiteException


def threadingRun(func):
    """
    多线程装饰器，能够快速实现方法的多线程。放置在方法上面，能够使得方法以多线程的方式启动
    usege:
        >>> @threadingRun
        >>> def _haha():
        >>>     print(1)
    """
    def run(*args, **kwargs):
        if getAnnotateSite(func)!='func':
            raise AnnotateSiteException('注解的位置错误:该注解只能位于方法的上方')
        return threading.Thread(target=func, args=args, kwargs= kwargs).start()
    return run # 返回需要执行的新的方法