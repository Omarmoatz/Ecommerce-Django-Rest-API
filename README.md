# Dj-Amazon-Clone

Dj-Amazon-Clone is an Amazon clone web application built using Python, Django, Django REST Framework, and JavaScript. It aims to replicate the core functionality and user experience of the popular e-commerce platform, Amazon.

## Technologies Used

The following technologies have been utilized in the development of Dj-Amazon-Clone:

- **Python**: The core programming language used for building the backend logic and handling server-side operations.
- **Django**: A high-level Python web framework that provides a robust set of tools and libraries for building web applications. Django is used for handling URL routing, managing database models, and implementing business logic.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs, enabling the creation of RESTful APIs to support frontend interactions.
- **JavaScript**: Used for client-side interactivity and enhancing the user experience.
- **HTML**: The markup language used for structuring the web pages and defining the content.
- **CSS**: Cascading Style Sheets are used for styling the web pages and defining the visual presentation.
- **Postman**: A popular API development and testing tool used for testing and debugging the API endpoints.
- **SQLite**: A lightweight and serverless database engine used for development and testing purposes.


## Installation

To set up and run Dj-Amazon-Clone locally, follow these steps:

1. Clone the repository using the following command:

   ```
   git clone https://github.com/Omarmoatz/Dj-Amazon-Clone.git
   ```

2. Navigate to the project directory:

   ```
   cd Dj-Amazon-Clone
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

8. Open your web browser and access the application at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

We would like to express our gratitude to the open-source community and the developers of the technologies used in this project. Their contributions and efforts are greatly appreciated.