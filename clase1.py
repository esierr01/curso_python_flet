import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800  # colocar color de fondo
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    # si colocamos .START se alinea a la izq o .END a la der

    page.title = "Sierra App"

    texto = ft.Text("Mi primera App con Flet")      # label 
    texto2 = ft.Text("Este un ejemplo para otra etiqueta")

    def cambiar_texto(e):
        if texto2.value == "Este un ejemplo para otra etiqueta":
            texto2.value = "Hice un cambio de texto, 2da linea"
        else:
            texto2.value = "Este un ejemplo para otra etiqueta"

        page.update()

    boton = ft.FilledButton(text="Cambiar Texto", on_click=cambiar_texto)

    page.add(texto, texto2, boton)

ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)        # -> Si se quiere hacer en el navegador