from flask import *
from util.aws.s3_upload_file_api import S3UploadFileApi
from service.board_message_service import BoardMessageService
from model.board_message import BoardMessage

upload_file_route = Blueprint("upload_file_route", __name__)

@upload_file_route.route('/rest/uploadFile', methods = ['POST'])
def upload_file():
    file = request.files['uploadFile']
    message = request.form.get('message')
    print(file.filename)
    print(message)
    if file and message:
        s3_upload_file_api = S3UploadFileApi()
        s3_upload_file_api.hello_s3()
        fileName = s3_upload_file_api.upload_file(file)
        board_message = BoardMessage(message, fileName)
        board_message_service = BoardMessageService()
        board_message_service.create_board_message(board_message = board_message)
        return 'success'
    
    return 'fail'