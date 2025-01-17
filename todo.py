import flet as ft


def main(page: ft.Page):
    page.title = "To-Do App"

    tasks = ft.Column()

    def add_task(e):
        task_name = task_input.value
        if task_name:
            # Create a task row with a unique remove button
            task_row = ft.Row(
                [
                    ft.Text(task_name),
                    ft.ElevatedButton(
                        "Remove", on_click=lambda e, tn=task_name: remove_task(tn)
                    ),
                ]
            )
            tasks.controls.append(task_row)
            task_input.value = ""
            page.update()

    def remove_task(task_name):
        # Keep only tasks that don't match the task_name to remove
        tasks.controls = [
            task for task in tasks.controls if task.controls[0].value != task_name
        ]
        page.update()

    task_input = ft.TextField(label="New Task")
    page.add(task_input, ft.ElevatedButton("Add Task", on_click=add_task), tasks)


ft.app(target=main)
