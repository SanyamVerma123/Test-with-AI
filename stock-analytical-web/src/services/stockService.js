import axios from 'axios';

const API_URL = 'https://api.example.com/stocks'; // Replace with the actual API URL

export const fetchStockData = async (symbol) => {
    try {
        const response = await axios.get(`${API_URL}/${symbol}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching stock data:', error);
        throw error;
    }
};