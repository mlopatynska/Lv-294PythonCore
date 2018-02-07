k = int (raw_input ("enter day from 1 to 365 \n"))
n = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
n = n*53
if k in range(1,366):
    print n[k-1]
else:
    print ("Error. Enter please number from 1 to 365 ")