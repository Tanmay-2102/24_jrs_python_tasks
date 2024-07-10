#Q1
#def list():
    #my_list=[]
    #n=int(input("Enter number of elements:"))
    #for i in range(1,n+1):
        #l=int(input("Enter even numbers:"))
        #if l%2==0:
            #my_list.append(l)
    #return my_list

#print(list())


#Q2
#def count(str):
  #l=len(str)
  #countv=0
  #countc=0
  #counts=0
  #countd=0
  #for i in range(0,l):
    #if(str[i]==" "):
      #counts=counts+1
    #elif(str[i]=='A'or str[i]=='E'or str[i]=='I'or str[i]=='O'or str[i]=='U' or str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
      #countv=countv+1
    #elif('A'<=str[i]<='Z' or 'a'<=str[i]<='z' ):
      #countc=countc+1
    #elif('0'<=str[i]<='9'):
      #countd=countd+1
  #print("Spaces",counts)
  #print("Vowels",countv)
  #print("Consonants",countc)
  #print("Digits",countd)

#str=input("Enter a string:")
#count(str)


#Q3
# def longest(l):
#   n=len(l)
#   max=0
#   k=0
#   for i in range(n):
#     if(max<len(l[i])):
#       max=len(l[i])
#       k=i
#     elif(max==len(l[i])):
#       continue
#   return l[k]
#
# n=int(input("Enter no. of elements:"))
# l=[]
# for i in range(n):
#   s=input("Enter the String:")
#   l.append(s)
#
# print(longest(l))


#Q4
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for i in nums:
#             if nums.count(i) > len(nums)//2:
#                 return i


#Q5
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         alphabet = [0] * 26
#         for c in ransomNote:
#             idx = ord(c) - ord('a')
#             i = magazine.find(c, alphabet[idx])
#             if i == -1:
#                 return False
#             alphabet[idx] = i + 1
#         return True


#Q6
# class Solution(object):
#   def firstUniqChar(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     num_of_appear = Counter(s)
#     if 1 not in num_of_appear.values():
#       return -1
#     for index, char in enumerate(s):
#       if num_of_appear[char] == 1:
#         return index
#     return -1
