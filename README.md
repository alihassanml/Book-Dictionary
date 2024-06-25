# 📚 FastAPI Book Dictionary App

Welcome to the FastAPI Book Dictionary App! This project is designed to help you manage a collection of books with ease. You can store book titles, descriptions, and ratings, and perform all the essential CRUD (Create, Read, Update, Delete) operations. The app uses SQLAlchemy for database management and FastAPI for creating a modern, fast (high-performance) web framework.

## 🚀 Features

- **Add New Books**: Easily add a new book with its title, description, and rating.
- **View All Books**: Retrieve a list of all books in the collection.
- **View Book Details**: Get detailed information about a specific book using its ID.
- **Update Book Information**: Update the details of an existing book.
- **Delete Books**: Remove a book from the collection by its ID.

## 🛠️ Built With

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **SQLite**: A C library that provides a lightweight, disk-based database.

## 📦 Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

Make sure you have Python 3.7+ installed.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-book-dictionary-app.git
   cd fastapi-book-dictionary-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

By default, the app uses SQLite. If you prefer a different SQL database, update the SQLALCHEMY_DATABASE_URL in `main.py`.

### Running the App

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by Swagger UI.

## 🔧 Usage

Here are some example endpoints you can use:

- **Create a new book:**
  
  `POST /books/`
  ```json
  {
    "title": "The Great Gatsby",
    "description": "A novel written by American author F. Scott Fitzgerald.",
    "rating": 9.2
  }
  ```

- **Retrieve all books:**

  `GET /books/`

- **Retrieve a single book by ID:**

  `GET /books/{book_id}`

- **Update a book:**

  `PUT /books/{book_id}`
  ```json
  {
    "title": "The Great Gatsby",
    "description": "An updated description.",
    "rating": 9.5
  }
  ```

- **Delete a book:**

  `DELETE /books/{book_id}`

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Your Name - [your.email@example.com](alihassanbscs@gmail.com)

Project Link: [https://github.com/alihassanml/fastapi-book-dictionary-app](https://github.com/alihassanml/fastapi-book-dictionary-app)

---

*Made with ❤️ by [Your Name](https://github.com/alihassanml)*
```

Feel free to customize this README further based on your specific project details and preferences.
