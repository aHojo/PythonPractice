import re


def replaceString(string, char=' '):

    return re.sub(r'^' + char + r'+' + r'|' + char + r'+' + r'$', '', string)


word = "-I have whitespace-"
print(replaceString(word, '-'))
