**Fuel Consumption Linear Regression**
This repository demonstrates a simple linear regression model using Python’s scikit-learn. The project analyzes the relationship between vehicle engine size and CO2 emissions using the FuelConsumption.csv dataset.

**The workflow includes:**
- Data loading with pandas
- Selecting engine size as the independent variable and CO2 emissions as the dependent variable
- Training a regression model with scikit-learn
- Predicting emissions for a single input (e.g., engine size = 2.6)
- Generating a regression line using NumPy’s linspace
- Visualizing results with matplotlib scatter plots and regression line

This project highlights how regression can be used both for prediction and visualization. The scatter plot shows actual data points, while the regression line illustrates the statistical relationship captured by the model.

Ideal for beginners, this repository demonstrates the end-to-end process of loading data, fitting a model, making predictions, and plotting results. Future improvements could include adding more features (like cylinders), evaluating model accuracy with metrics such as R², and experimenting with multiple regression techniques.

**Requirements**
To run this project, install the following libraries:
pandas, numpy, matplotlib, scikit-learn
