import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
data=pd.read_csv('C:\\Users\\A ONE COMPUTER\\OneDrive\\Desktop\\python_sm\\pandas\\apple_products.csv')
#print(data.head())
#print(data.describe())
#print(data.isnull().sum())

highest_rated=data.sort_values(by=["Sale Price"], ascending=False) 
highest_rated=highest_rated.head(10)
#print(highest_rated['Product Name'])
iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
count=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated, x=label, y=count, title="No. Highest Rated iPhones")
figure.show()


iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
count=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated, x=label, y=count, title="No. of  Highest reviewed iPhones")
figure.show()

figure=px.scatter(data_frame=highest_rated, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Ratings vs Sale Price")
figure.show() 

figure=px.scatter(data_frame=highest_rated, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Discount percentage vs Sale Price")
figure.show()


# Top 10 Most Expensive iPhones

most_expensive = data.sort_values(
    by="Sale Price",
    ascending=False
).head(10)

fig = px.bar(
    most_expensive,
    x="Product Name",
    y="Sale Price",
    color="Sale Price",
    title="Top 10 Most Expensive iPhones"
)

fig.update_layout(
    xaxis_title="Product Name",
    yaxis_title="Sale Price"
)

fig.show()

# Extract storage capacity

data["Storage"] = data["Product Name"].str.extract(
    r'(\d+\s?GB)'
)

avg_rating_storage = data.groupby(
    "Storage"
)["Star Rating"].mean().reset_index()

fig = px.bar(
    avg_rating_storage,
    x="Storage",
    y="Star Rating",
    color="Star Rating",
    title="Average Rating by Storage Capacity"
)

fig.update_layout(
    xaxis_title="Storage Capacity",
    yaxis_title="Average Rating"
)

fig.show()

import plotly.figure_factory as ff

corr_data = data[
    [
        "Sale Price",
        "Mrp",
        "Discount Percentage",
        "Number Of Ratings",
        "Number Of Reviews",
        "Star Rating"
    ]
]

corr_matrix = corr_data.corr()

fig = ff.create_annotated_heatmap(
    z=corr_matrix.values,
    x=list(corr_matrix.columns),
    y=list(corr_matrix.index),
    annotation_text=np.round(
        corr_matrix.values,
        2
    ),
    showscale=True
)

fig.update_layout(
    title="Correlation Heatmap"
)

fig.show()

# Top 10 Most Reviewed Products

top_reviewed = data.sort_values(
    by="Number Of Reviews",
    ascending=False
).head(10)

fig = px.bar(
    top_reviewed,
    x="Product Name",
    y="Number Of Reviews",
    color="Number Of Reviews",
    title="Top 10 Most Reviewed iPhones"
)

fig.show()