# ==========================================================
# MACHINE LEARNING LAB
# LAB 01 : Introduction to Python for Data Analysis
# ==========================================================

# Aim:
# To understand the basics of Python for data analysis using NumPy and Pandas.
# The experiments include creating arrays, reshaping matrices, working with
# DataFrames, and performing basic dataset exploration.

# ==========================================================
# Import Required Libraries
# ==========================================================

import numpy as np
import pandas as pd

# ==========================================================
# Experiment 1
# Create a NumPy array using a Python list and display
# the array along with its shape and data type.
# ==========================================================

print("\nExperiment 1")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)

# Output Example:
# Array: [10 20 30 40 50]
# Shape: (5,)
# Data Type: int64


# ==========================================================
# Experiment 2
# Create a 3x4 matrix of zeros and a 2x5 matrix of ones.
# Display both matrices and their shapes.
# ==========================================================

print("\nExperiment 2")

zeros_matrix = np.zeros((3,4))
ones_matrix = np.ones((2,5))

print("3x4 Zero Matrix:\n", zeros_matrix)
print("Shape:", zeros_matrix.shape)

print("\n2x5 Ones Matrix:\n", ones_matrix)
print("Shape:", ones_matrix.shape)

# Output Example:
# Zero matrix and ones matrix printed with respective shapes


# ==========================================================
# Experiment 3
# Create a NumPy array from 1 to 12 and reshape it into
# a 3x4 matrix.
# ==========================================================

print("\nExperiment 3")

array = np.arange(1,13)

print("Original Array:", array)
print("Original Shape:", array.shape)

reshaped = array.reshape(3,4)

print("Reshaped Matrix:\n", reshaped)
print("Reshaped Shape:", reshaped.shape)

# Output Example:
# Original: [1 2 3 ... 12]
# Reshaped:
# [[1 2 3 4]
#  [5 6 7 8]
#  [9 10 11 12]]


# ==========================================================
# Experiment 4
# Create a NumPy array of 10 random integers and find
# minimum, maximum, mean, and sum.
# ==========================================================

print("\nExperiment 4")

random_array = np.random.randint(1,100,10)

print("Random Array:", random_array)
print("Minimum:", np.min(random_array))
print("Maximum:", np.max(random_array))
print("Mean:", np.mean(random_array))
print("Sum:", np.sum(random_array))

# Output Example:
# Random Array: [12 54 23 67 ...]
# Minimum: 12
# Maximum: 89
# Mean: 45.3
# Sum: 453


# ==========================================================
# Experiment 5
# Create a Pandas DataFrame using a dictionary containing
# student names and marks.
# ==========================================================

print("\nExperiment 5")

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)
print("\nData Types:\n", df.dtypes)

# Output Example:
# Name   object
# Marks  int64


# ==========================================================
# Experiment 6
# Read a CSV file using read_csv()
# Display first 5 rows and last 5 rows
# ==========================================================

print("\nExperiment 6")

# Dataset Link Example (Sample dataset used)
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

df_csv = pd.read_csv("iris.csv")

print("First 5 Records:\n", df_csv.head())
print("\nLast 5 Records:\n", df_csv.tail())

# Output Example:
# head() shows first five rows
# tail() shows last five rows


# ==========================================================
# Experiment 7
# Load dataset and display structure using info()
# ==========================================================

print("\nExperiment 7")

print(df_csv.info())

rows, cols = df_csv.shape
print("Number of Rows:", rows)
print("Number of Columns:", cols)

missing_values = df_csv.isnull().sum()
print("Missing Values:\n", missing_values)

# Output Example:
# dataset information including column types and non-null count


# ==========================================================
# Experiment 8
# Display statistical summary using describe()
# ==========================================================

print("\nExperiment 8")

summary = df_csv.describe()

print("Statistical Summary:\n", summary)

# Interpretation Example:
# Mean → average value
# Std → standard deviation showing spread
# Min → smallest value
# Max → largest value