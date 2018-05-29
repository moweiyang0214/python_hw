def countchar(s):
    lst = [0] * 26
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <='z':  
            lst[ord(s[i])- ord('a')] += 1
    print(lst)

if __name__ == "__main__":
    s = "Hope is a good thing."
    s = s.lower()
    countchar(s)