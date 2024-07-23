import matplotlib.pyplot as plt

years = list(range(2024, 2036))
N_positive = [10.00, 11.00, 12.10, 13.31, 14.64, 16.11, 17.72, 19.49, 21.44, 23.58, 25.94, 28.53]
N_negative = [10.00, 9.00, 8.10, 7.29, 6.56, 5.90, 5.31, 4.78, 4.30, 3.87, 3.49, 3.14]

plt.figure(figsize=(10, 6))

plt.scatter(years, N_positive, color='b', label='N_positive')
plt.scatter(years, N_negative, color='r', label='N_negative')

plt.title('Comparison of N(t) with Different Correlation Coefficients')
plt.xlabel('Year')
plt.ylabel('N(t)')

plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()