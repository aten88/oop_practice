class Animals:
    age = int
    name = str
    breed = str
    voice = str
    form = str

    def __init__(self, age, name, breed, voice, form) -> None:
        self.age = age
        self.name = name
        self.breed = breed
        self.voice = voice
        self.form = form

    def make_voice(self) -> None:
        return self.voice * self.age

    def tell_me_about(self) -> None:
        return (
            f'{self.name} is a {self.form} {self.breed} and is '
            f'{str(self.age)} years old.'
        )


class Dogs(Animals):
    def make_voice(self) -> None:
        return f'{self.voice}i am a dog!'


class Cats(Animals):
    def make_voice(self) -> None:
        return f'{self.voice * self.age}i am a cat!'


chester = Cats(3, 'Chester', 'Siam', 'Miow ', 'Cat')
print(chester.make_voice())
print(chester.tell_me_about())
print(chester.breed)

bretta = Dogs(10, 'Bretta', 'Spaniel', 'Wow, Wow ', 'Dog')
print(bretta.make_voice())
print(bretta.tell_me_about())
print(bretta.breed)
