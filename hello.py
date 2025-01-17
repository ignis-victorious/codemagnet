#  https://codemagnet.in/2024/11/20/python-flet-tutorial-build-cross-platform-applications-effortlessly/
import flet as ft
## Widgets are the building blocks of a Flet application. Common widgets include Text, Button, TextField, and ListView.


def main(page: ft.Page) -> None:
    page.title = "Interactive Widgets"
    page.add(
        ft.Text("Welcome to Flet!"),
        ft.TextField(label="Enter your name"),
        ft.ElevatedButton(
            text="Click Me!",
            on_click=lambda e: page.add(ft.Text("This button has been clicked!")),
        ),
    )
    page.title = "Layouts Example"
    page.add(
        ft.Row(
            [
                ft.Text("Row Item 1"),
                ft.Text("Row Item 2"),
            ]
        ),
        ft.Column(
            [
                ft.Text("Column Item 1"),
                ft.Text("Column Item 2"),
            ]
        ),
    )
    counter = ft.Text("0", size=30)

    def increment(e) -> None:
        counter.value = str(int(counter.value) + 1)
        page.update()

    page.title = "Counter App"
    page.add(counter, ft.ElevatedButton(text="Increment", on_click=increment))


ft.app(target=main)
