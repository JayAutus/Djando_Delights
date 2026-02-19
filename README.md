# Django Delights

A restaurant management application built with Django that helps track inventory, menu items, recipes, and sales.

## Features

- **User Authentication**: Secure login/logout system - users must be authenticated to access the application
- **Dashboard**: Real-time view of inventory cost, revenue, profit, and key metrics
- **Ingredient Management**: Add, update, and track ingredient quantities and prices
- **Menu Management**: Create menu items with pricing
- **Recipe Requirements**: Define ingredient requirements for each menu item
- **Purchase Recording**: Record customer purchases with automatic inventory updates
- **Inventory Validation**: Only allow purchases when sufficient ingredients are available

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JayAutus/Djando_Delights.git
cd Djando_Delights
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. (Optional) Populate the database with sample data:
```bash
python manage.py populate_db
```

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your browser and navigate to `http://localhost:8000`

3. Login with your credentials (or use `admin`/`admin123` if you ran `populate_db`)

4. Explore the application:
   - View and manage ingredients in the inventory
   - Create menu items and their recipes
   - Record customer purchases
   - Monitor revenue and profit on the dashboard

## Default Login (if using populate_db)

- Username: `admin`
- Password: `admin123`

## Project Structure

```
djangodelights/         # Main project settings
inventory/              # Main application
  ├── models.py         # Data models (Ingredient, MenuItem, RecipeRequirement, Purchase)
  ├── views.py          # View logic
  ├── forms.py          # Form definitions
  ├── urls.py           # URL routing
  ├── templates/        # HTML templates
  └── static/           # CSS and static files
```

## Technologies Used

- Python 3.12
- Django 6.0.2
- SQLite (database)
- HTML/CSS

## License

This is a capstone project from Codecademy's Django course.
