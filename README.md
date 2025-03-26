# Post on Blog

This project is a blog post generator that creates blog content based on a given topic. The generated posts are saved to a database for later retrieval.

## Features

* **Generate Post** : Given a topic, the system generates a blog post and saves it to the database.
* **List Posts** : Retrieve and list all generated posts from the database.

## Technologies Used

* **Python** : Backend development.
* **FastAPI** : A modern web framework for building APIs quickly and efficiently.
* **SQLAlchemy** : ORM for handling database operations.
* **Docker** : Containerizes the application for easy deployment and portability.

## How to Run the Project Locally

1. Clone the repository:
   `git clone git@github.com:Matheus-mVilela/a-eight-post-blog-system.git`
2. Navigate to the project folder:
   `cd a-eight-post-blog-system`
3. Build Containers
   `make build`
4. Apply migrations:
   `make migration_upgrade_head`
5. Start the backend services:
   `make api`

* You can access the **API** at `http://localhost:8000/`.
* You can access the **Docs** at `http://localhost:8000/docs`.