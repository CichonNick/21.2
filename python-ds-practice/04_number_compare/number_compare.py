def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    Answer

    def number_compare(a,b):
    if a==b:
        print('Numbers are equal')
    elif b > a:
        print('Second number is greater')
    else:
        print('First number is greater')
