# Mis notas adhesivas

import flet as ft

def main(page: ft.Page):
    page.title = "Tablero de Notas adhesivas"
    page.padding = 20
    page.theme_mode = "light"   # para que ponga las letras en oscuro
    page.bgcolor = ft.colors.BLUE_GREY_900

    def add_note(e):
        new_note = create_note("");
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):
        note_content = ft.TextField(
            value=text, 
            multiline=True,    
            border=ft.InputBorder.NONE             
        )

        note = ft.Container(
                content=ft.Column([note_content, ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: delete_note(note))]),
                width=200, 
                height=200,
                bgcolor=ft.colors.YELLOW_300,
                border_radius=20,
                padding=10,  
        )
        return note
        

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        # horizontal=True,
        # horizontal=False
        child_aspect_ratio=1,
        spacing=40,     # espaciado vertical
        run_spacing=40,     # espaciado horizontal
    )

    notes = [
        
    ]
    # page.add(ft.Row(notes))
    for note in notes:
        grid.controls.append(create_note(note))

    page.add(ft.Row([
        ft.Text("Mis notas adhesivas", size = 24, weight="bold", color=ft.colors.WHITE),
        ft.IconButton(icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.WHITE)
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ), grid)


ft.app(target=main)