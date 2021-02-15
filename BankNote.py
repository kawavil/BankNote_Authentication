from pydantic import BaseModel
# pydantic provides some features like error reporting and data handling(reporting)

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
