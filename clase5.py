# galeria productos responsive

import flet as ft
import os
import base64

def crear_producto(nombre, precio, color, imagen_nombre):
    imagen_path = os.path.join(os.path.dirname(__file__), "assets", imagen_nombre)
    try:
        with open(imagen_path, "rb") as imagen_file:
            imagen_bytes = base64.b64encode(imagen_file.read()).decode()
    except FileNotFoundError:
        print(f"Adevertencia: la imagen {imagen_nombre} no existe en {imagen_path}")
        imagen_bytes = None

    return ft.Container(
        content=ft.Column([
            ft.Image(
                src_base64=imagen_bytes, 
                width=150, height=150, 
                fit=ft.ImageFit.CONTAIN, 
                error_content=ft.Text("Imagen no encontrada") if imagen_bytes else ft.Text("Imagen no encontrada"),
            ),
            ft.Text(nombre, size=16, weight=ft.FontWeight.BOLD),
            ft.Text(value=f"{precio}", size=14),
            ft.ElevatedButton(text="Agregar al carrito", color=ft.colors.WHITE),
        ]),
        bgcolor=color,
        padding=10, 
        border_radius=10,
        width=200,
        height=300,
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=10)
    )


def main(page: ft.Page):
    page.title = "Galería de Productos Responsiva"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900

    
    productos = [
        crear_producto(nombre="Producto 1", precio=19.99, color=ft.colors.BLUE_500, imagen_nombre="auto1.png"),
        crear_producto(nombre="Producto 2", precio=19.99, color=ft.colors.GREEN_500, imagen_nombre="auto2.png"),
        crear_producto(nombre="Producto 3", precio=19.99, color=ft.colors.ORANGE_500, imagen_nombre="auto3.png"),
        crear_producto(nombre="Producto 4", precio=19.99, color=ft.colors.RED_500, imagen_nombre="auto4.png"),
        crear_producto(nombre="Producto 5", precio=19.99, color=ft.colors.GREY_500, imagen_nombre="auto5.png"),
        crear_producto(nombre="Producto 6", precio=19.99, color=ft.colors.AMBER_500, imagen_nombre="auto6.png"),
        crear_producto(nombre="Producto 7", precio=19.99, color=ft.colors.BLUE_GREY_500, imagen_nombre="auto7.png"),
        crear_producto(nombre="Producto 8", precio=19.99, color=ft.colors.BROWN_500, imagen_nombre="auto8.png"),
    ]
    galeria = ft.ResponsiveRow(
        [ft.Container(producto, col={"sm":12, "md":6, "lg": 3}) for producto in productos],
        spacing=20,     # espaciado vertical
        run_spacing=20,     # espaciado horizontal
    )

    # page.add(titulo, galeria) # si lo hacemos asi, no se puede bajar para ver más imagenes abajo, falta el scroll
    contenido = ft.Column([
        ft.Text(value="Galería de Productos", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.colors.WHITE24),
        galeria
    ], scroll=ft.ScrollMode.AUTO, expand=True)
    page.add(contenido)


    

ft.app(main, view=ft.AppView.WEB_BROWSER)
