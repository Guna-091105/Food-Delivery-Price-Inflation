import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Food Delivery Price Inflation",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Load data
# -----------------------------
DATA_PATH = Path(__file__).parent / "Task1" / "food_delivery_price_inflation_cleaned.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

df = load_data()

# -----------------------------
# Header
# -----------------------------
st.title("🍔 Food Delivery Price Inflation")
st.markdown(
    "### Comparing dine-in prices with food delivery app prices"
)
st.caption(
    "Interactive data analytics dashboard built with Python, Pandas and Streamlit."
)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("🔎 Filters")

platforms = st.sidebar.multiselect(
    "Delivery Platform",
    options=sorted(df["delivery_platform"].dropna().unique()),
    default=sorted(df["delivery_platform"].dropna().unique()),
)

cities = st.sidebar.multiselect(
    "City",
    options=sorted(df["city"].dropna().unique()),
    default=sorted(df["city"].dropna().unique()),
)

cuisines = st.sidebar.multiselect(
    "Cuisine Type",
    options=sorted(df["cuisine_type"].dropna().unique()),
    default=sorted(df["cuisine_type"].dropna().unique()),
)

filtered = df[
    df["delivery_platform"].isin(platforms)
    & df["city"].isin(cities)
    & df["cuisine_type"].isin(cuisines)
].copy()

# -----------------------------
# Handle empty filters
# -----------------------------
if filtered.empty:
    st.warning("No records match the selected filters. Please change the filters.")
    st.stop()

# -----------------------------
# KPI calculations
# -----------------------------
avg_inflation = filtered["price_inflation"].mean()
avg_dine_in = filtered["dine_in_price"].mean()
avg_app = filtered["app_price"].mean()
inflated_pct = (
    filtered["inflation_flag"].eq("Inflated Price").mean() * 100
)

# -----------------------------
# KPI cards
# -----------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Average Inflation", f"₹{avg_inflation:.2f}")
c2.metric("Avg. Dine-in Price", f"₹{avg_dine_in:.2f}")
c3.metric("Avg. App Price", f"₹{avg_app:.2f}")
c4.metric("Items With Inflation", f"{inflated_pct:.1f}%")

st.divider()

# -----------------------------
# Charts
# -----------------------------
left, right = st.columns(2)

with left:
    platform_df = (
        filtered.groupby("delivery_platform", as_index=False)["price_inflation"]
        .mean()
        .sort_values("price_inflation", ascending=False)
    )

    fig_platform = px.bar(
        platform_df,
        x="delivery_platform",
        y="price_inflation",
        title="Average Price Inflation by Platform",
        labels={
            "delivery_platform": "Delivery Platform",
            "price_inflation": "Average Inflation (₹)",
        },
        text_auto=".1f",
    )
    st.plotly_chart(fig_platform, use_container_width=True)

with right:
    city_df = (
        filtered.groupby("city", as_index=False)["price_inflation"]
        .mean()
        .sort_values("price_inflation", ascending=False)
    )

    fig_city = px.bar(
        city_df,
        x="city",
        y="price_inflation",
        title="Average Price Inflation by City",
        labels={
            "city": "City",
            "price_inflation": "Average Inflation (₹)",
        },
        text_auto=".1f",
    )
    st.plotly_chart(fig_city, use_container_width=True)

left, right = st.columns(2)

with left:
    cuisine_df = (
        filtered.groupby("cuisine_type", as_index=False)["price_inflation"]
        .mean()
        .sort_values("price_inflation", ascending=False)
    )

    fig_cuisine = px.bar(
        cuisine_df,
        x="cuisine_type",
        y="price_inflation",
        title="Average Price Inflation by Cuisine",
        labels={
            "cuisine_type": "Cuisine Type",
            "price_inflation": "Average Inflation (₹)",
        },
        text_auto=".1f",
    )
    st.plotly_chart(fig_cuisine, use_container_width=True)

with right:
    comparison = (
        filtered[["dine_in_price", "app_price"]]
        .mean()
        .rename({"dine_in_price": "Dine-in", "app_price": "Delivery App"})
        .reset_index()
    )
    comparison.columns = ["Price Type", "Average Price"]

    fig_price = px.bar(
        comparison,
        x="Price Type",
        y="Average Price",
        title="Average Dine-in vs App Price",
        labels={"Average Price": "Price (₹)"},
        text_auto=".2f",
    )
    st.plotly_chart(fig_price, use_container_width=True)

# -----------------------------
# Discount analysis
# -----------------------------
st.subheader("💸 Discount Analysis")

discount_df = filtered[
    ["discount_shown", "actual_discount_percent", "price_inflation"]
].copy()

d1, d2, d3 = st.columns(3)
d1.metric("Average Discount Shown", f"{discount_df['discount_shown'].mean():.1f}%")
d2.metric(
    "Average Actual Discount",
    f"{discount_df['actual_discount_percent'].mean():.1f}%"
)
d3.metric(
    "Average Inflation",
    f"₹{discount_df['price_inflation'].mean():.2f}"
)

st.info(
    "The dataset compares the advertised discount with the actual price difference "
    "between the dine-in and app prices. A negative actual discount percentage can "
    "occur when the app price is higher than the dine-in price."
)

# -----------------------------
# Data table
# -----------------------------
st.subheader("📋 Filtered Dataset")

display_columns = [
    "restaurant_name",
    "food_item",
    "dine_in_price",
    "app_price",
    "discount_shown",
    "delivery_platform",
    "city",
    "cuisine_type",
    "price_inflation",
    "actual_discount_percent",
    "inflation_flag",
]

st.dataframe(
    filtered[display_columns],
    use_container_width=True,
    hide_index=True,
)

# -----------------------------
# Insights
# -----------------------------
st.subheader("💡 Key Insights")

top_platform = (
    filtered.groupby("delivery_platform")["price_inflation"]
    .mean()
    .idxmax()
)
top_city = (
    filtered.groupby("city")["price_inflation"]
    .mean()
    .idxmax()
)
top_cuisine = (
    filtered.groupby("cuisine_type")["price_inflation"]
    .mean()
    .idxmax()
)

st.markdown(
    f"""
- Customers pay an average of **₹{avg_inflation:.2f} more** per item through the delivery-app price in the filtered data.
- **{top_platform}** has the highest average price inflation among the selected platforms.
- **{top_city}** has the highest average inflation among the selected cities.
- **{top_cuisine}** has the highest average inflation among the selected cuisines.
- The dashboard allows users to compare pricing patterns interactively instead of relying only on static charts.
"""
)

st.subheader("💼 Business Recommendation")
st.markdown(
    """
Customers should compare the dine-in price with the final delivery-app price
before ordering. Delivery platforms and restaurants can also use this analysis
to understand how pricing, discounts and customer perception interact.
"""
)

st.caption("Food Delivery Price Inflation | Data Analytics Portfolio Project")
