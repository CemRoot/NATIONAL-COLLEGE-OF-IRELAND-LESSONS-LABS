# Contributing to NCI MSc AI Repository

Thank you for your interest in contributing to this academic repository! While this is primarily a personal project documenting my Master's coursework, I welcome contributions that enhance the learning experience for others.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring environment for all contributors. We expect all participants to:

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

### Academic Integrity

This repository contains coursework from an ongoing Master's program. Contributors must:

- **NOT** submit solutions to current assignments
- **NOT** provide complete answers to ongoing assessments
- Respect copyright and intellectual property
- Follow NCI's academic integrity policies

---

## 🤝 How Can I Contribute?

### Reporting Bugs

If you find a bug in the code:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear, descriptive title
   - Steps to reproduce the bug
   - Expected vs. actual behavior
   - Screenshots (if applicable)
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

1. **Check existing issues** for similar suggestions
2. **Open a new issue** describing:
   - The enhancement and its benefits
   - Possible implementation approach
   - Any relevant examples or references

### Code Contributions

You can contribute by:

- **Fixing bugs** reported in issues
- **Improving documentation** (README, comments, docstrings)
- **Optimizing code** (performance, readability)
- **Adding utilities** (helper functions, data preprocessing tools)
- **Enhancing visualizations** (better plots, interactive elements)
- **Writing tests** (unit tests, integration tests)

---

## 🚀 Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/NATIONAL-COLLEGE-OF-IRELAND-LESSONS-LABS.git
cd NATIONAL-COLLEGE-OF-IRELAND-LESSONS-LABS
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 4. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # If available
```

---

## 📝 Contribution Guidelines

### What to Contribute

✅ **DO**:
- Fix typos and improve documentation
- Optimize existing code
- Add helpful comments and docstrings
- Improve code readability
- Create reusable utility functions
- Add data visualization enhancements
- Write unit tests

❌ **DON'T**:
- Submit complete solutions to current assignments
- Include copyrighted materials without permission
- Add large binary files or datasets without discussion
- Make breaking changes without prior discussion

### Code Quality Standards

- **Python**: Follow PEP 8 style guidelines
- **Comments**: Write clear, meaningful comments
- **Docstrings**: Use Google or NumPy docstring format
- **Type Hints**: Include type hints where appropriate
- **Error Handling**: Add proper exception handling
- **Testing**: Write tests for new functionality

---

## 🎨 Style Guidelines

### Python Code Style

```python
# Good example
def calculate_accuracy(predictions: np.ndarray, labels: np.ndarray) -> float:
    """
    Calculate classification accuracy.

    Args:
        predictions: Model predictions array
        labels: Ground truth labels array

    Returns:
        Accuracy score between 0 and 1

    Raises:
        ValueError: If arrays have different lengths
    """
    if len(predictions) != len(labels):
        raise ValueError("Arrays must have the same length")

    correct = np.sum(predictions == labels)
    total = len(labels)
    return correct / total
```

### Documentation Style

- Use clear, concise language
- Include code examples where helpful
- Add links to relevant resources
- Use proper markdown formatting
- Include badges and visual elements

### Jupyter Notebook Style

- Clear markdown explanations before code cells
- Well-commented code
- Appropriate visualizations
- Clean output (run all cells before committing)
- Remove unnecessary cells

---

## 💬 Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(lab4): add data validation function

- Implemented input validation for dataset
- Added error handling for missing values
- Included unit tests

Closes #42
```

```bash
fix(ml-lab2): correct accuracy calculation

Fixed division by zero error in accuracy function
when predictions array is empty

Fixes #15
```

```bash
docs(readme): update installation instructions

- Added virtual environment setup
- Updated dependency list
- Added troubleshooting section
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update your fork** with the latest changes:
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Test your changes** thoroughly

3. **Update documentation** if needed

4. **Run code formatters** (if applicable):
   ```bash
   black your_file.py
   flake8 your_file.py
   ```

### Submitting the Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub with:
   - Clear, descriptive title
   - Detailed description of changes
   - Reference to related issues
   - Screenshots (if applicable)

3. **PR Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Motivation and Context
   Why is this change needed?

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code refactoring

   ## Testing
   How has this been tested?

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Documentation updated
   - [ ] Tests added/updated
   - [ ] All tests pass
   ```

### Review Process

- Maintainer will review within 3-5 days
- Address any requested changes
- Once approved, PR will be merged
- Your contribution will be acknowledged!

---

## 🏆 Recognition

Contributors will be acknowledged in:
- Repository contributors list
- Release notes (for significant contributions)
- Special thanks section (coming soon)

---

## 📧 Questions?

If you have questions about contributing:

- Open an issue with the `question` label
- Check existing issues and discussions
- Contact via university email (for NCI students)

---

## 📚 Additional Resources

- [Python PEP 8 Style Guide](https://pep8.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [Markdown Guide](https://www.markdownguide.org/)

---

<div align="center">

**Thank you for contributing! 🎉**

*Every contribution, no matter how small, makes a difference!*

</div>
