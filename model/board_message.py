from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Table

# 宣告對映
Base = declarative_base()

class BoardMessage(Base): # 創建這張資料表，繼承自 Base 這個 declarative_base() class
    __tablename__ = 'board_message'
    board_message_id = Column(Integer, primary_key=True)
    board_message = Column(String(1000), nullable=False)
    board_image_name = Column(String(1000), nullable=False)

    def __init__(self, board_message, board_image_name):
        self.board_message = board_message
        self.board_image_name = board_image_name

    def __repr__(self):
        return f"<BoardMessage(id={self.board_message_id}, message={self.board_message}, image_name={self.board_image_name})>"