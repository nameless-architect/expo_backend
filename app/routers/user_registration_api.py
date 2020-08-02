from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


@router.get('/testGet')
async  def test_get():
    return 'Hello from get'

@router.post('/savePersonalDetails')
async def upload_file(personal_details: Request):
    form = await personal_details.form()
    image_file_name = form.get('profilePic').filename
    image_content = await form.get('profilePic').read()
    with open(image_file_name, 'wb') as file:
        file.write(image_content)
    return 'OK'



