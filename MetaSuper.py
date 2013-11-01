'''
Created on Oct 30, 2013

@author: aaronkrolik
'''
from inspect import isfunction

class MetaSuper(type):
    def __new__(cls, name, bases, attrs):
        classFunctions = filter(lambda x: isfunction(x[1]), attrs.items())
        for item in classFunctions:
            attrs[item[0]] = cls.__genericWrapper(item[1])
        return super(MetaSuper, cls).__new__(cls, name, bases,attrs)
    
    @classmethod  
    def __genericWrapper(cls, funcIn):
        def closure(*args, **kwargs):
            cls.methodBefore()
            retValue = funcIn(*args, **kwargs)
            cls.methodAfter()
            return retValue
        return closure
    
    @classmethod
    def methodBefore(cls):
        pass
    @classmethod
    def methodAfter(cls):
        pass
        
class MetaTiming(MetaSuper):
    @classmethod
    def methodBefore(cls):
        print "BEFORE2"
        
        
class foo():
    __metaclass__= MetaSuper
    
    def helloWorld(self):
        print "hello world"
    def hw(self):
        print "FOO"
        
class bar(foo):
    __metaclass__=MetaTiming
    
    def helloWorld(self):
        print "hello world sub"
        
x = bar()
x.helloWorld()
