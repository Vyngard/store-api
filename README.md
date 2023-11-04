
# Simple RESTful API

Store API is a Flask-based RESTful API allowing basic operations 
on items, stores, tags, and users. It uses Flask's blueprint
pattern and integrates JWT authentication for secure access.  
For more documentation, You can find sufficient comments on the project. Also since we use Flask-Smorest, you can find the OpenAPI specification 
by running the project and visiting `http://127.0.0.1:5000/swagger-ui`

## Tools & Libraries Used

- Flask 2.2: Micro web framework for Python.
- Flask-Smorest: For automatic OpenAPI spec generation.
- SQLAlchemy: SQL toolkit and ORM for Python.
- Flask-SQLAlchemy 3.0.3: SQLAlchemy integration for Flask.
- Flask-JWT-Extended: Provides JWT support for Flask.
- Passlib: Password hashing library.

## Setting Up the Project

1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: 
    - For Linux/Mac: `source venv/bin/activate`
    - For Windows: `venv\Scripts\activate`
4. Install the required libraries: `pip install -r requirements.txt`
5. Set environment variables as required by `.flaskenv`.
6. Run the application: `flask run`

## API Endpoints
You can create a free account on [Postman.com](https://www.postman.com/) and
create these endpoints in your workspace to test the API. for that at the beginning of all the
following endpoints you must include `http://127.0.0.1:5000` which you can set as a variable 
for convenience.

### Items

- `GET /item/<int:item_id>`: Retrieve an item by its ID. Requires JWT authentication.
- `GET /item`: Retrieve all items. Requires JWT authentication.
- `POST /item`: Create a new item. Requires JWT authentication.
- `DELETE /item/<int:item_id>`: Delete an item by its ID. Requires JWT authentication.
- `PUT /item/<int:item_id>`: Update an item by its ID. Requires JWT authentication.

### Stores

- `GET /store/<int:store_id>`: Retrieve a store by its ID.
- `GET /store`: Retrieve all stores.
- `POST /store`: Create a new store.
- `DELETE /store/<int:store_id>`: Delete a store by its ID.

### Tags

- `GET /tag/<int:tag_id>`: Retrieve a tag by its ID.
- `GET /store/<int:store_id>/tag`: Retrieve all tags associated with a specific store by its ID.
- `POST /store/<int:store_id>/tag`: Add a new tag to a specific store.

### Users

- `GET /user/<int:user_id>`: Retrieve a user by its ID.
- `POST /register`: Register a new user.
- `DELETE /user/<int:user_id>`: Delete a user by its ID.
- `POST /login`: Login a user.
- `POST /logout`: Logout a user.
- `POST /refresh`: Refresh a user's access token.

## Docker Support

A `Dockerfile` is provided for containerizing the application. you can also sync your project folder
with the container volume so whenever you make a change, the program restarts automatically
so you don't have to do that manually. for that, first, create an image from dockerfile
```dockerfile
docker build -t store-api .
```
then you create a container with synced volume from that image
```dockerfile
docker run -dp 5000:5000 -w /app -v "${PWD}:/app" store-api
```
then you just have to use the endpoints either in Postman or in your browser
