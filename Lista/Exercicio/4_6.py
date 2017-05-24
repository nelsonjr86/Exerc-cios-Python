import sys
hrs = input("Digite as horas: ")
vhrs = input("Digite a hora regular: ")
OVERTIME_RATE = 1.5
try:
    hrs = float(hrs)
    vhrs = float(vhrs)
except:
    print ("Digite um valor")
    sys.exit(1)
def computepay(hrs, vhrs):
    if hrs > 40:
        overtime_hours = hrs - 40  # hours over 40
        hrs -= overtime_hours  # regular rate hours
        overtime_pay = overtime_hours * vhrs * OVERTIME_RATE
        return (hrs * vhrs) + overtime_pay
    else:
        return (hrs * vhrs)
print ("Pay: %.2f" % computepay(hrs, vhrs))