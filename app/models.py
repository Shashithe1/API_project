from sqlalchemy import Column, Integer, String, JSON
from app.database import Base  # Make sure this is the correct import

class WheelSpecification(Base):
	__tablename__ = "wheel_specifications"  # ✅ Table name is required

	id = Column(Integer, primary_key=True, index=True)
	formNumber = Column(String, unique=True)
	submittedBy = Column(String)
	submittedDate = Column(String)
	fields = Column(JSON)

class BogieChecksheet(Base):
	__tablename__ = "bogie_checksheet"  # ✅ Table name is required

	id = Column(Integer, primary_key=True, index=True)
	formNumber = Column(String, unique=True)
	inspectionBy = Column(String)
	inspectionDate = Column(String)
	bogieDetails = Column(JSON)
	bogieChecksheet = Column(JSON)
	bmbcChecksheet = Column(JSON)