import flet as ft

def one(page: ft.Page):
    page.title = "Test"

    page.window.width = 600
    page.window.height = 400
    page.window.resizable = False

    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    message = ft.Text(value = "Display 1 text messages")
    page.add(message)
#ft.run(one)

def heading_test(page: ft.Page):
    page.title = "test_2"

    heading = ft.Text(
        value = "Hello I am a window",
        size = 40,
        weight = ft.FontWeight.BOLD,
        data = 0
    )
    page.add(heading)
#ft.run(heading_test)

def button_test(page: ft.Page):
    def btn_click(e): #e is for the event that happens
        page.add(ft.Text("Default Button Clicked!")) #shows this when called

    # Default Button Control
    default_btn = ft.Button( #an object of the class
        content="Click Me",
        icon=ft.Icons.PLAY_ARROW, #arrow before "Click Me"
        on_click=btn_click #when clicked, it does the function
    )   #no bracket because it shouldn't be called right away until 'on_click'

    page.add(default_btn)
#ft.run(button_test)

def work(page: ft.Page):
    def btn_click(e):
        display.value = str(int(display.value) + 1)

    display = ft.Text(value = "0", size = 40)
    button = ft.Button(content = "+", on_click = btn_click)

    page.add(
        ft.Container(
            ft.Column(
                controls = [
                    display,
                    button
                ]
            )
        )
    )
#ft.run(work)