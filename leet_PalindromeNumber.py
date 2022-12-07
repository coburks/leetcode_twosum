





"""



x = 122



a = str(x)
b = str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 1
        while a == b:
            i += 1
            print("true")
            return True        
        else:
            print("false")
            return False


    isPalindrome()







^^^ the above solution was correct but i want to try and do it without converting to string







"""

# this is a method i found online to reverse a number using modulo
# in this case the number is 123
# this method would have to be converted to a loop



x = 123
tmp = 123
rev = 0 # x reversed

a = tmp % 10

print(a)


rev = rev * 10 + a


print(rev)

tmp /= 10

print(tmp)

a = tmp % 10
rev = rev * 10 + a
print(rev)

tmp /= 10

print(tmp)

a = tmp % 10
rev = rev * 10 + a
tmp /= 10

p = int(tmp)
print(p)














































































