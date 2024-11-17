import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.title = "2da Clase"

    texto1 = ft.Text(value="Texto 1", size=24, color=ft.colors.AMBER)
    texto2 = ft.Text(value="Texto 2", size=24, color=ft.colors.AMBER)
    texto3 = ft.Text(value="Texto 3", size=24, color=ft.colors.AMBER)

    # para que se pongan los textos en una fila, no uno encima de otro
    fila_textos = ft.Row(
        controls=[texto1, texto2, texto3],
        alignment=ft.MainAxisAlignment.CENTER,      # Alineado en el centro
        spacing=50          # espaciado 50px
    )
    page.add(fila_textos)

    boton1 = ft.FilledButton(text="Botón 1")
    boton2 = ft.FilledButton(text="Botón 2")
    boton3 = ft.FilledButton(text="Botón 3")

    # fila de botones
    fila_botones = ft.Row(
        controls=[boton1, boton2, boton3],
        alignment=ft.MainAxisAlignment.CENTER,      # Alineado en el centro
        spacing=50          # espaciado 50px
    )
    page.add(fila_botones)

    textos_columnas = [     # agrega los textos en columna
        ft.Text(value="Columna 1 - Fila 1", size=18, color=ft.colors.CYAN_400),
        ft.Text(value="Columna 1 - Fila 2", size=18, color=ft.colors.CYAN_400),
        ft.Text(value="Columna 1 - Fila 3", size=18, color=ft.colors.CYAN_400)
    ]
    columna_texto1 = ft.Column(
        controls=textos_columnas
    )

    textos_columnas2 = [     # agrega los textos en columna
        ft.Text(value="Columna 2 - Fila 1", size=18, color=ft.colors.CYAN_300),
        ft.Text(value="Columna 2 - Fila 2", size=18, color=ft.colors.CYAN_300),
        ft.Text(value="Columna 2 - Fila 3", size=18, color=ft.colors.CYAN_300)
    ]
    columna_texto2 = ft.Column(
        controls=textos_columnas2
    )

    fila_columnas = ft.Row(
        controls=[columna_texto1, columna_texto2], 
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    page.add(fila_columnas)
    

ft.app(target=main)