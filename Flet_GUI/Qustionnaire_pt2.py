import flet as ft
import json 

def test(page: ft.Page):
    page.title = "TEST"
    page.window.width = 400
    page.window.height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def main_page():
        page.controls.clear()
        greeting = ft.Text(value="Hello, fill out the text boxes.")
        username = ft.TextField(label="Username", hint_text="Enter your CS Student ID")
        password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        feedback = ft.Text(size=16)

        def login(e):
            data = {}

            with open("data.json", "r") as f:
                data = json.load(f)
            if data[username.value] == password.value:
                print("Login successful!")
            
            else:
                feedback.value = "Wrong password."
                      
        def register(e):
            register_page()

        default_btn = ft.Button("Login", on_click=login)
        page.floating_action_button = ft.FloatingActionButton("Sign up", on_click=register)

        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                        default_btn,
                        feedback
                    ]
                ),
                alignment=ft.Alignment.CENTER,
            )
           
        )

    def register_page():
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Fill out the text boxes to sign up.")
        username = ft.TextField(label="Username", hint_text="Enter your CS Student ID")
        password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        confirm_password = ft.TextField(label="Confirm Password", password=True, can_reveal_password=True)
        feedback = ft.Text(size=16)

        def register(e):
            if password.value == confirm_password.value:
                data = {}

                with open("data.json", "r") as f:
                    data = json.load(f)

                data[username.value] = password.value
                with open("data.json", "w") as f:
                    json.dump(data, f)

                main_page()
            
            else:
                feedback.value = ("Re-enter the same password to continue.")

        page.floating_action_button = ft.FloatingActionButton("Create Account", on_click=register)
       
        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                        confirm_password,
                        feedback
                    ]
                ),
                alignment=ft.Alignment.CENTER,
            )
           
        )

    main_page()

ft.run(test)