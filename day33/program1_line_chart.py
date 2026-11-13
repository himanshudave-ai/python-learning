
import matplotlib.pyplot as plt

# Weekly test data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
marks = [65, 70, 75, 80, 90]

# Create line chart
plt.plot(days, marks, marker="o", label="Student Marks")

# Add title and labels
plt.title("Weekly Test Performance")
plt.xlabel("Days")
plt.ylabel("Marks")

# Display grid and legend
plt.grid(True)
plt.legend()

# Display chart
plt.show()
