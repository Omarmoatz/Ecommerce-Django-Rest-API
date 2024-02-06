# Ecommerce-Django-Rest-API

Ecommerce-Django-Rest-API is a Django project focused on building a RESTful API for an e-commerce application. The project aims to provide functionality for user authentication, product management, and order processing.

## Technologies Used

The following technologies have been utilized in the development of the Ecommerce-Django-Rest-API:

- **Python**: The core programming language used for building the backend logic and handling server-side operations.
- **Django**: A high-level Python web framework that provides a robust set of tools and libraries for building web applications. Django is used for handling URL routing, managing database models, and implementing business logic.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs, enabling the creation of RESTful APIs to support frontend interactions.
- **PostgreSQL**: An open-source relational database management system used for storing and retrieving data related to users, products, and orders.
- **Postman**: A popular API development and testing tool used for testing and debugging the API endpoints.
- **CRUD Operations**: The project includes Create, Read, Update, and Delete (CRUD) operations, allowing users to perform essential operations on the resources.
- **Authentication**: User authentication is implemented using Django's built-in authentication system or third-party libraries such as Django-REST-Auth or JWT (JSON Web Tokens).
- **Product Management**: The API supports operations related to managing products, such as creating new products, retrieving product details, updating product information, and deleting products.
- **Order Processing**: The API provides endpoints for creating new orders, retrieving order details, updating order status, and managing order-related operations.
- **Python Packages**: The project may utilize various Python packages and libraries to enhance functionality and improve development efficiency.

## Installation

To set up and run the Ecommerce-Django-Rest-API locally, follow these steps:

1. Clone the repository using the following command:

   ```
   git clone https://github.com/Omarmoatz/Ecommerce-Django-Rest-API.git
   ```

2. Navigate to the project directory:

   ```
   cd Ecommerce-Django-Rest-API
   ```

3. Create a virtual environment to isolate the project's dependencies:

   ```
   python3 -m venv myenv
   ```

4. Activate the virtual environment:

   - For Linux/Mac:

     ```
     source myenv/bin/activate
     ```

   - For Windows:

     ```
     myenv\Scripts\activate
     ```

5. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set up the database by running the migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Open your web browser or use Postman to access the API endpoints at `http://localhost:8000` or as specified in the project configuration.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

We would like to express our gratitude to the open-source community and the developers of the technologies used in this project. Their contributions and efforts are greatly appreciated.