Temperature Data Analysis

This repository contains a Python script that reads, cleans, analyzes, and visualizes temperature data. The script uses the Pandas library for data manipulation and Matplotlib for data visualization.
🧠 Overview

    Data Input: The script reads temperature data from a CSV file.

    Data Cleaning: It handles invalid temperature values by coercing them to numeric and dropping missing values.

    Basic Statistics: The script calculates the average, maximum, and minimum temperatures.

    Alert Generation: It identifies temperature readings above a certain threshold (85ºC) and marks them as alerts.

    Visualization: The data is plotted over time, with a horizontal line indicating a safe temperature limit.

📋 Features

    Data Cleaning: Handles invalid or missing temperature data.

    Basic Statistics: Computes basic temperature statistics like mean, max, and min.

    Alert Generation: Filters temperature readings exceeding the safe limit (85ºC).

    Graphical Representation: Displays a time series plot of temperatures over time with an alert threshold line.

🔧 Technologies

    Python 3.7+

    Pandas

    Matplotlib

🛠️ How to Run

    Install the necessary libraries:

pip install pandas matplotlib

Ensure you have a CSV file (temperatures.csv) formatted with two columns:

    timestamp: Date and time of the temperature reading.

    temperature: Temperature value in degrees Celsius.

The script assumes that the file has no headers.

Run the Python script:

    python temperature_analysis.py

    The script will output raw data, statistics (average, max, and min), alerts for high temperatures, and display a chart with temperature data over time.

🧑‍💻 Code Explanation

    Reading Data: The CSV file is loaded into a DataFrame using pandas.read_csv().

    Cleaning Data: Invalid temperature values are coerced to NaN using pd.to_numeric(), and any rows with missing data are dropped.

    Statistics: The script calculates basic statistics, such as average, maximum, and minimum temperatures.

    Alerts: It filters out temperature readings higher than 85ºC and prints those entries as high-temperature alerts.

    Chart: A plot of temperature over time is generated, with a red dashed line marking the safe temperature limit (85ºC).

📚 Learning Objectives

    Learn how to read and process temperature data using Pandas.

    Understand how to clean and manipulate data in Python.

    Visualize time-series data and identify key insights.

    Work with alerts and thresholds for temperature monitoring.

  👩‍💻 Author

Karine Oliveira
Computer Science student at Saint Leo University
Currently living in Weert, Netherlands 🇳🇱

📬 Contact:

    LinkedIn https://www.linkedin.com/in/karine-c-oliveira/
