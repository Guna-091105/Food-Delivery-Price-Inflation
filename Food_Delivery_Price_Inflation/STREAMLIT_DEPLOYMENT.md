# Streamlit Web App

## Run locally

From the `Food_Delivery_Price_Inflation` project root:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app should open at:

```text
http://localhost:8501
```

## Deployment

Push the project to GitHub and deploy it using Streamlit Community Cloud.

When creating the app, select:

- Repository: your GitHub repository
- Branch: the branch containing `app.py`
- Main file path: `Food_Delivery_Price_Inflation/app.py`

If you move `app.py` to the repository root instead, use `app.py` as the main file path.

## Project structure

```text
Food_Delivery_Price_Inflation/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── Task1/
│   └── food_delivery_price_inflation_cleaned.csv
├── Task2/
├── Task3/
├── Task4/
└── Task5/
```
