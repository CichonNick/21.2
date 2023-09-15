def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    >>> [] should return false
    >>> () should return false
    >>> False should return false
    ____________________________________________________________________________

    
return [val for val in lst if val]
    
