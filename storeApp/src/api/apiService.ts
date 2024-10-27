import axios from 'axios';
// import { Product } from '';

const API_BASE_URL = 'https://web.bhors.com/api/items';

// Function to fetch all items
export const fetchAllItems = async (): Promise<Product[]> => {
  try {
    const response = await axios.get<Product[]>(API_BASE_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching all items:', error);
    throw error;
  }
};

// Function to fetch a single item by ID
export const fetchItemById = async (id: number): Promise<Product> => {
  try {
    const response = await axios.get<Product>(`${API_BASE_URL}/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching item with ID ${id}:`, error);
    throw error;
  }
};
