class NextId:
    @classmethod
    def get_next_id(cls):
        cls.id = cls.id + 1
        return cls.id