import math


def area(r):
    '''
    Return area of circle.

        Parameters:
            r (float): Radius of circle.
        
        Return value:
            area (float): Area of circle.
    '''
    return math.pi * r * r / 2


def perimeter(r):
    '''
    Return perimeter of circle.

        Parameters:
            r (float): Radius of circle.
        
        Return value:
            perimeter (float): Perimeter of circle.
    '''
    return 2 * math.pi * r

