COLOUR_TO_CODE = {"absolutezero": "#0048ba", "acidgreen": "#$b0bf1a", "aliceblue": "#f0f8ff", "amaranth": "#e52b50",
                  "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1",
                  "aqua": "#00ffff"}

colour = input("Colour: ").strip().lower()
while colour != "":
    if colour in COLOUR_TO_CODE:
        print(COLOUR_TO_CODE[colour])
    else:
        print("Invalid colour")
    colour = input("Colour: ").strip().lower()