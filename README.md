# MStarSupply

**MStarSupply** is an inventory management system developed with Flask on the backend and React with Vite and Chakra UI on the frontend. It allows for managing products, including registering new items, tracking entries and exits, and displaying data in a user-friendly manner.

## Features

- **Products Registration:** Register new items in the inventory, including detailed information about each product.
- **Movement Management:** Track the entries and exits of products, with support for different types of movements.
- **User-Friendly Interface:** Use intuitive modals and forms, created with Chakra UI, to facilitate interaction with the system.
- **Themes:** Light/dark theme switching available in the Navbar.
- **Data Validation:** Client-side input validation to ensure data integrity.
- **Backend/Frontend Integration:** Efficient communication between the Flask backend and the React frontend using a REST API.

## Technologies Used

- **Frontend:** React.js, Vite, Chakra UI
- **Backend:** Flask, Python
- **Database:** SQLite

## Installation and Setup

1. **Clone the repository**:
```bash
git clone https://github.com/goncalvesfrederico/MStarSupply.git
cd MStarSupply
```

2. Set up the backend:
- Navigate to the backend folder and create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

- Install the dependencies:
```bash
pip install -r requirements.txt
```
- Start the Flask server:
```bash
flask run
```
3. **Set up the frontend**:
- Navigate to the frontend folder and install the dependencies:
```bash
npm install
```

- Start the development server:
```bash
npm run dev
```

4. **Access the application**:
Open your browser and go to http://localhost:3000 to view the interface frontend and http://127.0.0.1:5000/ on backend.

## Contribution

Contributions are welcome! Feel free to open issues and pull requests to improve MStarSupply.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.