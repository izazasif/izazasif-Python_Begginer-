from functools import reduce


nums = [2,6,8,3,5,6,7]
evens =list(filter(lambda n:n%2==0,nums))
mp = list(map(lambda a:a+2,evens))
sum = reduce(lambda a,b:a+b,mp)
print(sum)
