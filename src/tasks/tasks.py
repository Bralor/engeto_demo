# import requests  # unused


class EngetoTaskEntity:
    """Create an object that represents the task from the course."""

    def __init__(
            self, name: str, time: int,
            tests: bool, lesson: str,
            solution: str = "") -> None:
        self.name = name
        self.time = time
        self.tests = tests
        self.lesson = lesson
        self.solution = solution

    def __repr__(self) -> str:
        return f"{self.lesson}: {self.name}"

    @property
    def solution(self) -> str:
        return self._solution

    @solution.setter
    def solution(self, filename: str):
        if not isinstance(filename, str):
            raise ValueError("Filename has to be string.")
        self._solution = filename
