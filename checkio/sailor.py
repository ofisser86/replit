VOWELS = "aeiouy"

def translate(phrase):
    p = []
    for i in phrase:
        if i not in VOWELS:
            p.append(i)
            i += 1
            continue
    return phrase


translate("hieeelalaooo")