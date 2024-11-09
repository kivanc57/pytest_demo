# Pytest Testing 🧪

This repository provides a comprehensive testing suite for validating geometric shapes, mathematical functions, and a fictional Hogwarts-themed classroom model. With a set of pre-defined tests, mocks, and parameterizations, this project demonstrates extensive testing using `Pytest`.

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## Table of Contents
- [🏗️ Project Structure](#project-structure)
- [🚀 Installation](#installation)
- [🛠️ Usage and Execution](#usage-and-execution)
- [🔬 Testing Components](#testing-components)
- [🔎 Sample Code and Fixtures](#sample-code-and-fixtures)
- [🧩 Notes](#notes)
- [⚙️ Requirements](#requirements)
- [🤝 Contributing](#contributing)
- [📜 License](#license)
- [📬 Contact](#contact)

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

# 🏗️ Project Structure <a id="project-structure"></a>
```markdown
📁 project-root
├── 📁 source
│ ├── 📄 __init__.py
│ ├── 📄 functions.py
│ ├── 📄 school.py
│ ├── 📄 service.py
│ └── 📄 shapes.py
│
├── 📁 tests
│ ├── 📄 __init__.py
│ ├── 📄 conftest.py
│ ├── 📄 test_Circle.py
│ ├── 📄 test_functions.py
│ ├── 📄 test_Rectangle.py
│ ├── 📄 test_school.py
│ ├── 📄 test_service.py
│ └── 📄 test_Square.py
│
├── 📄 .gitignore
├── 📄 .gitattributes
├── 📄 requirements.txt
└── 📄 test_commands.txt
```

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 🚀 Installation <a id="installation"></a>

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kivanc57/pytest_testing
   cd pytest_testing
   ```

2. **Set up the virtual environment:**
    ``` python
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
    ``` python
    pip install -r requirements.txt
    ```

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 🛠️ Usage and Execution <a id="usage-and-execution"></a>
### Running Tests
The testing suite is built with Pytest and can be executed with various options:

Run all tests:
``` bash
pytest
```

Run tests with verbose output:
``` bash
pytest -v
```

Run specific tests (e.g., slow tests):
``` bash
pytest -m slow
```

### Mock Tests
Mocks are utilized in this project to simulate external calls (e.g., API requests) and avoid dependencies on real databases or services.

### Parameterized Tests
This project also employs parameterized testing for the shapes module, allowing multiple test cases with different inputs.

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 🔬 Testing Components <a id="testing-components"></a>
### **Shapes Module Tests**
 Tests cover various shapes, including:

- 🔷 **Rectangle** 🔷
  
  Validates `area()` and `perimeter()` methods, ensuring correct calculations.

- 🔴 **Circle** 🔴

  Checks `area()` and `perimeter()` for circular dimensions.


- 🟩 **Square** 🟩

  Uses parameterized testing to validate multiple `side_length`s.

### Classroom Module Tests
Simulates a Hogwarts-style classroom:

- 🏫 **Classroom Initialization** 🏫

  Ensures teacher and students are correctly assigned.

- 👨🏻‍🎓 **Student Addition and Removal** 👨🏻‍🎓
  
  Tests adding/removing students and handles maximum capacity constraints.

- 👩🏻‍🏫 **Teacher Assignment** 👩🏻‍🏫
  
  Validates the teacher's assignment and reassignment.

### Mocked Tests
Uses unittest.mock to:

* **Mock Database Calls**: Validates responses from database functions without actual database dependencies.

* **Mock API Calls**: Tests API calls and error handling without hitting real endpoints.

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 🔎 Sample Code and Fixtures <a id="sample-code-and-fixtures"></a>
- **Fixtures for Reusable Test Objects**: Fixtures in conftest.py help set up reusable test objects for shapes and the classroom environment. One of them is below:

``` python
# conftest.py
@pytest.fixture
def test_rectangle():
    return shapes.Rectangle(length=10, width=20)
```

💡 **Example Test Cases**
* Testing add function
``` python
def test_add():
    result = functions.add(number_one=1, number_two=4)
    assert result == 5
```

* Testing classroom initialization
``` python
def test_classroom_initialization(hogwarts_classroom):
    assert hogwarts_classroom.teacher.name == "Minerva McGonagall"
    assert len(hogwarts_classroom.students) == 5
```

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

### 🧩 Notes <a id="notes"></a>
* Skip Tests:
  Some tests are marked as `@pytest.mark.skip` if a feature is broken or in development.

* Expected Failures:
  `@pytest.mark.xfail` marks tests that are expected to fail under certain conditions.


─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## ⚙️ Requirements <a id="requirements"></a>
* Python 3.7+
* Pytest
* Mock (for testing API/database dependencies)
* Requirements specified in `requirements.txt`

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 🤝 Contributing <a id="contributing"></a>
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 📜 License <a id="license"></a>
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](https://github.com/kivanc57/pytest_testing/blob/main/LICENSE) file for details.

─── ⋆⋅☆⋅⋆ ─────────────────────────────────────────────────────

## 📬 Contact <a id="contact"></a>

For any inquiries or contributions, please feel free to reach out.
- **GitHub Profile**: [kivanc57](https://github.com/kivanc57)
- **Email**: [kivancgordu@hotmail.com](mailto:kivancgordu@hotmail.com)
