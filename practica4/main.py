import flet as ft


def main(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor inserte su nombre"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hola {name}, como estas"))


    txt_name = ft.TextField(label="Ingrese su nombre")
    boton = ft.ElevatedButton("Presione para saludarlo!", on_click=btn_click)

    page.add(txt_name, boton)


ft.app(main)
