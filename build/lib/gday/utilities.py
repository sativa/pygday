""" Logic tests for floating point numbers """

import math
import sys

__author__  = "Martin De Kauwe"
__version__ = "1.0 (09.03.2011)"
__email__   = "mdekauwe@gmail.com"


def get_attrs(obj):
    """ Get user class attributes and exclude builitin attributes
    Returns a list
    
    Parameters:
    ----------
    obj : object
        clas object 
    
    Returns:
    -------
    attr list : list 
        list of attributes in a class object
    
    """
    return [i for i in obj.__dict__.keys() 
                if not i.startswith('__') and not i.endswith('__')]

class Bunch(object):
    """ group a few variables together 
    
    advantage is that it avoids the need for dictionary syntax, taken from the
    python cookbook; although nothing to guard against python reserved words 
    
    >>> point = Bunch(datum=y, squared=y*y, coord=x)
    """
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def switch(option, cases):
    """Use a dictionary to simulate a switch statement and avoid long if,elif"""
    try:
        return cases[option]
    except KeyError:
        raise ValueError("Unknown option %s" % option) 

class FloatLogic(object):
    """Series of logic tests for floating point numbers.
    
    Due to rounding issues we shouldn't test float comparisons, rather using 
    some tolerance see if the tests are met.

    see http://www.lahey.com/float.htm, adapted from scitools, as that wasn't
    working for me.
    """
   
    def __init__(self, comparison=None, tol=1E-14):
        """ Pick an operator'==', '<', '<=', '>', '>=', '!='. """
        
        d = {   '==': self.eq, 
                '!=': self.ne, 
                '<' : self.lt, 
                '<=': self.le, 
                '>' : self.gt, 
                '>=': self.ge    }
        self.comparison = d[comparison]
        self.tol = tol

    def __call__(self, arg1, arg2):
        """ Call the appropriate method given our comparison test """
        return self.comparison(arg1, arg2)
    
    def eq(self, arg1, arg2):
        """arg1 == arg2"""
        if math.fabs(arg1 - arg2) < self.tol + self.tol * math.fabs(arg2):
            return True
        else:
            return False 
            
    def ne(self, arg1, arg2):
        """arg1 != arg2"""
        return not self.eq(arg1, arg2)
    
    def lt(self, arg1, arg2):
        """arg1 < arg2"""
        if arg2 - arg1 > math.fabs(arg1) * self.tol:
            return True
        else:
            return False
            
    def le(self, arg1, arg2):
        """arg1 <= arg2"""
        return self.lt(arg1, arg2)

    def gt(self, arg1, arg2):
        """arg1 > arg2"""
        if arg1 - arg2 > math.fabs(arg1) * self.tol:
            return True
        else:
            return False    
        
    def ge(self, arg1, arg2):
        """arg1 >= arg2"""
        return self.gt(arg1, arg2)
   
   
# define shorter interface names for method calling
float_eq = FloatLogic('==')
float_ne = FloatLogic('!=')
float_lt = FloatLogic('<')
float_le = FloatLogic('<=')
float_gt = FloatLogic('>')
float_ge = FloatLogic('>=')
    
if __name__ == '__main__':
    
    print float_eq(0.0, 0.0)