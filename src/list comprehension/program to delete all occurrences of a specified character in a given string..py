def DeleteOcccurences(Strings,char_del):
    result = ""
    for char in Strings:
        if char != char_del:
            result += char
    return result

result_del = DeleteOcccurences('Tutor Joes Computer Education','t')
print(result_del)

