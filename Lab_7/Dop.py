def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    if cleaned == "":
        return False
    return cleaned == cleaned[::-1]


assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("   ") == False
assert is_palindrome("Python") == False
assert is_palindrome("А!") == False

print("Дополнительные проверки пройдены!")
