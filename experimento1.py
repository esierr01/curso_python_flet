import flet as ft


def main(page: ft.Page):
    page.title = "Experimento 1"
    page.window_width = 520
    page.window_height = 600
    page.window_resizable = False
    page.bgcolor = ft.colors.with_opacity(0.7, '#1D2E61')
    page.update()
    
    # FUNCIONES
    #
    def presiono(e):
        if (nombre.value):
            mensaje = ft.Text(value=f"Hola {nombre.value}, ya este vehículo es tuyo !!", size=20, weight=ft.FontWeight.BOLD)
            bloque_msg = ft.Column(
                [
                    mensaje,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            page.add(mensaje)
        else:
            nombre.error_text = "Por favor inserte su nombre para poder avanzar"
            page.update()

    # ELEMENTOS
    #
    imagen = ft.Image(
        src="./assets/auto1.png",
        width=350,
        height=350,
        fit=ft.ImageFit.SCALE_DOWN,
    )
    nombre = ft.TextField(label="Introduzca su nombre")
    boton = ft.ElevatedButton("Presione", on_click=presiono)
    #
    # Creo una columna que contenga todos los elementos y los centre
    columna_ppal = ft.Column(
        [
            imagen,
            nombre, 
            boton,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # PINTAR
    #
    page.add(columna_ppal)

ft.app(main)
