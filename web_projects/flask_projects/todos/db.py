import json
from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    title: str
    description: str
    done: bool


class Todos:
    def __init__(self, file_name="todos.json"):
        self.file_name = file_name
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name) as f:
                todos = json.load(f)
                self.todos = [Todo(**t) for t in todos]

        except FileNotFoundError:
            self.todos = [
                Todo(
                    id=1,
                    title="Nauka Pythona",
                    description="Codziennie pół godziny",
                    done=False,
                )
            ]

    def save_data(self):
        with open(self.file_name, "w") as f:
            todos = [t.__dict__ for t in self.todos]
            json.dump(todos, f)

    def all(self):
        return self.todos

    def get(self, id):
        return self.todos[id - 1]

    def create(self, data: dict):
        id = len(self.todos) + 1
        data["id"] = id
        todo = Todo(**data)
        self.todos.append(todo)
        self.save_data()

    def __enter__(self):
        self.load_data()
        print("Dane załadowane")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.save_data()
        print("Dane zapisane")


with Todos() as todos:
    print(todos.all())

# todos = Todos()

# print(todos.all())
print("Po context managerze")
