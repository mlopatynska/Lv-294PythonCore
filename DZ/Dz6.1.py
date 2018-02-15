def countChars(chars, text):
    n = 0
    for char in text:
        if char in chars or char in chars.upper():
            n += 1
    return n

text = u'The doctor said I need about three weeks of recovery,But the nurses is loving me Saying the best part of the day is my half '

g = countChars(u"Golosni", text)
s = countChars(u"Prugolosni", text)

print u"Golosni: %i, prugolosni: %i" % (g, s)