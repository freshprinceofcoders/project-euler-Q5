#first_num // gcd(first_num, second_num) * second_num
import math

def compute_LCM():
    ans = 1
    for second_num in range(1,20):
        ans *=  getLCM(ans, second_num)
    return ans
       
def getLCM(ans, second_num):
    return second_num //math.gcd(second_num, ans)

print(compute_LCM())

