fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sum = sum + float(line[line.find(' '):])
    count = count + 1
print ("Average spam confidence:", sum / count)