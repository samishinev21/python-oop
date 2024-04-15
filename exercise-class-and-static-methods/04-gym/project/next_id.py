class NextId:
    @classmethod
    def get_next_id(cls):
        current_id = cls.id
        cls.id =+ 1
        return current_id