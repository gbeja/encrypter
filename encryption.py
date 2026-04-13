def crypted(sentence):
    mapping = {
        "a": "@", "b": "#", "c": "$", "d": "%", "e": "^",
        "f": "&", "g": "*", "h": "+", "i": "=", "j": "!",
        "k": "?", "l": "~", "m": "`", "n": "|", "o": "{",
        "p": "}", "q": "[", "r": "]", "s": "<", "t": ">",
        "u": "(", "v": ")", "w": "-", "x": "_", "y": ";",
        "z": ":"
    }

    encryption = ""

    for element in sentence:
        encryption += mapping.get(element.lower(), element)

    return encryption


print(crypted(input("What do you want to encrypt: ")))
