from models import TodoList
from storage import load, save


class TodoCLI:

    def __init__(self, filename):

        self.filename = filename

        tasks = load(filename)

        self.todo = TodoList(tasks)

        print(
            f"Loaded {len(tasks)} task(s) from {filename}"
        )

    def save_tasks(self):

        save(
            self.filename,
            self.todo.tasks
        )

    def show_menu(self):

        print()
        print(
            "1) Add task 2) List tasks "
            "3) Complete task 4) Delete task "
            "5) Quit"
        )

    def add_task(self):

        title = input("Title: ").strip()

        priority = input(
            "Priority (high/medium/low) [medium]: "
        ).strip().lower()

        if not priority:
            priority = "medium"

        if priority not in (
            "high",
            "medium",
            "low"
        ):
            print(
                "Invalid priority, using medium."
            )
            priority = "medium"

        task = self.todo.add_task(
            title,
            priority
        )

        self.save_tasks()

        print(
            f"Added task {task.id}."
        )

    def list_tasks(self):

        tasks = self.todo.list_tasks()

        open_count = 0
        done_count = 0

        for task in tasks:

            mark = "[x]" if task.done else "[ ]"

            print(
                f"{mark} {task.id}. "
                f"{task.title} "
                f"({task.priority})"
            )

            if task.done:
                done_count += 1
            else:
                open_count += 1

        print(
            f"{open_count} open, "
            f"{done_count} done"
        )

    def read_task_id(self):

        value = input("Task id: ").strip()

        try:
            return int(value)

        except ValueError:
            print(
                f"'{value}' is not a number."
            )
            return None

    def complete_task(self):

        task_id = self.read_task_id()

        if task_id is None:
            return

        try:

            task = self.todo.complete_task(
                task_id
            )

            self.save_tasks()

            print(
                f"Completed: {task.title}"
            )

        except ValueError as e:

            print(
                f"Error: {e}"
            )

    def delete_task(self):

        task_id = self.read_task_id()

        if task_id is None:
            return

        try:

            self.todo.delete_task(task_id)

            self.save_tasks()

            print(
                f"Deleted task {task_id}"
            )

        except ValueError as e:

            print(
                f"Error: {e}"
            )

    def run(self):

        while True:

            try:

                self.show_menu()

                choice = input(
                    "Choice: "
                ).strip()

            except EOFError:

                self.save_tasks()

                print()
                print(
                    f"Saved "
                    f"{len(self.todo.tasks)} "
                    f"task(s). Bye."
                )

                break

            if choice == "1":

                self.add_task()

            elif choice == "2":

                self.list_tasks()

            elif choice == "3":

                self.complete_task()

            elif choice == "4":

                self.delete_task()

            elif choice == "5":

                self.save_tasks()

                print(
                    f"Saved "
                    f"{len(self.todo.tasks)} "
                    f"task(s). Bye."
                )

                break

            else:

                print(
                    "Please choose 1-5."
                )