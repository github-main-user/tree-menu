# Tree Menu

This Django example app shows a way to render tree-structured menus using template tags.
Menus and their items are stored in the database and are editable via the Django admin panel.

## Features

- Active menu item is determined based on the current URL
- Menu structure is stored in the database
- Validates circular dependencies
- Supports multiple menus per page (identified by name)
- Supports both hardcoded and named Django URLs
- Each menu is rendered with exactly one database query

## Installation

1. Clone the repository:
```shell
git clone https://github.com/github-main-user/tree-menu.git
```

2. Enter the directory
```shell
cd tree-menu
```

3. Setup environment
```shell
cp .env.example .env
```

4. Install dependencies
```shell
poetry install --no-root
```

## Usage

5. Apply migrations
```shell
python manage.py migrate
```

6. Create a super user
```shell
python manage.py createsuperuser
```

For demonstration purposes some sample data has been prepared in fixtures.
To load fixtures:
```shell
python manage.py loaddata fixtures.json
```

7. Start the project
```shell
python manage.py runserver
```
