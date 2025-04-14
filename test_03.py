# NEETCODE 250 (007)

# Leetcode 27. Remove Element

# Solution accepted! Beats 4.02%
def removeElement_00(nums: list[int], val: int) -> int:
    def swap(l: list[int], idx: int):
        for i, val in enumerate(l):
            if i > idx and val != l[idx]:
                temp = l[i]
                l[i] = l[idx]
                l[idx] = temp
                return

    count = nums.count(val)
    res = len(nums) - count
    for i, _val in enumerate(nums):
        if _val == val:
            # swap until value is out of range
            swap(nums, i)
    return res


# Solution 02. Beats 100%
# NOTE: Again, this is a case of doing everything at the same time. Not doing a, then b, then c
# But rather abc (all together) while iterating through the array ONCE.
# I don't really think like this, but hopefully it will get better with practice and time. 
def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for i in range(0, len(nums)):
        if nums[i] != val:      # if the value is not equal to the value that we're looking for
            nums[k] = nums[i]   # redefine this position (nums[i]) by (nums[k]) and increment k by one 
            k += 1              # thus counting the value that we're going to need at the end.
    return k


def main() -> None:
    print(removeElement(nums = [3,2,2,3], val = 3))         # 2, nums = [2,2,_,_] 
    print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)) # 5, nums = [0,1,4,0,3,_,_,_] 


if __name__ == '__main__':
    main()
