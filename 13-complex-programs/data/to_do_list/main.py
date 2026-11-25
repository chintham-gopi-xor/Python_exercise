import argparse

from cli import TodoCLI


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        default="todo.json"
    )

    args = parser.parse_args()

    TodoCLI(args.file).run()


if __name__ == "__main__":
    main()