import os


class User:
    MOVIES_LIKED = []
    MOVIES_OWNED = []
    MIN_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = self.MOVIES_LIKED
        self.movies_owned = self.MOVIES_OWNED

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value is None:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError(f"Users under the age of {self.MIN_AGE} are not allowed!")
        self.__age = value

    def __str__(self):
        # TODO: Extract into a method
        movies_liked_str = 'No movies liked.'
        if self.movies_liked:
            movies_liked_str = os.linesep.join(m.details() for m in self.movies_liked)
        # `linesep` is `\n` for Unix/Linux and `\n\r` for Windows

        # TODO: Extract into a method
        movies_owned_str = 'No movies owned.'
        if self.movies_owned:
            movies_owned_str = os.linesep.join(m.details() for m in self.movies_owned)

        return f'''Username: {self.username}, Age: {self.age}
Liked movies:
{movies_liked_str}
Owned movies:
{movies_owned_str}'''