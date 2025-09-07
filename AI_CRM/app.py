import streamlit as st
import pandas as pd

# Load CRM dataset
df = pd.read_csv("crm_data.csv")

st.title("🤖 AI-Enhanced CRM Insights")

# Show dataset
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Show segmentation summary
st.subheader("📊 Customer Segments")
if "segment" in df.columns:
    st.write(df["segment"].value_counts())
else:
    st.warning("Run segmentation code in notebook first to add 'segment' column.")

# Show churn risk customers
st.subheader("⚠️ Customers At Risk of Churn")
if "churn_probability" in df.columns:
    st.write(df[df["churn_probability"] > 0.6][["customer_id", "company_name", "churn_probability"]])
else:
    st.warning("Run churn prediction code in notebook first to add 'churn_probability' column.")

# Simple chatbot-like query system
st.subheader("💬 Ask CRM Assistant")
query = st.text_input("Type your question (e.g., 'show high value customers')")

if query:
    query = query.lower()
    if "high value" in query:
        if "segment" in df.columns:
            st.write(df[df["segment"] == "High Value"][["customer_id", "company_name", "segment"]])
        else:
            st.warning("Segmentation not available.")
    elif "at risk" in query or "churn" in query:
        if "churn_probability" in df.columns:
            st.write(df[df["churn_probability"] > 0.6][["customer_id", "company_name", "churn_probability"]])
        else:
            st.warning("Churn prediction not available.")
    else:
        st.write("Sorry, I didn't understand. Try asking about 'high value' or 'churn'.")
