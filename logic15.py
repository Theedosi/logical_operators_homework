def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a//100
    x2 = a%10
    x3 = ((a-x2)//10)%2
    return (x1+x2+x3)%2==1
print(main(124))