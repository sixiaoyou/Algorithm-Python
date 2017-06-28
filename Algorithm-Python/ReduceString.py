list = ["abce","abcdef"]
import  collections
# a = "aabbbccceeee"
for j in list:
    b = collections.Counter(j)
    c = ""
    for i in b.keys():
        c+=i+str(b[i])
    print c if len(c) != 2* len(j) else j