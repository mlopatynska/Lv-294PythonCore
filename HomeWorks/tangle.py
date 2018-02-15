line=str(raw_input(" Enter a number "))
line=list(line)
min=line[0]
for i in line:
	if min>i:
		min=i
print min 
