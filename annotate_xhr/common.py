
def getAnnotateSite(annotateObj):
    """
    获得被注解对象的位置。
    :param annotateObj: 被注解的对象
    :return :func or class 。当返回值为func的时候，表示该注解在方法上面，当返回值维class的时候，表示该注解在类上面
    """
    if type(annotateObj) == type(lambda x: x):
        return 'func'
    else:
        return 'class'
