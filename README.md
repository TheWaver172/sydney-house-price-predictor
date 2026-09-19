# Sydney House Price Predictor

This project develops a machine-learning application that estimates house sale prices in Liverpool, Ryde, and Mosman. It uses a Random Forest regression pipeline trained on 1,200 disclosed Sydney property sales.

## 1. Set up the project

### Clone the repository

Open a terminal and clone the repository using the URL available from the green **Code** button on GitHub:

```powershell
git clone https://github.com/TheWaver172/sydney-house-price-predictor.git
```

Move into the downloaded project folder:

```powershell
cd sydney-house-price-predictor
```

### Download without Git

Alternatively:

1. Select the green **Code** button on GitHub.
2. Select **Download ZIP**.
3. Extract the downloaded ZIP file.
4. Open a terminal inside the extracted project folder.

Forking is not required unless the user wants to create and modify their own GitHub copy.

## 2. Install the required libraries

From the project folder, run:

```powershell
python -m pip install -r requirements.txt
```

If `python` is not recognised, use:

```powershell
py -m pip install -r requirements.txt
```

The saved model requires `scikit-learn==1.7.2`, which is fixed in `requirements.txt` to prevent compatibility errors.

## 3. Project structure

```text
project-folder/
├── app.py
├── code.ipynb
├── README.md
├── requirements.txt
├── sydney_house_sales.csv
├── figures/
│   ├── model_comparison.png
│   ├── prediction_errors.png
│   ├── sale_price_distribution_by_suburb.png
│   └── time_and_property_relationships.png
└── models/
    └── house_price_model.joblib
```

## 4. Run the notebook

Open `code.ipynb` in Jupyter Notebook or Visual Studio Code and run all cells from top to bottom.

The notebook will:

1. Load and inspect the housing dataset.
2. Prepare the data and engineer additional features.
3. Compare Ridge Regression, Random Forest, and Gradient Boosting.
4. Evaluate the models using five-fold cross-validation.
5. Investigate the five largest prediction errors.
6. Save the generated figures in the `figures` folder.
7. Export the selected Random Forest pipeline to `models/house_price_model.joblib`.

Run the complete notebook before launching the application if the exported model is unavailable or needs to be regenerated.

## 5. Launch the application

From the project folder, run:

```powershell
python -m streamlit run app.py
```

Alternatively:

```powershell
py -m streamlit run app.py
```

Streamlit should open the application automatically. If it does not, open the following address in a web browser:

```text
http://localhost:8501
```

Keep the terminal open while using the application. Press `Ctrl+C` in the terminal to stop it.

## 6. Use the application

Enter the following property information:

- suburb;
- expected sale method;
- valuation date;
- number of bedrooms;
- number of bathrooms;
- number of parking spaces; and
- land size in square metres.

If the land size is unavailable, select **Land size is unknown**. The preprocessing pipeline will replace the missing value using median imputation.

Select **Predict sale price** to display the estimated sale price in Australian dollars.

## 7. Model information

Random Forest was selected as the deployment model because it achieved the lowest mean five-fold cross-validation MAE among the evaluated models.

The saved pipeline includes:

- median imputation for missing numerical values;
- one-hot encoding for categorical variables;
- engineered property and sale-date features;
- a logarithmic target transformation; and
- the trained Random Forest regressor.

## 8. Limitations

The application is based on disclosed historical sales from three Sydney suburbs. It does not account for every factor affecting property value, including renovation quality, condition, architectural design, views, frontage, exact street position, or buyer competition.

Predictions for unusual prestige properties and houses outside the ranges represented in the training data should be interpreted cautiously. The displayed result is decision support only and is not a professional property valuation.