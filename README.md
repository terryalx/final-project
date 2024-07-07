# Con|nect.tech

Developed as part our ALX Software Engineering program fufilment requirement, Con|nect.tech is an online web platform that serves as a vibrant community for computer engineers and tech enthusiasts. Users can read and write informative blog posts on various topics related to hardware and software development. The platform fosters interaction and knowledge sharing through a well-organized tagging system and intuitive features.

## Features

1. User Authentication and Authorization:
    - Secure user registration with unique user ID.
    - Robust password hashing using industry-standard algorithms for enhanced security.
    - Session management with a login system for persistent user identification.
    - User profiles to update information (future implementation).

2. Blog Management:
    - User-friendly interface for creating and editing blog posts.
    - Rich text formatting capabilities for creating visually appealing content.
    - Tagging system to categorize posts under relevant topics (e.g., embedded engineering, devops, cybersecurity).
    - Ability to filter posts by tags for efficient topic exploration.
    - Display of most recently created posts on the main page

3. Interaction (Future Implementation):
    - Commenting system to enable user interaction on posts.

## Development Stack

- Languages: Python, JavaScript
- Frameworks/Libraries: Django, Bootstrap
- Database: MySQL

## Compatibility

Con|nect.tech is compatible with:

Operating Systems: Linux, macOS
Web Browsers: Google Chrome, Mozilla Firefox, Microsoft Edge

Note: Please ensure that you have the latest version of Python installed before proceeding with the setup instructions.

## Setup Instructions

1. Prerequisites:
    - Python
    - MySQL Database

2. Clone Repository: Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/terryalx/final-project.git
    ```

3. Create Virtual Environment: It's highly recommended to create a virtual environment to isolate project dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
    ```


4. Install Dependencies: Install required dependencies from requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```


5. Database Configuration:
    - Create a database and user with appropriate permissions.
    - Configure database connection details in `website/settings.py`.


6. Run Migrations: Apply database migrations to create the necessary tables:

    ```bash
    python manage.py migrate
    ```


8. Start Development Server: Launch the Django development server to run the application locally:

    ```bash
    python manage.py runserver
    ```

## Contributors

We welcome contributions from the community to enhance Con|nect.tech. The following individuals have contributed to the project:

- [Terry](https://github.com/terryalx)
- [Motun Ajirotutu](https://github.com/Motunblue)

If you would like to contribute to Con|nect.tech, please fork the repository and submit a pull request with your changes.
