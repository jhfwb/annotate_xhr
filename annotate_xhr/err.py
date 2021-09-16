class AnnotateException(Exception):
    """注解错误"""

class AnnotateSiteException(AnnotateException):
    """注解存在的位置错误导致的。"""
    def __init__(self,msg,site='function' or 'class' or 'module'):
        self.msg=msg
    def __str__(self):
        return super(AnnotateSiteException, self).__str__()
class OverloadException(AnnotateException):
    # def __init__(self, msg, site='function' or 'class' or 'module'):
    #     self.msg = msg
    pass
    # def __str__(self):
    #     return super(AnnotateSiteException, self).__str__()

if __name__ == '__main__':
    raise AnnotateSiteException('你好')

