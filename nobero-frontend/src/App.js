import React from 'react';
import './App.css'; // Import your CSS file for styling

function App() {
  // Manually defined product data
  const products = [
    {
      title: 'Product 1',
      price: 199.99,
      mrp: 249.99,
      last_7_day_sale: '10% off',
      fit: 'Regular',
      fabric: 'Cotton',
      neck: 'Round Neck',
      sleeve: 'Short Sleeve',
      pattern: 'Solid',
      length: 'Regular',
      description: 'A comfortable and stylish t-shirt.',
      imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST4XrcpfJC1omvBC_VXaGIIYA9U_1v0YU-Bw&s', // Replace with your image URL
    }
  ];

  return (
    <div className="App">
      <h1 className="header">Products</h1>
      <div className="product-list">
        {products.map((product, index) => (
          <div className="product-card" key={index}>
            <img src={product.imageUrl} alt={product.title} className="product-image" />
            <h2 className="product-title">{product.title}</h2>
            <p className="product-price">Price: ${product.price.toFixed(2)}</p>
            <p className="product-mrp">MRP: ${product.mrp.toFixed(2)}</p>
            <p className="product-sale">Sale: {product.last_7_day_sale}</p>
            <p className="product-fit">Fit: {product.fit}</p>
            <p className="product-fabric">Fabric: {product.fabric}</p>
            <p className="product-neck">Neck: {product.neck}</p>
            <p className="product-sleeve">Sleeve: {product.sleeve}</p>
            <p className="product-pattern">Pattern: {product.pattern}</p>
            <p className="product-length">Length: {product.length}</p>
            <p className="product-description">{product.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
