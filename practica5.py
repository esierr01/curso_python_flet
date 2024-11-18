import flet as ft


def main(page: ft.Page):
    def checkbox_changed(e):
        output_text.value = (
            f"Ya aprendiste como usar ski : {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Aprenda a usar ski", value=False, on_change=checkbox_changed)
    page.add(output_text, todo_check)


ft.app(main)
