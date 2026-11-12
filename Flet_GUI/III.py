import flet as ft

def main(page: ft.Page):
    page.title = "TEST"
    page.window.width = 400
    page.window.height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    quiz_group = ft.RadioGroup(
        content=ft.Column([
            ft.RadioGroup(value="list", label="list"),
            ft.RadioGroup(value="tuple", label="tuple"),
            ft.RadioGroup(value="array", label="array (primitive keyword)"),
            ft.RadioGroup(value="dict", label="dict"),
        ])
    )
    feedback = ft.Text(size=16)

    def check_answer():
        if quiz_group.value == "array":
            feedback.value = "Correct!"
            feedback.color = ft.Colors.GREEN
        else:
            feedback.value = "Incorrect!"
            feedback.color = ft.Colors.RED

    page.floating_action_button = ft.FloatingActionButton("Submit", on_click=check_answer)

    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                controls = [
                    quiz_group,
                    feedback
                ]
            ),
            alignment=ft.Alignment.CENTER,            
        )    
    )

#ft.run(main)

def test(page: ft.Page):
    page.title = "TEST"
    page.window.width = 400
    page.window.height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    questions = {
        "204 - 107" : 97,
        "112 - 36" : 76,
        "64 - 15" : 49,
        "84 + 68" : 152,
        "198 - 67" : 131
    }

    question_list = []

    question_list[0] = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="107", label="107"),
            ft.Radio(value="97", label="97"),
            ft.Radio(value="87", label="87"),
        ])
    )
    question_list[1] = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="76", label="76"),
            ft.Radio(value="148", label="148"),
            ft.Radio(value="88", label="88"),
        ])
    )
    question_list[2] = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="8.9", label="8.9"),
            ft.Radio(value="49", label="49"),
            ft.Radio(value="79", label="79"),
        ])
    )
    question_list[3] = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="154", label="154"),
            ft.Radio(value="16", label="16"),
            ft.Radio(value="152", label="152"),
        ])
    )
    question_list[4] = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="131", label="131"),
            ft.Radio(value="141", label="141"),
            ft.Radio(value="245", label="245"),
        ])
    )
    feedback = ft.Text(size=16)

    def check_answer():
        for x in question_list:
            if int(x.value) == questions[x.label]:
                with open("data.txt", "w") as f:
                    f.write(question_list.value + "\n")
                feedback.value = "Correct!"
                feedback.color = ft.Colors.GREEN
            else:
                with open("data.txt", "w") as f:
                    f.write(question_list.value + "\n")
                feedback.value = "Incorrect!"
                feedback.color = ft.Colors.RED

    page.floating_action_button = ft.FloatingActionButton("Submit", on_click=check_answer)

    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                controls = [
                    questions,
                    question_list,
                    feedback
                ]
            ),
            alignment=ft.Alignment.CENTER,            
        )    
    )

ft.run(test)