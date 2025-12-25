# Contributor Guidelines for python-nocobase

Welcome to python-nocobase! We're excited that you want to contribute to our open-source project. Please take a moment to read and follow these guidelines to ensure a smooth and collaborative development process.

## Table of Contents

- [Getting Started](#getting-started)
- [Contribution Process](#contribution-process)
  - [1. Fork the Repository](#1-fork-the-repository)
  - [2. Set Up Development Environment](#2-set-up-development-environment)
  - [3. Create a Branch](#3-create-a-branch)
  - [4. Work on Your Contribution](#4-work-on-your-contribution)
  - [5. Test Your Code](#5-test-your-code)
  - [6. Commit Your Changes](#6-commit-your-changes)
  - [7. Create a Pull Request](#7-create-a-pull-request)
- [Coding Guidelines](#coding-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Reporting Issues](#reporting-issues)
- [Authors](#authors)

## Getting Started

Before contributing, please:
1. Read this entire document
2. Check existing [issues](https://github.com/ueki-kazuki/python-nocobase/issues) and [pull requests](https://github.com/ueki-kazuki/python-nocobase/pulls)
3. Consider opening an issue to discuss your proposed changes before starting work

## Contribution Process

To contribute to this project, follow these steps:

### 1. Fork the Repository

Click the "Fork" button on the top right corner of the repository's page on GitHub. This will create a copy of the repository in your GitHub account.

### 2. Set Up Development Environment

Clone your forked repository and set up the development environment:

```bash
git clone https://github.com/your-username/python-nocobase.git
cd python-nocobase

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in development mode
pip install -e .

# Install development dependencies (if you have them)
pip install pytest pytest-cov black flake8
```

### 3. Create a Branch

Create a new branch for your contribution. Name your branch in a descriptive manner that reflects the purpose of your contribution.

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
# or
git checkout -b docs/documentation-update
```

### 4. Work on Your Contribution

Now you can start working on your contribution. Be sure to follow the coding guidelines (mentioned below) and implement your changes or new features.

### 5. Test Your Code

Thoroughly test your code to ensure it works as expected:

```bash
# Run existing tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=nocobase

# Run specific test files
python -m pytest nocobase/api_test.py
python -m pytest nocobase/nocobase_test.py
```

Make sure to write unit tests for new functionality. Your contribution should not introduce new bugs or regressions.

### 6. Commit Your Changes

Once you are satisfied with your work, commit your changes. Be sure to write clear and descriptive commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) format:

```bash
git add .
git commit -m "feat: add support for collection field management"
# or
git commit -m "fix: handle empty response in list method"
# or
git commit -m "docs: update API reference for new methods"
```

### 7. Create a Pull Request

When your code is ready for review, push your changes to your forked repository, and then open a Pull Request (PR) to the main repository's `main` branch:

```bash
git push origin feature/your-feature-name
```

In your PR description, provide:
- A clear and detailed explanation of your contribution
- What the change does and why it is needed
- Any breaking changes
- Screenshots or examples if applicable
- Reference to related issues (e.g., "Closes #123")

Our team will review your PR, provide feedback, and merge it when it meets our quality and functionality standards.

## Coding Guidelines

Please adhere to the following coding guidelines:

### Python Style
- Follow [PEP 8](https://pep8.org/) Python style guide
- Use [Black](https://black.readthedocs.io/) for code formatting: `black nocobase/`
- Use [flake8](https://flake8.pycqa.org/) for linting: `flake8 nocobase/`
- Maximum line length: 88 characters (Black default)

### Code Quality
- Write clean, readable, and well-documented code
- Keep code modular and DRY (Don't Repeat Yourself)
- Use meaningful variable and function names
- Include type hints where appropriate (following existing patterns)
- Follow the existing code structure and patterns

### Specific Guidelines
- Use `Optional[Type]` for optional parameters
- Use `List[Type]` and `Dict[str, Type]` for collections
- Prefer composition over inheritance
- Handle exceptions appropriately with custom exception classes
- Use docstrings for public methods and classes

### Example Code Style
```python
from typing import Optional, List, Dict

class ExampleClass:
    """Example class following project conventions."""
    
    def __init__(self, name: str, config: Optional[Dict[str, str]] = None):
        self.name = name
        self.config = config or {}
    
    def process_items(self, items: List[str]) -> List[str]:
        """Process a list of items and return processed results.
        
        Args:
            items: List of items to process
            
        Returns:
            List of processed items
        """
        return [item.strip().lower() for item in items if item]
```

## Testing

### Writing Tests
- Write unit tests for all new functionality
- Place tests in the same directory as the code being tested
- Use descriptive test names that explain what is being tested
- Follow the existing test patterns and structure

### Test Structure
```python
def test_function_name_expected_behavior():
    # Arrange
    input_data = {"key": "value"}
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result == expected_output
```

### Running Tests
```bash
# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=nocobase --cov-report=html

# Run specific test file
python -m pytest nocobase/api_test.py -v
```

## Documentation

Documentation is crucial for maintaining and improving our project. When you make a contribution, you should:

### Code Documentation
- Include docstrings for all public classes and methods
- Use clear and concise comments for complex logic
- Follow [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

### Project Documentation
- Update the README.md if you add or change features
- Update API examples if you modify the public interface
- Add or update usage examples for new functionality
- Keep the implementation status section current

### Documentation Example
```python
def create_collection(self, name: str, schema: Dict[str, Any]) -> Collection:
    """Create a new collection with the specified schema.
    
    Args:
        name: The name of the collection to create
        schema: Dictionary containing the collection schema definition
        
    Returns:
        Collection: The newly created collection instance
        
    Raises:
        NocoBaseAPIError: If the API request fails
        ValueError: If the schema is invalid
        
    Example:
        >>> client = NocoBaseRequestsClient(token, base_url)
        >>> schema = {"fields": [{"name": "title", "type": "string"}]}
        >>> collection = client.create_collection("my_table", schema)
    """
```

## Reporting Issues

### Bug Reports
When reporting bugs, please include:
- Python version and operating system
- NocoBase version you're connecting to
- Complete error messages and stack traces
- Minimal code example that reproduces the issue
- Expected vs actual behavior

### Feature Requests
When requesting features, please include:
- Clear description of the desired functionality
- Use case and motivation for the feature
- Proposed API design (if applicable)
- Willingness to contribute the implementation

### Issue Template
```markdown
**Bug Report / Feature Request**

**Description:**
Brief description of the issue or feature

**Environment:**
- Python version: 
- NocoBase version: 
- Operating System: 

**Steps to Reproduce:** (for bugs)
1. Step one
2. Step two
3. Step three

**Expected Behavior:**
What you expected to happen

**Actual Behavior:** (for bugs)
What actually happened

**Code Example:**
```python
# Minimal code example
```
```

## Authors

We appreciate all contributors to our project. To give credit where it's due, please add your name and GitHub username to the "Authors" section of the README if it's not already there.

Thank you for your interest in contributing to python-nocobase. We look forward to your contributions and collaborations. Happy coding!
