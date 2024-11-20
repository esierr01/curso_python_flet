# Navegación y enrutamiento pero en el navegador

import flet as ft


def main(page: ft.Page):
    page.adaptive = True    # Si es True, ajusta automáticamente la UI a la plataforma o dispositivo.
    # Dimensiones de la app (si no esta en el celular)
    page.window_width = 360
    page.window_height = 720
    page.bgcolor = ft.colors.BROWN_900
    page.window_resizable = False

    page.add(
        ft.Text(f"Route Inicial:  {page.route}")
    )

    def route_change(e: ft.RouteChangeEvent):
        page.add(
            ft.Text(f"Route Modificada  {page.route}")
        )

    page.on_route_change = route_change
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)