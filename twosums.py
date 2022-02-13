def twosums(nums,target: int):
    seen={}
    for i,value in enumerate(nums):
        remaining=target-nums[i]
        if remaining in seen:
            return[i,seen[remaining]]
        else:
            seen[value]=i
n=[23,45,223,55,2,34]
t= 79
x=twosums(n,t)
print(x)