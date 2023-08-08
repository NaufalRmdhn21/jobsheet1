class guess:
    def __init__(self):
        self.tebakan = ""
        self.jawaban = ""

    def cek(self):
        if self.tebakan == self.jawaban:
            return True
        return False
