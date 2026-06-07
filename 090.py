# Check Palindrome using Recursion

def palindrome(st):

    if len(st) <= 1:
        return "Palindrome"

    if st[0] == st[-1]:
        return palindrome(st[1:-1])
    else:
        return "Not a Palindrome"


print(palindrome("madam"))
print(palindrome("121"))
print(palindrome("python"))
