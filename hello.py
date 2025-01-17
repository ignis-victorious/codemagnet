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


ft.app(target=main)
