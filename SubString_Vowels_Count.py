# Program to print the substring containing maximum number of vowels and if two substrings
# contains equal number of vowels in a string the print the first one. And if the string doesn't
# contain any vowels print "Not found!".


def findSubstring(s, k):
    # s = Input string and k = integer/the size of substring
    vowels = {"a", "e", "i", "o", "u"}
    var = k
    countdict = {}
    if any(i in s for i in vowels) and len(s) >= k:
        for i in range(len(s)):
            count = 0
            if len(s[i:var]) == k:
                for j in s[i:var]:
                    if j in vowels:
                        count += 1
                countdict[s[i:var]] = count
                var += 1
            else:
                break
        maxval = countdict[list(countdict.keys())[0]]
        item = list(countdict.keys())[0]
        for j in countdict.keys():
            if maxval < countdict[j]:
                maxval = countdict[j]
                item = j
        print(item)

    else:
        print("Not found!")


if "__main__" == __name__:
    findSubstring("iiiurreee", 2)
