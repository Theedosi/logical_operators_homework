def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    121
    a2 = x %10 # 1
    a3 = ((x-a2)//10)%10 #2 
    a1 = x //100 #1
    
    return a1 == a2 or a2 == a3
print(main(12))