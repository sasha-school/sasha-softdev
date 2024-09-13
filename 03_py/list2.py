def count_evens(nums):
  counter =0
  for item in nums:
    if item%2==0:
      counter+=1
  return counter

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  return (sum(nums)-max(nums)-min(nums))/(len(nums)-2)

def sum13(nums):
  sum =0
  index1 =0
  while index1<len(nums):
    if nums[index1]==13:
      index1+=2
    else:
      sum+=nums[index1]
      index1+=1
  return sum