# -*- coding: utf8 -*-
k = int(input("Будь ласка, введіть номер дня в році: "))
n = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if k%7 == 1:
    print "За даних умов, {}-й день року - це {}".format(k, n[0])
elif k%7 == 2:
    print "За даних умов, {}-й день року - це {}".format(k, n[1])
elif k%7 == 3:
    print "За даних умов, {}-й день року - це {}".format(k, n[2])
elif k%7 == 4:
    print "За даних умов, {}-й день року - це {}".format(k, n[3])
elif k%7 == 5:
    print "За даних умов, {}-й день року - це {}".format(k, n[4])
elif k%7 == 6:
    print "За даних умов, {}-й день року - це {}".format(k, n[5])
elif k%7 == 0:
    print "За даних умов, {}-й день року - це {}".format(k, n[6])