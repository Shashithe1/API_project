# 🚆 KPA Form Data API

A FastAPI + PostgreSQL backend for handling Railway Workshop form submissions, as per the KPA assignment. This implementation includes:

- ✅ Wheel Specification Submission
- ✅ Bogie Checksheet Submission

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- dotenv

---

## 🔧 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kpa-api.git
cd kpa-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure .env File

Create a file named `.env` in the root directory:

```env
DATABASE_URL=postgresql://kpa_user:YourPassword@localhost:5432/kpa_db
```

Make sure the database and user exist in PostgreSQL.

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

API docs available at:  
📄 http://127.0.0.1:8000/docs

---

## 🗃 API Endpoints

### 1. POST `/api/forms/wheel-specifications`

Submit new wheel specifications.

**Request body (JSON):**
```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelDiscWidth": "127 (+4/-0)"
    // ... other fields
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "...",
    "submittedBy": "...",
    "submittedDate": "...",
    "status": "Saved"
  }
}
```

---

### 2. POST `/api/forms/bogie-checksheet`

Submit bogie checksheet data.

**Request body (JSON):**
```json
{
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "makerYearBuilt": "RDSO/2018",
    "incomingDivAndDate": "NR / 2025-06-25",
    "deficitComponents": "None",
    "dateOfIOH": "2025-07-01"
  },
  "bogieChecksheet": {
    "bogieFrameCondition": "Good",
    "bolsterSuspensionBracket": "Cracked"
  },
  "bmbcChecksheet": {
    "cylinderBody": "WORN OUT",
    "plungerSpring": "GOOD"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Bogie checksheet submitted successfully.",
  "data": {
    "formNumber": "...",
    "inspectionBy": "...",
    "inspectionDate": "...",
    "status": "Saved"
  }
}
```

---

## 🧪 Testing with Postman

- Import the collection: `KPA_form data.postman_collection.json`
- Update request URLs to: `http://127.0.0.1:8000`
- Send requests and check for success responses

---

## 📹 Deliverables

- ✅ Source Code (GitHub or ZIP)
- ✅ Updated Postman Collection (.json)
- ✅ README.md (this file)
- ✅ Screen Recording (2–5 min demo using Swagger UI/Postman + DB view)

---

## 👤 Author

**Shashank Shashi**  
📧 [karthishashi1100@gmail.com](mailto:karthishashi1100@gmail.com)  
📍 Bangalore, India
