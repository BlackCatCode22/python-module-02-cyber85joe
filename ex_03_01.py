sh  = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
#print(fh, fr)
if  fh > 40 :
    # print("Overtime")
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40) * (fr * 0.5)
    print("Pay:",otp)
    xp = reg + otp
else:
    # print("regular")
    print("regular")
    xp = fh * fr
print("Pay:",xp)