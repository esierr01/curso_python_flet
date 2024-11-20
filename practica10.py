# APLICACION ADAPTATIVA PARA CELULAR (ANDROID Y IOS)

import flet as ft


def main(page: ft.Page):
    page.adaptive = True    # Si es True, ajusta automáticamente la UI a la plataforma o dispositivo.
    # Dimensiones de la app (si no esta en el celular)
    page.bgcolor = ft.colors.GREY_800
    page.window_width = 360
    page.window_height = 720
    page.window_resizable = False

    # barra de aplicación (AppBar) en la parte superior de la interfaz de usuario
    page.appbar = ft.AppBar(
        leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),   # Un widget (por ejemplo, un icono) que aparece al principio de la barra de aplicación. Generalmente se usa para un botón de menú (hamburguesa) o un ícono de navegación.
        title=ft.Text("NavBar Adaptativa"),     # Define el título de la barra de aplicación.
        center_title=True,  # Si es true se centra el título, si es false se alinea a la izquierda
        actions=[   # Lista de widgets (por ejemplo, íconos o botones) que se muestran al final de la barra.
            ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))
        ],  # Se utiliza para mostrar acciones como buscar, compartir o configuraciones.
        bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),    # Define el color de fondo de la barra de aplicación.
        toolbar_height=40,  # altura de la appbar
        automatically_imply_leading=True, # Si está en True, automáticamente añade un ícono de retroceso cuando sea necesario.
    )

    # barra de navegación inferior en aplicaciones móviles
    page.navigation_bar = ft.NavigationBar(
        destinations=[  # Lista de objetos que representan cada sección o vista
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Bookmark"),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
        ),
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Checkbox(value=False, label="Dark Mode"),
                    ft.Text("Nombre:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),    # KeyboardType, es para especificar teclado virtual
                    ft.Text("Apellido:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),    # KeyboardType, es para especificar teclado virtual
                    ft.Switch(label="A Switch"),    # Swicthe
                    ft.FilledButton(content=ft.Text("Botón Adaptativo")),
                    ft.ElevatedButton(text="Presiona"),
                    ft.Text("Línea de Texto 1"),
                    ft.Container(
                        ft.Image(
                            src="./assets/auto6.png",
                            width=200,
                            height=150,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        alignment=ft.alignment.center,
                    ),
                ]
            )
        )
    )

ft.app(main)