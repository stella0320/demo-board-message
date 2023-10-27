
from model.board_message import BoardMessage
from util.db.connect_db import ConnectDb
from sqlalchemy import MetaData, Table
import logging

logger = logging.getLogger(__name__)
class BoardMessageService():

    def __init__(self):
        try:
            self.__connect_db__ = ConnectDb()
            self.__engine__ = self.__connect_db__.get_engine()
            self.__session__ = self.__connect_db__.get_session()
        except Exception as e:
            logger.debug(f'exception {e}')

    def get_column_name(self):
        metadata = MetaData()
        engine = self.__engine__
        table = Table('board_message', metadata, autoload=True, autoload_with=engine)

        # Access the column names
        column_names = table.columns.keys()
        return column_names

    def create_board_message(self, board_message = None):
        if board_message:
            try:
                self.__session__.add(board_message)
                self.__session__.commit()
                self.__session__.close()
            except Exception as e:
                self.__session__.rollback()
    
    def create_board_message_list(self, board_message_list = None):
        if board_message_list:
            try:
                self.__session__.add_all(board_message_list)
                self.__session__.commit()
                self.__session__.close()
            except Exception as e:
                self.__session__.rollback()

    def find_all_board_message(self):
        board_message_list = self.__session__.query(BoardMessage)
        self.__session__.close()
        return board_message_list