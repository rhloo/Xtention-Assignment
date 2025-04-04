# def is_anagram(str1,str2):
#     for i in range(len(str2)):
#         if str2[i] in str1:
#             print(f"{str2[i]} char is present both {str1} and {str2}")
# # is_anagram("listen","silent")
# is_anagram("hello","world")

def is_anagram(str1,str2):

    str1=list(str1.lower())
    str2=list(str2.lower())  
    str2.sort()
    str1.sort()
    print(str2)
    print(str1)
    return str1==str2
print(is_anagram("hello","world"))
print(is_anagram("listen","silent"))

