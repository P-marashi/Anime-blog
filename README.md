# Simple Django Anime Site Project

This is a simple Django project for an **anime website**, showcasing the use of **HTML** and **CSS**.

## Features

- Django framework for web development.
- HTML templates for the website structure.
- CSS stylesheets for the visual presentation.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/P-marashi/Anime-blog.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the Django project and database:
   - Make database migrations: `python manage.py makemigrations`
   - Apply database migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`
5. Access the site in your browser at `http://localhost:8000`.

## Project Structure

The project has the following structure:

- `manage.py`: Django project management script.
- `blog/`: Django app for the **anime blog functionality**.
  - `models.py`: Defines the database models for the blog.
  - `views.py`: Contains the views for handling requests and rendering templates.
  - `templates/`: HTML templates for rendering the web pages.
  - `static/`: Static files such as CSS stylesheets and images.
- `...` (Other project files and directories)

## Usage

This project provides a simple anime site with **blog functionality**. You can browse and read anime-related articles, view anime details, and navigate through different sections of the site.

Feel free to explore the code, modify it, and customize the project to fit your needs.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).

---

Please make sure to replace `<repository_url>` in the "Getting Started" section with the actual URL of your repository.
