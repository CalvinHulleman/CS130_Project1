import statistics as stat
import matplotlib.pyplot as plt
f = open("StudentExercise.csv")
hours = []
d = dict()
next(f)
for row in f:
    num = row.split(",")
    if num[0] != "," and num[0] != '':
        n = float(num[0])
        hours.append(n)
        #if num != ',':
        d[n] = d.get(n,0) + 1
#print(hours)


fig, ax = plt.subplots()
ax.bar(sorted(d.keys()), d.values())
ax.set(title = "Student's Exercise", xlabel = "Hours of Exercise Per Week")
plt.show()

def average(ls):
    return stat.mean(ls)

def prop_above(ls):
    av = average(ls)
    count = sum(1 for x in ls if x > av)
    return count/len(ls)

def median(ls):
    return stat.median(ls)

print("Average:", average(hours))
print("Proportion above Average:", prop_above(hours))
print("Median:", median(hours))

