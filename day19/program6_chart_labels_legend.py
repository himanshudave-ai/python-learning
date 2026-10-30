import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 120, 150, 130, 170]
sales_2026 = [110, 140, 160, 150, 190]

plt.plot(months, sales_2025, marker="o", label="2025")
plt.plot(months, sales_2026, marker="s", label="2026")

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.show()