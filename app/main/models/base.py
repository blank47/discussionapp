# In your models/base.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True  # Ensures Base class is not created as a table

    def to_dict(self):
            """Generic method to convert model to dictionary, handling non-serializable types."""
            result = {}
            for column in self.__class__.__table__.columns:
                value = getattr(self, column.name)
                # Check for datetime type and format it as a string in ISO format
                if isinstance(value, datetime):
                    result[column.name] = value.isoformat()
                # Here you can add more conditions to handle other specific types
                # Example for handling Decimal type (common in financial data):
                # elif isinstance(value, Decimal):
                #     result[column.name] = float(value)
                else:
                    result[column.name] = value
            return result