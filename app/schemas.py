from pydantic import BaseModel
from typing import Dict

class WheelSpecificationCreate(BaseModel):
	formNumber: str
	submittedBy: str
	submittedDate: str
	fields: Dict[str, str]

class BogieChecksheetCreate(BaseModel):
	formNumber: str
	inspectionBy: str
	inspectionDate: str
	bogieDetails: Dict[str, str]
	bogieChecksheet: Dict[str, str]
	bmbcChecksheet: Dict[str, str]

class StandardResponse(BaseModel):
	success: bool
	message: str
	data: dict