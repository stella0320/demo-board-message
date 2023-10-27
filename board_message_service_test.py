from service.board_message_service import BoardMessageService
# from servwice as Ser
from model.board_message import BoardMessage

def create_board_message():
    board_message = BoardMessage('test2', 'test2_fileName')
    board_message_service = BoardMessageService()
    board_message_service.create_board_message(board_message)
    print('success')

def find_all_board_message():
    board_message_service = BoardMessageService()
    list = board_message_service.find_all_board_message()
    for bean in list:
        print(bean.__dict__)

def main():
    pass

if __name__ == '__main__':
    main()