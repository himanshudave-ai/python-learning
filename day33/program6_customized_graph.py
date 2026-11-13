import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [10000, 15000, 12000, 20000, 25000]

plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8,
    label="Monthly Sales"
)

plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales (Rs.)")

plt.grid(True)
plt.legend()

plt.show()