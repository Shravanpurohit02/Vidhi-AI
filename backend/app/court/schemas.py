from pydantic import BaseModel


class CaptchaResponse(BaseModel):
    session_id: str
    image_url: str


class SearchByCNRRequest(BaseModel):
    session_id: str
    cnr: str
    captcha: str


class SearchCaseRequest(BaseModel):
    state: str = ""
    district: str = ""
    court: str = ""
    case_number: str
    year: str


class ImportCourtCaseRequest(BaseModel):
    session_id: str
    cnr: str
    captcha: str
