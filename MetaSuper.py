'''
Created on Oct 30, 2013

@author: aaronkrolik
'''
from inspect import isfunction
import time

class MetaSuper(type):
    def __new__(cls, name, bases, attrs):
        classFunctions = filter(lambda x: isfunction(x[1]), attrs.items())
        for item in classFunctions:
            attrs[item[0]] = cls._genericWrapper(item[1])
        return super(MetaSuper, cls).__new__(cls, name, bases,attrs)
    
    @classmethod  
    def _genericWrapper(cls, funcIn):
        def closure(*args, **kwargs):
            cls.methodBefore(*args, **kwargs)
            retValue = funcIn(*args, **kwargs)
            cls.methodAfter(retValue)
            return retValue
        return closure
    
    @classmethod
    def methodBefore(cls, *args, **kwargs):
        pass
    @classmethod
    def methodAfter(cls, *args, **kwargs):
        pass
    
class MetaTiming(MetaSuper):
    @classmethod
    def methodBefore(cls, *args, **kwargs):
        cls.start = time.time()
    @classmethod
    def methodAfter(cls, *args, **kwargs):
        cls.elapsed = time.time()-cls.start
        print "elapsed time (seconds): ", cls.elapsed
        
class MetaMemo(MetaSuper):
    def __new__(cls, name, bases, attrs):
        print "init"
        cls.memo={}
        return super(MetaMemo, cls).__new__(cls, name, bases,attrs)
    
    @classmethod
    def _genericWrapper(cls, funcIn):
        def closure(*args, **kwargs):
            cls.methodBefore(*args, **kwargs)
            if kwargs:
                retValue = funcIn(*args, **kwargs)
            else:
                try:
                    #print args, cls.memo.get(args, "not memoized yet")
                    cls.memo[args] = retValue = cls.memo.get(args, funcIn(*args))
                except TypeError:
                    #print "TYPE ERROR" 
                    retValue = funcIn(*args)
            cls.methodAfter(retValue)
            return retValue
        return closure
            
            
    
    
     
     
if __name__ == "__main__":   
    class TestTiming():
        __metaclass__= MetaTiming
        
        def spin(self):
            x=1000
            time.sleep(2)
            while x>0:
                x-=1
            
    class TestMemo():
        __metaclass__=MetaMemo
        
        def add5(self, input):
            return input+5
    
#     x = TestMemo()
#     output1 = x.add5(5)
#     print "output1, ",output1
#     output2 = x.add5(5)
#     print "output2, ",output2
    
    #x = TestTiming()
    #x.spin()
    
        


