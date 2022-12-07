
# index of array items start at 0 then increment by 1
# so the first item of nums is "1" , with an index number of 0

# i = nums.index() # the index of the highest value item of nums


# for v in nums:
#         if nums[0] + rem == target:
#             print(nums[0],i)
#         if nums[1] + rem == target:
#             print(nums[1],i)
#         if nums[2] + rem == target:
#             print(nums[3],i)
#         else:
#             print("no solution for input")



# print(rem)
# print(nums[0] + rem)
# print(nums[1] + rem)
# print(nums[2] + rem)
# print(nums[3] + rem)


# for v in nums:
#     print(nums.index(v))
# pass


# while sum < target:

# for ele in range(0, len(nums)):
#     target = target + nums[ele]
#     print(target)



# for ele in nums:
#         if ele < target:
#             x = target - ele 
#         if ele > target:
#             x = ele - target
#         for ele in nums:
#             a = x + ele
#             if a == target:
#                 x = abs(x - target)
#                 y = ele
#             if x + y == target:                
#                  print(nums.index(x) , nums.index(y))
   



  
      

# for ele in nums:
#     if ele < target:
#         x = target - ele
#     if ele > target:
#         x = ele - target
#     for ele in nums:
#         x += ele
#         print(x)

        



"""



target = 37
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
size = len(nums)
    
def output():
    for x in nums:
        for y in nums:
            if x + y == target:
                print(nums.index(x) , nums.index(y))
     

output()
    

     




# this code is O(n^2) time complexity, and it needs to be faster than that,
# so the solution will have to be O(n), meaning we can only iterate through
# the array once

"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            pair = []
            table = {}   
            for k,v in enumerate(nums):
                y = target - v
                if y in table:
                    pair.append(table[y])
                    pair.append(k)
                    return pair                                     
                else:
                    table[v] = k
            return
            

# target = 9
# nums = [2,7,11,15] 

# hashing(nums, target)










"""
k, v
where k is the key of an element in nums
v is the value



"""
    










"""

        def hashing(nums, target): 
                pair = []
                table = {}   
                for k,v in enumerate(nums):
                    y = target - v
                    if y in table:
                        pair.append(table[y])
                        pair.append(k)
                        return pair                                    
                    else:
                        table[v] = k
                return


        target = 9
        nums = [2,7,11,15] 

        hashing(nums, target)





mine! ^^^^^
-------------------------------------------------------------------------

formatted for leetcode solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            pair = []
            table = {}   
            for k,v in enumerate(nums):
                y = target - v
                if y in table:
                    pair.append(table[y])
                    pair.append(k)
                    return pair                                     
                else:
                    table[v] = k
            return
            














"""







