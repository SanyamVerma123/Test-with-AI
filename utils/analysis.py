import pandas as pd
import numpy as np

def perform_analysis(df):
    """Perform technical analysis and return recommendations"""
    analysis = {}
    
    # Trend Analysis
    current_price = df['Close'].iloc[-1]
    sma_20 = df['SMA_20'].iloc[-1]
    rsi = df['RSI'].iloc[-1]
    
    # Trend
    analysis['trend'] = 'Bullish' if current_price > sma_20 else 'Bearish'
    
    # RSI Analysis
    if rsi > 70:
        analysis['rsi_signal'] = 'Overbought'
    elif rsi < 30:
        analysis['rsi_signal'] = 'Oversold'
    else:
        analysis['rsi_signal'] = 'Neutral'
    
    # MACD Analysis
    macd = df['MACD_diff'].iloc[-1]
    analysis['macd_signal'] = 'Buy' if macd > 0 else 'Sell'
    
    return analysis
