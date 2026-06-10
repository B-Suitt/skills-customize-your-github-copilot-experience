# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful API using the FastAPI framework. Students will create endpoints to create, read, update, and delete resources and learn how to run the app locally with Uvicorn.

## 🧾 Background

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. This assignment focuses on core REST concepts and basic request/response handling.

## 🧰 Starter Code

There is a starter application in this folder: `starter_app.py`.

Run the app locally with:

```bash
pip install -r requirements.txt
uvicorn starter_app:app --reload
```

The API will be available at `http://127.0.0.1:8000` and the automatic docs at `http://127.0.0.1:8000/docs`.

## 📝 Tasks

### 🛠️ Implement a CRUD API for `items`

#### Description
Finish and/or extend the provided starter app so it offers a minimal CRUD API for an `Item` resource. Use in-memory storage (dictionary or list) for simplicity.

#### Requirements
Completed program should:

- Expose endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`.
- Use Pydantic models for request and response validation.
- Return appropriate HTTP status codes (e.g., 201 for created, 404 for not found).
- Validate input and handle error cases with clear JSON error messages.
- Include example curl or HTTPie requests in the README or comments.

## 🧪 Examples

Create an item (example using `httpie`):

```bash
http POST :8000/items name="Ball" description="A round object"
```

Get all items:

```bash
http :8000/items
```

## 📤 Submission

- Submit the completed `starter_app.py` (or `app.py` / `main.py`) and any notes in this folder. Ensure the code runs with the commands above.
- Include in the PR description how to run the app and any extra features implemented.

## ⏱️ Estimated Time

60–90 minutes

## ⚖️ Difficulty

Intermediate

## 🧾 Grading Notes (for TAs)

- Verify endpoints exist and behave as documented.
- Check Pydantic validation and HTTP status codes.
- Confirm the app runs with `uvicorn starter_app:app --reload` and docs are reachable at `/docs`.

---

**Files in this assignment folder**: `starter_app.py`, `requirements.txt`.

If you'd like, I can also add automated tests or an example Postman collection.
