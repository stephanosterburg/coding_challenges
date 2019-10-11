from collections import Counter
from itertools import groupby
# Sherlock considers a string to be valid if all characters of the string
# appear the same number of times. It is also valid if he can remove just
# 1 character at 1 index in the string, and the remaining characters will
# occur the same number of times. Given a string s, determine if it is valid.
# If so, return YES, otherwise return NO.
def isValid(s):
    x = Counter(s).values()
    l = sorted(x, reverse=True)
    t = sorted([list(j) for i, j in groupby(l)], key=len)
    print(t)
    if len(t) == 1:
        return "YES"
    elif len(t) == 2 and len(t[0]) == 1:
        if abs(t[0][0] - t[1][0]) == 1 or t[0][0] == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


s = 'aabbccddeefghi'
print(isValid(s)) # NO

# All characters occur twice except for e which occurs 3 times.
# We can delete one instance of  to have a valid string.
s = 'abcdefghhgfedecba'
print(isValid(s)) # YES

s = 'aaaabbcc'
print(isValid(s)) # NO

s = 'aabbc'
print(isValid(s)) # YES


s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
print(isValid(s)) # YES


s = 'hyzzeohdidavrazjqqjfyulkoutdkywsyvrdlaitdirxkqicitijovtcpphcndwmzppmpziujzrtrcvavfjlceputwwhauvbjmnylvuuwopoqkonszzwdoqznognidorpbrazmwvaljsxzfpagmgxefktnxdqlvfoohnaflcquwnwcfwktchxhrsuqwmdtruhajkfumxplllnsjzlmjkvafqtdcywwsfycpewebnpoaegkftyoetrjjkookkmdrkhjodpstggtmpfridgoxxzijnwtziyrtfcjlrbexkxjzfcjiiafhzospmooxmhqsjzdadjzpiionnzyvzdfbtxqingfaqvuzwzcbkbqsmggziewjjbkfbcnqlsqbpmannerxghquqyvyerhpvuwywjojdhkutnkjrbizkavayqaekiwfesdaermjawgwjqfdtnefoaiosivcsrhwlmzpglbgjhctzjyuzeznehdzqybkrlhfxiwftxmceqxfcxzbczqigthyujjnusstapzvmnztfzahwaiabyjjusiqdtdznytnpukdjjyokzwhbgjehsndnxtqsyqfyjunferoqpcaqajtjtxsnlvakqrdqhipsfexjvnznrcfslzdewvujsuuilxyuhpomunyrazgsbmmplrthmnrekloxkouteiiawgryhyqjmeyxvtejjxpvkdswumqavaatgtrntkyfqycmujxdinytsspmfhmchmxpiqfdafjtenhyyedhrbcmvtyadlemzdcjujnuownulwsmbxvuyxgwshyvudktgmfcxsxnqmidlcpmakgajpwcwvzqajlixqlwkkkaysgjuvvugevrvtttovjoewzepkazwkcueiezfbvlhsdemyxctgtafsguegvatxuzhaynewanqfscephzyabduhzyqualuukbxlodhrqzwieaalcynddhnefdyfqsbawalmdudwuagycglegyklfxpmcq'
print(isValid(s)) # NO
