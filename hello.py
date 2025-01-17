import flet as ft


def main(page: ft.Page):
    page.title = "Hello Flet!"
    page.add(ft.Text("Hello, World!"))


# Run the app
ft.app(target=main)
