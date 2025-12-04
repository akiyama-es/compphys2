import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

with open("score.csv","r") as fileRef:
    year = []
    jpn = []
    math_ia = []
    math_iib = []
    for line in fileRef:
        fileList = line.split(",")
        print(fileList)
        if fileList[0] != "Year":
            year.append(int(fileList[0]))
            jpn.append(float(fileList[4]))
            math_ia.append(float(fileList[6]))
            math_iib.append(float(fileList[8]))

plt.plot(year, jpn, marker="o", label="Japanese")
plt.plot(year, math_ia, marker="o", label="Math IA")
plt.plot(year, math_iib, marker="o", label="Math IIB")
plt.legend()
plt.xlim(2006, 2025)
plt.xticks(range(2006,2026,3))
plt.ylim(0, 100)
plt.xlabel("Year")
plt.ylabel("Average Score")
plt.savefig("score.pdf")
