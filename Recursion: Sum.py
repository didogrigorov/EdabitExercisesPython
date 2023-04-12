# Python program to find the sum of natural using recursive function

def recur_sum(num):

   if num <= 1:
       return num
   else:
       total = 0
       recursive_total = num + recur_sum(num-1)
       total += recursive_total
       return total

# change this value for a different result
print(recur_sum(5))
