
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the DataFrame
df = pd.read_csv('sales_data.csv')

# Streamlit Dashboard
st.title("Sales Dashboard")
st.write("## Sales Data Overview")
st.dataframe(df)


# Display Summary Statistics
st.write("## Summary Statistics")
st.write(df.describe())

# Visualizations
st.write("## Visualizations")

st.write("### Total Price by Item")
total_price_by_item = df.groupby('Item Name')['Total Price'].sum().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(data=total_price_by_item, x='Item Name', y='Total Price', ax=ax2)
ax2.set_title("Total Price by Item")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig2)

st.write("### Top Items by Total Price")
top_items = df.groupby('Item Name')['Total Price'].sum().nlargest(10).reset_index()
fig5, ax5 = plt.subplots()
sns.barplot(data=top_items, x='Item Name', y='Total Price', ax=ax5)
ax5.set_title("Top Items by Total Price")
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig5)

