from pydantic import BaseModel, ConfigDict, EmailStr


class BrandingBase(BaseModel):
    firm_name: str
    advocate_name: str

    address: str
    city: str
    state: str
    pincode: str

    phone: str
    email: EmailStr
    website: str | None = None

    gst_number: str | None = None
    bar_registration_no: str | None = None

    logo_path: str | None = None
    signature_path: str | None = None

    primary_color: str = "#1F4E79"
    secondary_color: str = "#404040"

    default_invoice_template: str = "classic"


class BrandingCreate(BrandingBase):
    pass


class BrandingUpdate(BaseModel):
    firm_name: str | None = None
    advocate_name: str | None = None

    address: str | None = None
    city: str | None = None
    state: str | None = None
    pincode: str | None = None

    phone: str | None = None
    email: EmailStr | None = None
    website: str | None = None

    gst_number: str | None = None
    bar_registration_no: str | None = None

    logo_path: str | None = None
    signature_path: str | None = None

    primary_color: str | None = None
    secondary_color: str | None = None

    default_invoice_template: str | None = None


class BrandingResponse(BrandingBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
