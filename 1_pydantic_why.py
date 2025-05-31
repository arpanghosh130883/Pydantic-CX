from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)] # strict = True is used to supress the property of pydantic to auto convert any numeric values to Int/float value if passed as string
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # **patient_info unpacks the dictionary into individual keyword arguments matching the fields of the Patient class (which is a Pydantic model here).

'''
patient_info = {
    'name': 'nitish',
    'email': 'abc@gmail.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': '30',
    'weight': 75.2,
    'contact_details': {'phone': '2353462'}
}

patient1 = Patient(**patient_info)

will be unpacked to 

Patient(
    name='nitish',
    email='abc@gmail.com',
    linkedin_url='http://linkedin.com/1322',
    age='30',
    weight=75.2,
    contact_details={'phone': '2353462'}
)

'''


update_patient_data(patient1)
