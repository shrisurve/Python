import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X: ")
print(*range(1,50))
print("Values of Y(thrice of X):")
print(Y)
# plot lines and/or markers to the axis.
plt.plot(X, Y)
# Set the X axis lable of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title
plt.title('Draw a line')
# Display the figure.
plt.show()