# Navegación y enrutamiento pero en el navegador

import flet as ft


def main(page: ft.Page):
    page.adaptive = True    # Si es True, ajusta automáticamente la UI a la plataforma o dispositivo.
    # Dimensiones de la app (si no esta en el celular)
    page.window_width = 360
    page.window_height = 720
    page.bgcolor = ft.colors.BROWN_900
    page.window_resizable = False

    ruta_actual = ft.Text(f"Ruta actual:  {page.route}")

    def go_store(e):
        page.route = "/store"
        ruta_actual.value = f"Ruta actual:  {page.route}"
        page.update()

    def go_raiz(e):
        page.route = "/"
        ruta_actual.value = f"Ruta actual:  {page.route}"
        page.update()

    
    page.add(
        ruta_actual,
        ft.Row(
            [
                ft.ElevatedButton("Ve a la tienda", on_click=go_store),
                ft.ElevatedButton("Regresar", on_click=go_raiz),
            ],
        )        
    )

ft.app(main, view=ft.AppView.WEB_BROWSER)