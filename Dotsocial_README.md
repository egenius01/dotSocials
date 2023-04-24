# Dotsocials

Dotsocials is a social media API built using Django and Django Rest Framework. It allows for user registration, token authentication, posting, commenting, liking, and reposting.

## Features

- User registration and authentication
- Token-based authentication
- Post creation, retrieval, updating, and deletion
- Comment creation, retrieval, updating, and deletion
- Like creation and deletion
- Repost creation and deletion
- User profile retrieval and updating

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/dotsocials.git
    ```

2. Create a virtual environment:

    ```
    python -m venv env
    ```

3. Activate the virtual environment:

    ```
    source env/bin/activate
    ```

4. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the migrations:

    ```
    python manage.py migrate
    ```

2. Create a superuser:

    ```
    python manage.py createsuperuser
    ```

3. Run the server:

    ```
    python manage.py runserver
    ```

4. Use the API at `http://localhost:8000/`.

## API Endpoints

- POST api/v1/users/register/ (user-register)
- GET/PUT/DELETE api/v1/userprofiles/<pk>/ (user-profile-detail)
- GET/POST api/v1/post/ (post-list)
- GET/PUT/DELETE api/v1/post/<pk>/ (post-detail)
- GET/POST api/v1/like/ (like-list)
- GET/PUT/DELETE api/v1/like/<pk>/ (like-detail)
- GET/POST api/v1/redot/ (redot-list)
- GET/PUT/DELETE api/v1/redot/<pk>/ (redot-detail)
- GET/POST api/v1/comment/ (comment-list)
- GET/PUT/DELETE api/v1/comment/<pk>/ (comment-detail)
- GET api/v1/ (api-root)
- POST api/token/ (token_obtain_pair)
- POST api/token/refresh/ (token_refresh)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
Feel free to modify it to suit your project's specific needs!
