# Laila Bahman

def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    return x + multiply(x,y-1)

def collectMultiples(intList,n):
    if len(intList) == 0:
        return []
    else:
        if (intList[0]%n == 0):
            return [intList[0]] + collectMultiples(intList[1:], n)
        else:
            return collectMultiples(intList[1:], n)

def countVowels(s):
    if len(s) == 0:
        return 0
    else:
        if (s[0] in ['A','E','I','O','U','a','e','i','o','u']):
            return 1 + countVowels(s[1:])
        else:
            return countVowels(s[1:])

def reverseVowels(s):
    if len(s) == 0:
        return s
    else:
        if (s[0] in ['A','E','I','O','U','a','e','i','o','u']):
            return reverseVowels(s[1:]) + s[0]
        else:
            return reverseVowels(s[1:])
    
def removeSubString(s,sub):
    firstIndex = s.find(sub)
    if (firstIndex != -1):
        String = s.replace(sub,'',1)
        return(removeSubString(String,sub))
    else:
        return s
