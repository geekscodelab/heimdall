# Heimdall

**Version**: 0.1.0  
**Description**: Authentication & Authorization Service

## Authors

- **Milad Moslehikhou** - [milad.moslehikhou@gmail.com](mailto:milad.moslehikhou@gmail.com)
- **Hesam Ghasemi** - [s.hesam.ghasemi@gmail.com](mailto:s.hesam.ghasemi@gmail.com)

## License

This project is licensed under the MIT License.

---

## Requirements

### Python Version

- Python >= 3.10

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/geekscodelab/heimdall
cd heimdall
```

### Step 2: Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install poetry
poetry install
```

### Step 4: Run Migrations and Collect statics

```bash
python manage.py migrate
python3 manage.py collectstatic
```

### Step 5: Start the Development Server

```bash
python manage.py runserver
```

Access the application in your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Step 6: Access API Documentation

Heimdall uses **drf-spectacular** to provide OpenAPI 3.0-compliant schema documentation. The documentation can be
accessed at:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### Step 7: Coding Standards

This project uses the following tools to maintain code quality:

- **ruff**: Automatic code formatting and linting.

#### Running Linting and Formatting

```bash
# Check code quality
poetry run ruff check

# Fix code quality errors
poetry run ruff check --fix
```

### Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Run the following to set up development environment:
    ```bash
    pre-commit install
    pre-commit install --hook-type commit-msg
    ```
4. Commit your changes with clear and descriptive commit messages.
5. Submit a pull request for review.

### Support

If you encounter any issues or have questions, feel free to reach out to the authors:

- **Milad Moslehikhou** - [milad.moslehikhou@gmail.com](mailto:milad.moslehikhou@gmail.com)
- **Hesam Ghasemi** - [s.hesam.ghasemi@gmail.com](mailto:s.hesam.ghasemi@gmail.com)

