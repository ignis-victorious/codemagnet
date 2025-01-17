import flet as ft


def main(page: ft.Page) -> None:
    page.title = "First Flet Navigation test"

    def name_page(e) -> None:
        page.clean()
        page.add(
            ft.Text("Welcome to Flet!"),
            ft.TextField(label="Enter your name"),
            ft.ElevatedButton(
                text="Click Me!",
                on_click=lambda e: page.add(ft.Text("This button has been clicked!")),
            ),
        )
        page.update()

    def layout_page(e) -> None:
        page.clean()
        page.add(
            ft.Text("Welcome to Flet!"),
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
            ),
        )
        page.update()

    def counter_page(e) -> None:
        page.clean()

        counter = ft.Text("0", size=30)

        def increment(e) -> None:
            counter.value = str(int(counter.value) + 1)
            page.update()

        page.title = "Counter App"
        page.add(counter, ft.ElevatedButton(text="Increment", on_click=increment))

        page.update()

    page.add(
        ft.Text(
            "This is the main page.",
            size=22,
            color="blue",
        ),
        ft.Text(
            "Navigate to all the functions from here!",
            size=22,
            color="blue",
        ),
        ft.ElevatedButton(text="Press to insert your details", on_click=name_page),
        ft.ElevatedButton(
            text="Press to see the new page layout", on_click=layout_page
        ),
        ft.ElevatedButton(text="Press to play with Counter", on_click=counter_page),
    )


ft.app(target=main)
