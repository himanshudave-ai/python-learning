import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
temperature = [30, 32, 29, 35, 33]

plt.plot(days, temperature, marker="o")

plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (Celsius)")

plt.show()