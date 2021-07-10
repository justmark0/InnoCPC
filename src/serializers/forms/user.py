from fastapi import Form


class TelegramAuthUser:
    def __init__(
        self,
        id: int = Form(...),
        auth_date: int = Form(...),
        first_name: str = Form(...),
        username: str = Form(...),
        hash: str = Form(...),
    ):
        self.id = id
        self.auth_date = auth_date
        self.username = username
        self.first_name = first_name
        self.hash = hash
