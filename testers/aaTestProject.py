import random

def random_case(text):
    return ''.join(random.choice([c.upper(), c.lower()]) for c in text)

def alternating_case(text):
    result = ''
    upper = True
    for c in text:
        if c.isalpha():
            result += c.upper() if upper else c.lower()
            upper = not upper
        else:
            result += c
    return result

def leet_speak(text):
    leet_dict = {
        'a': '4', 'b': '8', 'e': '3', 'l': '1', 'o': '0',
        's': '5', 't': '7', 'g': '9', 'z': '2'
    }
    return ''.join(leet_dict.get(c.lower(), c) for c in text)

def emoji_speak(text):
    emoji_dict = {
        'a': '🅰️', 'b': '🅱️', 'c': '🌜', 'd': '🌛',
        'e': '📧', 'g': '🌀', 'h': '♓', 'i': '🎐',
        'l': '👢', 'm': '〽️', 'n': '🎶', 'o': '🅾️',
        'p': '🅿️', 'r': '🌱', 's': '💲', 't': '🌴',
        'u': '⛎', 'v': '✅', 'w': '🔱', 'x': '❌',
        'y': '🍸', 'z': '💤'
    }
    return ''.join(emoji_dict.get(c.lower(), c) for c in text)

def funky_translator(text, style):
    if style == "random":
        return random_case(text)
    elif style == "alternate":
        return alternating_case(text)
    elif style == "leet":
        return leet_speak(text)
    elif style == "emoji":
        return emoji_speak(text)
    else:
        return "❗Unknown style. Please choose from: random, alternate, leet, emoji."

# 🧪 Example usage:
if __name__ == "__main__":
    print("🎉 Welcome to Funky Translator 🎉")
    text = input("Enter your message: ")
    print("Choose your funk style: random | alternate | leet | emoji")
    style = input("Enter style: ").lower()

    funky = funky_translator(text, style)
    print("\n🎨 Funky Output:\n" + funky)
