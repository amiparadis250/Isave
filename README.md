# Expense Tracker & Saving Groups
A Django-based web application for tracking personal expenses and managing saving groups. Built with Django, GraphQL, PostgreSQL, and Cloudinary.

## Features
### Expense Tracker
- **User Authentication:** Sign up, log in, and manage your profile.
- **Expense Management:** Add, view, edit, and delete expenses.
- **Budgeting:** Set monthly budgets and receive alerts when approaching limits.
- **Categories and Tags:** Organize expenses with categories and custom tags.
- **Reports:** Generate monthly/yearly expense reports.

### Saving Groups
- **Create/Join Groups:** Create saving groups or join existing ones.
- **Group Contributions:** Track contributions from members.
- **Progress Tracking:** Visualize progress with a progress bar and milestones.
- **Notifications:** Receive alerts for contributions and goal completion.

### Additional Features
- **GraphQL API:** Flexible and efficient data querying.
- **Cloudinary Integration:** Store and manage media files (e.g., profile pictures).
- **PostgreSQL Database:** Reliable and scalable database for production.

## Technologies Used
- **Backend:** Django,Graphene-Django (GraphQL)
- **Database:** PostgreSQL
- **File Storage:** Cloudinary
- **Authentication:** Django’s built-in authentication system
- **Frontend:** (Optional) React, Vue.js, or any frontend framework.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Cloudinary account (for media storage)

## Setup Guide
### 1. Clone the Repository
```bash
git clone https://github.com/amiparadis250/Isave
cd Isave
```
### 2. Create and Activate Virtual Environment
```bash
pipenv install --dev
pipenv shell
```
### 3. Install Dependencies
```bash
pipenv install -r requirements.txt
```
### 4. Set Up PostgreSQL
Create a PostgreSQL database:
```sql
CREATE DATABASE expense_tracker;
```
Update `settings.py` with your database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'expense_tracker',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Set Up Cloudinary
Sign up for a Cloudinary account and update `settings.py` with your Cloudinary credentials:
```python
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create a Superuser
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```
Visit [http://localhost:8000](http://localhost:8000) to access the application.

## GraphQL API
The application provides a GraphQL API for querying and mutating data.
### Access GraphiQL
Visit [http://localhost:8000/graphql/](http://localhost:8000/graphql/) to interact with the GraphQL API.

#### Example Queries
**Fetch all expenses:**
```graphql
query {
  allExpenses {
    id
    amount
    category
    date
  }
}
```

**Fetch all saving groups:**
```graphql
query {
  allSavingGroups {
    id
    name
    targetAmount
    deadline
  }
}
```

## Project Structure
```
expense_tracker/
├── users/               # User authentication and profile management
├── expenses/            # Expense tracking and budgeting
├── savings/             # Saving groups and contributions
├── notifications/       # Notifications and alerts
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Environment Variables
Create a `.env` file in the root directory and add the following variables:
```env
DATABASE_URL='your_postgres_connection_string'
CLOUDINARY_URL='cloudinary://<api_key>:<api_secret>@<cloud_name>'
```

## Contributing
- Fork the repository.
- Create a new branch: `git checkout -b feature/your-feature-name`.
- Commit your changes: `git commit -m 'Add some feature'`.
- Push to the branch: `git push origin feature/your-feature-name`.
- Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, feel free to reach out:
- **Name:** ISHIMWE Ami Paradis
- **Email:** pishimweaime7@gmail.com
- **GitHub:** https://github.com/amiparadis250
- **Telephone:** +250791966291

Enjoy building and using the Expense Tracker & Saving Groups app! 🚀
