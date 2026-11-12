import flet as ft
import json

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text("Header", size=24, weight="bold"),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.Text("Left Box"), expand=2, bgcolor="blue200", padding=10),
                        ft.Container(content=ft.Text("Right Box"), expand=1, bgcolor="green200", padding=10),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.Text("2nd Left Box"), expand=1, bgcolor="blue200", padding=10),
                        ft.Container(content=ft.Text("2nd Right Box"), expand=3, bgcolor="green200", padding=10),
                    ]
                )
            ]
        )
    )
#ft.run(main)

def grid(page: ft.Page):
    page.add(
        ft.Container(
            expand=1,
            content=ft.GridView(
                expand=1,
                runs_count=8,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
                controls=[
                    ft.Images(
                        src=f"https://picsum.photos/150/150?{i}",
                    )
                    for i in range(0,60)
                ]
            )

        )
    )

def test(page: ft.Page):
    page.title = "TEST"
    page.window.width = 700
    page.window.height = 900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    questions = {
        "19 + (23*3)" : 88,
        "13 * 9" : 117,
        "(6 * 4) / 2" : 12,
        "(58 + 40) / 2 - 4" : 45,
        "(884 - 68) / 4 + 7" : 213
    }
    question_list = []

    def main_page():
        page.controls.clear()
        page.floating_action_button = None
        feedback = ft.Text(size=16)

        questions = {
            "19 + (23*3)" : 88,
            "13 * 9" : 117,
            "(6 * 4) / 2" : 12,
            "(58 + 40) / 2 - 4" : 45,
            "(884 - 68) / 4 + 7" : 213
        }

        question_list = []
        question_list.append(ft.Text("19 + (23*3)", size=18, weight="bold"))
        question_list.append(ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="126", label="126"),
                ft.Radio(value="99", label="99"),
                ft.Radio(value="88", label="88"),
            ])
        )) 
        question_list.append(ft.Text("13 * 9", size=18, weight="bold"))
        question_list.append(ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="69", label="69"),
                ft.Radio(value="117", label="117"),
                ft.Radio(value="93", label="93"),
            ])
        ))
        question_list.append(ft.Text("(6 * 4) / 2", size=18, weight="bold"))
        question_list.append(ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="12", label="12"),
                ft.Radio(value="24", label="24"),
                ft.Radio(value="48", label="48"),
            ])
        ))
        question_list.append(ft.Text("(58 + 40) / 2", size=18, weight="bold"))
        question_list.append(ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="53", label="53"),
                ft.Radio(value="45", label="45"),
                ft.Radio(value="-49", label="-49"),
            ])
        ))
        question_list.append(ft.Text("(884 - 68) / 4 + 7", size=18, weight="bold"))
        question_list.append(ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="213", label="213"),
                ft.Radio(value="220.4", label="220.4"),
                ft.Radio(value="420", label="420"),
            ])
        ))

        def check_answer(e):
            checking_answers_page()

        page.floating_action_button = ft.FloatingActionButton("Submit", on_click=check_answer)

        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=question_list
                ),
                alignment=ft.Alignment.CENTER
            ),
            feedback
        )

    def checking_answers_page():
        page.controls.clear()
        page.floating_action_button = None
        message = ft.Text("Click the button below to check your score!", size=18, weight="bold")
        feedback = ft.Text(size=16)

        def check_answer(e):
            score = 0
            for x in range(len(question_list)):
                if x%2 == 0:
                    continue
                else:
                    if question_list[x].value == questions[question_list[x-1].value]:
                        score.value+=1
            feedback.value=(f"Your final score is {score}.")

        check_score = ft.Button("Score", on_click=check_answer)

        page.add(
            ft.Container(
                expand=1,
                content=ft.Column(
                    controls=[
                        message,
                        check_score,
                        feedback
                    ]
                )
            )
        )
    
    main_page()

ft.run(test)