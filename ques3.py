import matplotlib.pyplot as plt

months = ["January", "February", "March", "April"]
attendance = [85, 90, 95, 88]

plt.plot(months, attendance, marker='o')
plt.xlabel("Month")
plt.ylabel("Average Students Present")
plt.title("Monthly Attendance Trend")
plt.show()
