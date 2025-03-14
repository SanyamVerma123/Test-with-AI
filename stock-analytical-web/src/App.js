import React, { useEffect, useState } from 'react';
import StockChart from './components/StockChart';
import { fetchStockData } from './services/stockService';

const App = () => {
    const [stockData, setStockData] = useState(null);
    const [symbol, setSymbol] = useState('AAPL'); // Default stock symbol

    useEffect(() => {
        const getStockData = async () => {
            const data = await fetchStockData(symbol);
            setStockData(data);
        };

        getStockData();
    }, [symbol]);

    return (
        <div>
            <h1>Stock Analytical Web</h1>
            <input 
                type="text" 
                value={symbol} 
                onChange={(e) => setSymbol(e.target.value)} 
                placeholder="Enter stock symbol" 
            />
            {stockData && <StockChart data={stockData} />}
        </div>
    );
};

export default App;