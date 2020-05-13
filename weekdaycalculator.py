#Arina Momajjed
#Weekday Calculator
print ("Weekday Calculator")
print ("This program calculates the weekday for any dates based on the Gregoran calendar (years 1700+).")
yr = str (input ("year (yyyy): "))
m = int (input ("m (m): "))
d = int (input ("d (d): "))
y = list (yr)
y = [int (x) for x in str (yr)] 
a = [y[0], y[1]]
if (y[2] == 0):
    lastn = y[3]
else:
    b = [y[2], y[3]]
    lastn = int (''.join (str(x) for x in b))
first2n = int (''.join (str (x) for x in a))
num = (lastn // 4 + lastn) % 7 
c = first2n % 17
if (c == 0):
    ycode = num + 5
elif (c == 1):
    ycode = num + 3
elif (c == 2):
    ycode = num + 1
elif (c == 3):
    ycode = num
mlistly = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
mlist = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
if (lastn % 4 == 0): 
    mcode = mlistly[m - 1]
else:
    mcode = mlist[m - 1]
code = mcode + ycode + d
final = code % 7
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ans = day [final - 1]
print (ans)
