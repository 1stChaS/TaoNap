class Taonap_Bill:
    def __init__(self, customer_name, customer_nickname, customer_phone):
        self.__customer_name = customer_name  # name with surname ex. Chananthida Sopaphol
        self.__customer_nickname = customer_nickname
        self.__customer_phone = customer_phone

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Your name should be string.")
        self.__customer_name = new_name

    @property
    def customer_nickname(self):
        return self.__customer_nickname

    @customer_nickname.setter
    def customer_nickname(self, new_nickname):
        if not isinstance(new_nickname, str):
            raise ValueError("Your nickname should be string.")
        self.__customer_nickname = new_nickname

    @property
    def customer_phone(self):
        return self.__customer_phone

    @customer_phone.setter
    def customer_phone(self, new_phone):
        if not isinstance(new_phone, str):
            raise ValueError("Your phone number should be string.")
        if len(new_phone) != 10:
            raise ValueError("Your phone number should have 10 digits.")
        self.__customer_phone = new_phone


