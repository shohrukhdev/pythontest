To run the project:
1. Install packages from requirements.txt  - pip install -r requirements.txt
2. Run the server: uvicorn app.main:app --reload

Endpoints:
1) 
POST http://127.0.0.1:8000/projects/
{
  "project_name": "Restaurant",
  "location": "San Francisco"
}

Response: 


2) 
GET http://127.0.0.1:8000/projects/1

