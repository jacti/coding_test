from sys import stdin
# from collections import deque
# stdin = open("input.txt","r")
input = stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

str1, str2 = (str2, str1) if len(str2) > len(str1) else (str1, str2)

a = ord('a')
index_list = [set() for _ in range(ord('z') - a +1)]

for i, txt in enumerate(str1):
    index_list[ord(txt)-a].add(i)

max_count = 0
max_str = ""
# q = deque()

# for i, txt in enumerate(str2):
#     if index_list[ord(txt)-a]:
#         for index in index_list[ord(txt)-a]:
#             q.appendleft((i,index,txt,1))

# while q:
#     str_index, index, txt, count = q.pop()
#     str_index += 1
#     index +=1

#     if str_index < len(str2) and index in index_list[ord(str2[str_index])- a]:
#         q.appendleft((str_index,index,txt+str2[str_index],count+1))
#     else:
#         if max_count < count:
#             max_count = count
#             max_str = txt

candidates_list = [(0,{})]
for i,txt in enumerate(str2):
    new_candidates_list = []
    for count, candidates in candidates_list:
        if candidates:
            new_candidates_list.append((count+1,{x+1 for x in candidates & index_list[ord(txt)-a] }))
        else:
            if max_count < count:
                max_count = count
                max_str = str2[i-count-1:i-1]
    new_candidates_list.append((0,{x+1 for x in index_list[ord(txt)-a]}))
    candidates_list = new_candidates_list

for count, candidates in candidates_list:
    j=i
    if candidates:
        count +=1
        j+=1
    if max_count < count:
        max_count = count
        max_str = str2[j-count:j]
        count = 0

print(max_count)
print(max_str)