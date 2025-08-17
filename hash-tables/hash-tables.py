dic = {
  "apple": 1.94,
  "banana": 2.1,
}


dic["avocat"] = 3.2

print(dic)


# duplicate [] 0(n)
nums = [1, 2, 3]

n = len(nums)
dic = {}
for x in range(0,n) :
    dic[nums[x]] = x

print(len(dic)!=n)