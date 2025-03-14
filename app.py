import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.indicators import calculate_indicators
from utils.analysis import perform_analysis

st.set_page_config(
    page_title="Stock Analysis Tool",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

def main():
    if not st.session_state['login_status']:
        col1, col2 = st.columns([1, 1])
        with col1:
            username = st.text_input("Username")
        with col2:
            password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "admin":  # Replace with secure authentication
                st.session_state['login_status'] = True
                st.experimental_rerun()
        return

    st.title("📈 Premium Stock Analysis Tool")
    
    # Sidebar
    st.sidebar.header("Configuration")
    symbol = st.sidebar.text_input("Stock Symbol", "AAPL")
    period = st.sidebar.selectbox("Time Period", 
                                ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if symbol:
            # Fetch data
            stock = yf.Ticker(symbol)
            df = stock.history(period=period)
            
            # Calculate indicators
            df = calculate_indicators(df)
            
            # Create interactive chart
            fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
            
            st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        if symbol:
            info = stock.info
            st.subheader("Stock Info")
            st.write(f"Company: {info.get('longName', symbol)}")
            st.write(f"Sector: {info.get('sector', 'N/A')}")
            st.write(f"Market Cap: ${info.get('marketCap', 0):,.2f}")
            
            # Technical Analysis
            analysis = perform_analysis(df)
            st.subheader("Technical Analysis")
            st.write(analysis)

try:
    if __name__ == "__main__":
        main()
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.error("Please try again later or contact support.")
