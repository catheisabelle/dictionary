thisdict = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..",
            "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....",
            "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..",
            "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.",
            "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-",
            "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-",
            "Y" : "-.--", "Z" : "--..","a" : ".-", "b" : "-...", 
            "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", 
            "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", 
            "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", 
            "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", 
            "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", 
            "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..",
            "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-",
            "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..",
            "9" : "----.", "0" : "-----", " " : "/"}

def text_to_morse(text):
    return ' '.join(thisdict[char] for char in text if char in thisdict)

sentence = input("sentence = ")
print(text_to_morse(sentence))
