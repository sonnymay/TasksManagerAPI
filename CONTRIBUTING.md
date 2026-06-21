# Contributing to Task Manager API

Thank you for your interest in contributing! Bug reports, feature requests, and pull requests are all welcome.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/TasksManagerAPI.git`
3. Create a feature branch: `git checkout -b feat/your-feature-name`
4. Install dependencies and set up the project (see [README](README.md#quickstart))

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

## Making Changes

- Follow the existing code style (PEP 8 for Python)
- Add or update tests for any changed behavior
- Keep commits focused — one logical change per commit
- Write clear commit messages: `feat: add task priority endpoint`

## Pull Request Process

1. Ensure all tests pass: `pytest`
2. Update the README if you're adding or changing functionality
3. Open a PR against `main` with a clear description of what you changed and why
4. Reference any related issues with `Closes #123`

## Reporting Bugs

Open an [issue](https://github.com/sonnymay/TasksManagerAPI/issues) with:
- A clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

## Feature Requests

Open an issue labeled `enhancement` describing:
- The problem you're trying to solve
- Your proposed solution
- Any alternatives you considered

## Code of Conduct

Be respectful and constructive. This is a portfolio project maintained by one person — response times may vary.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
