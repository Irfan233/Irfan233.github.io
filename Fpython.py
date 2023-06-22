# num=[1,2,3,4,5]
# def sumofarray(num):
#     a = (1, 2, 3, 4, 5)
#     x = sum(a)
#     for I in array(len[num]):
#         sum+=num[i]
#         return sum
#     print(sumofarray(num))
        
# def reverse(s):
#     s = []
#     for i in s:
#         s = i + s
#         return s
#     s=[1,2,3,4,5,6];
#     print("end="())
    
# list=[1,2,3,4,5]
# print(list)
# reverse_list=[]
# for i in list:
#     reverse_list.insert(0,i)
# print(reverse_list)

# list=[1,2,3,4,5]
# print(list)
# list=[]
# for i in list:
#         list=[i] + new_list
# print(new_list)
list1 = [1, 2, 3, 4, 5]
L = len(list1)

for i in range(int(L / 2)):
        n = list1[i]
        list1[i] = list1[L - i - 1]
list1[L - i - 1] = n

print(list1)







