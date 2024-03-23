import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [items, setItems] = useState('');
  const [total, setTotal] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/checkout', { items });
      setTotal(response.data.total);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ textAlign: 'center', margin: 'auto' }}>
      <h1>Supermarket Checkout</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <label htmlFor="items" style={{ marginBottom: '10px' }}>Enter items (e.g., AAB):</label>
        <input
          type="text"
          id="items"
          value={items}
          onChange={(e) => setItems(e.target.value)}
          placeholder="AAB"
          style={{ padding: '10px', width: '300px', marginBottom: '20px' }}
        />
        <button type="submit">Calculate Total</button>
      </form>
      {total !== '' && <h2>Total: ${total}</h2>}
    </div>
  );
}

export default App;