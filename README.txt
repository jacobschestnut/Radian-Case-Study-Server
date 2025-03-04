Radian Case Study Server

This is a simple server built using FastAPI.

Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd draw-steel-server

2. Set up virtual environment:
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows

3. Install dependencies:
    pip install -r requirements.txt

4. Run the server:
    uvicorn app.main:app --reload

Now the FastAPI server will be running at http://127.0.0.1:8000 !
