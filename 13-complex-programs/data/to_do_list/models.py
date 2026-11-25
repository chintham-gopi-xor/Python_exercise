from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    priority: str
    done: bool = False


class TodoList:

    PRIORITY_ORDER = {
        "high": 0,
        "medium": 1,
        "low": 2
    }

    def __init__(self, tasks=None):
        self.tasks = tasks or []

    def next_id(self):

        if not self.tasks:
            return 1

        return max(task.id for task in self.tasks) + 1

    def add_task(self, title, priority="medium"):

        task = Task(
            id=self.next_id(),
            title=title,
            priority=priority,
            done=False
        )

        self.tasks.append(task)

        return task

    def get_task(self, task_id):

        for task in self.tasks:

            if task.id == task_id:
                return task

        raise ValueError(f"no task with id {task_id}")

    def complete_task(self, task_id):

        task = self.get_task(task_id)

        task.done = True

        return task

    def delete_task(self, task_id):

        task = self.get_task(task_id)

        self.tasks.remove(task)

    def list_tasks(self):

        return sorted(
            self.tasks,
            key=lambda task: (
                task.done,
                self.PRIORITY_ORDER[task.priority],
                task.id
            )
        )