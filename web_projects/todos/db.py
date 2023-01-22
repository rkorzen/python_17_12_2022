from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    title: str
    description: str
    done: bool

class Todos:

    def __init__(self):
        self.todos = [Todo(id=1, title="Nauka Pythona", description="Codziennie pół godziny", done=False)]

    def all(self):
        return self.todos

    def get(self, id):
        return self.todos[id-1]

    def create(self, data: dict ):
        id = len(self.todos) + 1
        data["id"] = id
        todo = Todo(**data)
        self.todos.append(todo)

todos = Todos()