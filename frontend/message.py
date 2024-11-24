import json

class Message:
    """
    Message
      Parameters:
        usrname: The username of the message owner.
        msg: The message content.

      Methods:
        modify: used to modify the contents of a message.
    """
    def __init__(self, msg_id, usrname, msg) -> None:
        self.username : str = usrname
        self.content : str = msg
        self.id : int = msg_id

    def modify(self, msg) -> int: #we'll call replacing "modifying" XD
        """Modify the message, returns 1 if successful 0 if not."""
        try:
            self.message = msg
            return 1
        except Exception as e:
            print('INVALID MODIFICATION, MESSAGE NOT CHANGED')
            return 0
    
    def __str__(self) -> str:
        return f"Message: Username = '{self.username}', Content = '{self.content}', ID = {self.id}"
    
    def to_json(self) -> str:
        return json.dumps(self.__dict__)
    