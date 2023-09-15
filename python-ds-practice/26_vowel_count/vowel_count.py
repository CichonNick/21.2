def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    Answer

    def vowel_count(phrase)
    count = 0
    vowels = 'aeiouAEIOU'
    for letters in phrase:
        if letters in vowels:
            count = count + 1
