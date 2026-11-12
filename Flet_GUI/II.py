import flet as ft
#data is an invisible factor
#this is another way to do the question from 'Flet_GUI' 
def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)
    message = ft.Text("This is a message", size=30)

    def increment_click(e):
        counter.data+=1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )

    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    message,
                    counter
                ]
            ),
            alignment=ft.Alignment.CENTER,
        )
    )
#ft.run(main)

info = ["ICS4U", "91878"]

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

        def submit_click(e):
            collected_name = username.value
            collected_password = password.value
            if (collected_name == info[0] and collected_password == info[1]):
                print("Login successful!")
                question_page()
            
            else:
                print("Wrong password.")

        page.floating_action_button = ft.FloatingActionButton("Log In", on_click=submit_click)
       
        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                    ]
                ),
                alignment=ft.Alignment.CENTER,
            )
           
        )

    def question_page():
        questions = {
            "32 + 78" : 110,
            "112 - 36" : 76,
            "64 - 15" : 49,
            "84 + 68" : 152,
            "198 - 67" : 131
        }
        page.controls.clear()
        questionnaire = [
            ft.TextField(label=x, hint_text="Enter your answer") for x in questions
        ]
            
        def submit_click(e):
            score = 0
            for x in questionnaire:
                if (int(x.value) == questions[x.label]):
                    score+=20

            print(f"Your final score is {score}.")                

        page.floating_action_button = ft.FloatingActionButton("Submit", on_click=submit_click) 

        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(controls = questionnaire),
                alignment=ft.Alignment.CENTER,
            )
        )

    main_page()

ft.run(test)