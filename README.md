## Getting Started

1. Clone the repository:

```bash
git clone <repository-url>
cd radian-case-study-server
```

2. Set up virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

Now the FastAPI server will be running at http://127.0.0.1:8000.
