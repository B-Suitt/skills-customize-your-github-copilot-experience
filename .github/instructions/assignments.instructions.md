---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- The assignment must be created as a `README.md` file
- Do not remove or skip required sections from the template.

## 2. Section Guidance

The section headers should reflect the structure in the template, including the exact icon usage.
- The section headers should reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., Python Basics, Loops and Conditionals).
- **Objective**: 1–2 sentences summarizing the learning outcome or goal.
- **Background** (optional): short context or motivation, 1–3 sentences.
- **Starter Code**: point to starter files (relative paths) and describe how to run them.
- **Tasks**: List numbered tasks. For each task include:
   - **Name**: action-oriented task title.
   - **Description**: clear steps the student must perform.
   - **Requirements**: bullet list of measurable acceptance criteria.
   - **Examples**: input/output or sample runs in fenced code blocks when helpful.
- **Submission**: how students should submit their work (file names, folder structure, or link formats).
- **Estimated Time**: approximate completion time (e.g., 30–60 minutes).
- **Difficulty**: one of `Beginner`, `Intermediate`, `Advanced`.
- **Grading Notes** (optional): hints for TAs/graders about automatic tests or common pitfalls.

Do not add unrelated sections. Keep each assignment focused, concise, and student-friendly.

---

**Required filename and location**

- Each assignment MUST be a `README.md` located inside its assignment folder under `assignments/` (for example `assignments/python-basics/README.md`).

**Template**

- Start from the template at [`templates/assignment-template.md`](../../templates/assignment-template.md). Do not remove required sections from the template; fill them in with assignment-specific content.

**Style & formatting**

- Use clear, simple language aimed at students learning the topic for the first time.
- Use fenced code blocks for code examples and shell commands.
- Use relative links for starter code or data files so assignments render correctly on GitHub.
- Keep lines under ~100 characters where possible.

**Checklist before submitting a new/updated assignment**

- [ ] Based on `templates/assignment-template.md` and saved as `README.md`.
- [ ] Title, Objective, Tasks, Requirements, and Submission sections completed.
- [ ] Starter code paths and data links verified (relative paths).
- [ ] Estimated time and difficulty set.
- [ ] Examples and test instructions included when applicable.

If you need help converting an existing assignment to the template, open an issue linking the current assignment path and a maintainer will assist.