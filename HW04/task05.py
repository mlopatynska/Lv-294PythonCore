text = raw_input('Enter your text for checking:\n')
lookup = raw_input('Tell we the beginnig of words which I have to look for:\n')
textwords = text.split()
for i in textwords:
  if i.startswith(lookup):
    print i
