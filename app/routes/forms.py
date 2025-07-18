from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@router.post("/api/forms/wheel-specifications", response_model=schemas.StandardResponse)
def submit_wheel_spec(data: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
	entry = models.WheelSpecification(**data.dict())
	db.add(entry)
	db.commit()
	db.refresh(entry)
	return {
		"success": True,
		"message": "Wheel specification submitted successfully.",
		"data": {
			"formNumber": entry.formNumber,
			"submittedBy": entry.submittedBy,
			"submittedDate": entry.submittedDate,
			"status": "Saved"
		}
	}

@router.post("/api/forms/bogie-checksheet", response_model=schemas.StandardResponse)
def submit_bogie_checksheet(data: schemas.BogieChecksheetCreate, db: Session = Depends(get_db)):
	entry = models.BogieChecksheet(**data.dict())
	db.add(entry)
	db.commit()
	db.refresh(entry)
	return {
		"success": True,
		"message": "Bogie checksheet submitted successfully.",
		"data": {
			"formNumber": entry.formNumber,
			"inspectionBy": entry.inspectionBy,
			"inspectionDate": entry.inspectionDate,
			"status": "Saved"
		}
	}