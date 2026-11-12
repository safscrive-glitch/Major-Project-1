import flet as ft

def main(page: ft.Page):
    page.title = "Addition & Subtraction QUIZ"
    page.window.width = 400
    page.window.height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    questions = {
        "32 + 78" : 110,
        "112 - 36" : 76,
        "64 - 15" : 49,
        "84 + 68" : 152,
        "198 - 67" : 131
    }

    def main_page():
        page.controls.clear()
        feedback = ft.Text(size=16)
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
                content=ft.Column(controls = [questionnaire, feedback]),
                alignment=ft.Alignment.CENTER,
            )
           
        )

    main_page()

ft.run(main)