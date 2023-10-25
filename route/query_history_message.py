from flask import *
from service.board_message_service import BoardMessageService

query_history_message_route = Blueprint("query_history_message_route", __name__)


@query_history_message_route.route('/rest/queryAllHistoryMessage')
def queryAllHistoryMessage():
    try:
        board_message_service = BoardMessageService()
        all_message = board_message_service.find_all_board_message()
        aws_cloud_front_domain_name='https://d305hij1yblnjs.cloudfront.net/'
        result = []
        for boardMessage in all_message:
            url = aws_cloud_front_domain_name + boardMessage.board_image_name
            row = {
                'board_message':boardMessage.board_message,
                'board_image_url':url
            }
            result.append(row)
        return {
            'data': result
        }
    except Exception as e:
        print(str(e))
    
    return jsonify(error=True, message="查詢失敗"), 500
    