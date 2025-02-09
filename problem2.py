letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''
name = input("Enter your name : ")

print(letter.replace("<|Name|>", name).replace("<|Date|>", "07-02-2025"))