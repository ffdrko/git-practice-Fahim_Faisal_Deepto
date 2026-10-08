# Project Description

This project is part of **Module 8 - Git & GitHub Practical Assignment** by **Fahim Faisal Deepto**.

## Objectives

- Create and manage a public GitHub repository
- Use Git locally with multiple commits
- Work with branches (`feature/calculator`, `feature/error-handling`)
- Merge branches back into `main`
- Push code to GitHub
- Follow proper folder structure

## Project Overview

A beginner-friendly Python project that prints the author's name, today's date, and demonstrates a simple calculator module (`src/utils.py`) with `add`, `subtract`, `multiply`, `divide`, plus error handling for edge cases like division by zero.

## Folder Structure

```text
git-practice-Fahim_Faisal_Deepto/
├── README.md
├── .gitignore
├── src/
│   ├── main.py
│   └── utils.py
└── docs/
    └── project-description.md
```

## Git Workflow Used

1. `git init` and initial commit with project structure
2. `Add gitignore file`
3. Branch `feature/calculator` → add `add()` and `subtract()` → merge to `main`
4. Improve README formatting
5. Add `multiply` and `divide` functions
6. Update this documentation
7. Branch `feature/error-handling` → add validation and error handling → merge to `main`
8. Push to GitHub with `git remote add origin` and `git push -u origin main`
