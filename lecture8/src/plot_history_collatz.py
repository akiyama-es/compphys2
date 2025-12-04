import matplotlib.pyplot as plt

init_val = 100
filename = f"collatz_{init_val}.dat"

steps = []   
history = []  

with open(filename, "r") as f:
    for line in f:

        if line.startswith("#"):
            continue

        fileList = line.split()

        steps.append(int(fileList[0]))
        history.append(int(fileList[1]))

plt.plot(steps, history, marker="o")
plt.axhline(y=1, linestyle="--",color="red")
plt.xlabel("Step")
plt.ylabel("History of the Collatz problem")
plt.grid(True)
plt.savefig(f"collatz_{init_val}.pdf")


