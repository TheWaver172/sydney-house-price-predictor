from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import streamlit as st

MODEL_PATH = Path('models') / 'house_price_model.joblib'

@st.cache_resource
def load_model_bundle():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            'Run code.ipynb before starting the application.'
        )
    return joblib.load(MODEL_PATH)


st.set_page_config(
    page_title = 'Sydney House Price Predictor',
    page_icon = '🏠',
    layout = 'centered'
)

st.markdown(
    '<h1 style="text-align: center;">Sydney House Price Predictor</h1>',
    unsafe_allow_html = True
)

bundle = load_model_bundle()

suburb = st.selectbox('Suburb', bundle['suburbs'])
sale_method = st.selectbox('Expected sale method', bundle['sale_methods'])
sale_date = st.date_input(
    'Valuation date',
    value = bundle['training_date_max'].date()
)
bedrooms = st.number_input(
    'Bedrooms',
    min_value = 1,
    max_value = 15,
    value = 4
)
bathrooms = st.number_input(
    'Bathrooms',
    min_value = 1,
    max_value = 10,
    value = 2
)
parking_spaces = st.number_input(
    'Parking spaces',
    min_value = 0,
    max_value = 10,
    value = 2
)
land_unknown = st.checkbox('Land size is unknown')
land_size_sqm = st.number_input(
    'Land size (square metres)',
    min_value = 1.0,
    max_value = 5000.0,
    value = 600.0,
    disabled = land_unknown
)
submitted = st.button('Predict sale price', type = 'primary')

if submitted:
    land_value = np.nan if land_unknown else land_size_sqm
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'parking_spaces': [parking_spaces],
        'land_size_sqm': [land_value],
        'sale_year': [sale_date.year],
        'sale_month': [sale_date.month],
        'total_rooms': [bedrooms + bathrooms],
        'land_per_bedroom': [land_value / bedrooms],
        'suburb': [suburb],
        'sale_method': [sale_method]
    })

    prediction = bundle['model'].predict(
        input_data[bundle['feature_columns']]
    )[0]

    st.metric('Estimated sale price', f'${prediction:,.0f}')
    st.caption(
        'This estimate is based on a sample of disclosed historical sales '
        'and is not a professional property valuation.'
    )
