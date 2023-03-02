def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    s=x
    a = s%10
    s//=10
    b = s%10
    s//=10
    c = s%10
    return (x>99 and c ==a) or (x<=99 and a==b)
print(main(11))