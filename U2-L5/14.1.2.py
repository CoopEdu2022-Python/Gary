class User:
    def __init__(self, id, nickname, credits):
        self.nickname = str(nickname)
        self.id = str(id)
        self.credits = int(credits)

    def upgrade_to_vip(self):
        vip = self.id, self.nickname, self.credits

        return vip

    def get_info(self):
        print(self.nickname)
        print(self.id)
        print(self.credits)


class Vip(User):
    def __init__(self, id, nickname, credits):
        super().__init__(id, nickname, credits)
        self.vip_level = 1

    def get_info(self):
        super().get_info()
        print(self.vip_level)



