import json
from dataclasses import dataclass
from django.conf import settings


@dataclass
class Todo:
    id: int
    title: str
    description: str
    done: bool


class Todos:

    def __init__(self, file_name=settings.BASE_DIR / "data/todos.json"):
        # def __init__(self, file_name):
        self.file_name = file_name
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name) as f:
                todos = json.load(f)
                self.todos = [Todo(**t) for t in todos]
            print("Załadowano dane")
        except FileNotFoundError:
            self.todos = [Todo(id=1, title="Nauka Pythona", description="Codziennie pół godziny", done=False)]

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

    def update(self, id: int, data: dict):
        todo = self.get(id)
        for k, v in data.items():
            if k == "id": continue
            setattr(todo, k, v)

        if 'done' not in data:
            todo.done = False

        self.save_data()

    def __enter__(self):
        self.load_data()
        print("Dane załadowane")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.save_data()
        print("Dane zapisane")


if __name__ == "__main__":
    pass


# with Todos() as todos:
#     print(todos.all())
#


#
# todos = Todos(file_name="../data/todos.json")
# print(todos.all())
# data = {"title": "cos tam"}
#
# todos.update(id=1, data=data)


class TaskLoadData:

    def __init__(self, klass):
        # def __init__(self, file_name):
        self.data = Todos().all()
        self.model_class = klass

    def insert(self):
        for d in self.data:
            t = self.model_class()  # Todo
            t.title = d.title
            t.description = d.description
            t.done = bool(d.done)
            t.save()
