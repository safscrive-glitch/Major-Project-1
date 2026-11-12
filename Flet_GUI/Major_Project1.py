import flet as ft
import json

questions = [
    "What is your name?",        
    "What is your age?",
    "What is your gender?",
    "[1] Do you prefer...",
    "[2] Do you prefer...",
    "[3] Do you prefer...",
    "[4] Do you prefer...",
    "[5] Your go-to drink in the morning is...",
    "[6] You would go swimming at...",
    "[7] During winter, you would...",
]   

class person:
    def __init__(self, name, age, gender, answer_list):
        self.name = name
        self.age = age
        self.gender = gender
        self.answer_list = answer_list

    def match(self,other):
        counter = 0
        for x in self.answer_list:
            if other.answer_list[int(x)] == self.answer_list[int(x)]:
                counter+=1
        for x in range(7):
            if counter == x:
                return counter
        
people = [
    person("Irene", 20, "Female",   ['2','2','1','2','3','1','1']),
    person("Vince", 21, "Enby",     ['1','1','2','1','3','1','2']),
    person("Pearl", 28, "Female",   ['1','1','1','1','3','3','4']),
    person("Bianca", 33, "Female",  ['1','2','2','2','2','3','1']),
    person("Harvey", 27, "Male",    ['2','2','1','1','3','3','3']),
    person("Morgan", 32, "Enby",    ['2','2','2','3','1','1','3']),
    person("Ezra", 19, "Male",      ['1','2','1','3','4','3','4']),
    person("Jasmine", 29, "Female", ['2','1','1','3','2','1','1']),
    person("Nicole", 28, "Female",  ['1','2','1','3','1','3','4']),
    person("Riko", 29, "Male",      ['1','2','2','3','3','3','3']),
    person("Theresa", 31, "Female", ['2','1','2','1','2','1','1']),
    person("Parker", 23, "Male",    ['2','2','2','2','3','2','3']),
] 

current_user: person

def main(page: ft.Page):
    page.title = "Dating App"
    page.window.width = 475
    page.window.height = 675
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.floating_action_button = None
    page.scroll = ft.ScrollMode.ALWAYS

    def start_page():
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Login to your account or sign up", size=16, weight="bold", color=ft.Colors.GREEN_300)
        username = ft.TextField(label="Username", hint_text="Enter your username")
        password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        feedback = ft.Text(size=16)

        def login(e):
            global current_user
            single_info = {}
            question_info = None

            with open("info.json", "r") as f:
                single_info = json.load(f)
            with open("data.json", "r") as f:
                question_info = json.load(f)
            
            try: 
                if single_info[username.value] == password.value:
                    print("Login successful!")
                    for x in question_info:
                        if x["What is your name?"] == username.value:
                            answerlist = [x[questions[i]] for i in range(len(questions)) if i > 2]
                            current_user = person(x["What is your name?"], x["What is your age?"], x["What is your gender?"], answerlist)
                        
                    match_page()
                
            except:
                feedback.value = "Incorrect username or password. Try again."
                        
        def register(e):
            register_page()

        default_btn = ft.Button("Login", on_click=login, icon=ft.Icons.LOGIN, icon_color=ft.Colors.GREEN_300)
        page.floating_action_button = ft.FloatingActionButton("Sign up", on_click=register, icon=ft.Icons.ARROW_UPWARD)

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
        global username
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Fill out the text boxes to sign up and start the survey", size=16, weight="bold", color=ft.Colors.BLUE_300)
        username = ft.TextField(label="Username", hint_text="Enter your username")
        password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        confirm_password = ft.TextField(label="Confirm Password", password=True, can_reveal_password=True)
        feedback = ft.Text(size=16)

        def register(e):
            if password.value == confirm_password.value:
                single_info = {}

                with open("info.json", "r") as f:
                    single_info = json.load(f)

                single_info[username.value] = password.value
                with open("info.json", "w") as f:
                    json.dump(single_info, f)

                question_page()
            
            else:
                feedback.value = "Re-enter the same password to continue."

        page.floating_action_button = ft.FloatingActionButton("Create Account", on_click=register, icon=ft.Icons.CREATE_SHARP)
       
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

    def question_page():
        page.controls.clear()
        page.floating_action_button = None
        message = ft.Text("Fill out the questions, then click submit once finished", size=16, weight="bold", color=ft.Colors.CYAN_300)
          
        question_controls = [
            ft.TextField(label="What is your name?", hint_text="Enter your answer"),
            ft.TextField(label="What is your age?", hint_text="Enter your answer"),
            ft.TextField(label="What is your gender?", hint_text="Enter your answer"),
            ft.Text(value="[1] Do you prefer..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="Clean"), ft.Radio(value="2", label="Messy")])),
            ft.Text(value="[2] Do you prefer..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="Formal"), ft.Radio(value="2", label="Casual")])),
            ft.Text(value="[3] Do you prefer..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="Quiet"), ft.Radio(value="2", label="Outgoing")])),
            ft.Text(value="[4] Do you prefer..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="Short"), ft.Radio(value="2", label="Tall"), ft.Radio(value="3", label="Does not matter")])),
            ft.Text(value="[5] Your go-to drink in the morning is..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="Coffee"), ft.Radio(value="2", label="Matcha"), ft.Radio(value="3", label="Tea"), ft.Radio(value="4", label="Water")])),
            ft.Text(value="[6] You would go swimming at..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="A beach"), ft.Radio(value="2", label="A pool"), ft.Radio(value="3", label="Not at all")])),
            ft.Text(value="[7] During winter, you would..."),
            ft.RadioGroup(content=ft.Column([ft.Radio(value="1", label="Go sledding"), ft.Radio(value="2", label="Go skating"), ft.Radio(value="3", label="Play in the snow"), ft.Radio(value="4", label="Stay home")])),
        ]

        def submit(e):
            global current_user
            data = []
            with open("data.json", "r") as f:
                data=json.load(f)

            new_person = {}
            for x in range(len(questions)):
                if x<3:
                    new_person[questions[x]] = question_controls[x].value
                else:
                    new_person[questions[x]] = question_controls[(x-3)*2+4].value

            data.append(new_person)

            with open("data.json", "w") as f:
                json.dump(data, f)
                                 
            data = []
            with open("data.json", "r") as f:
                data=json.load(f)

            for x in data:
                if x["What is your name?"] == username.value:
                    hobby_answer = [x[questions[i]] for i in range(len(questions)) if i > 2]
                    current_user = person(x["What is your name?"], x["What is your age?"], x["What is your gender?"], hobby_answer) 
            
            people.append(current_user)
            match_page()

        page.floating_action_button = ft.FloatingActionButton(content="Submit", on_click=submit)

        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(controls=message),   
                alignment=ft.Alignment.CENTER
            ),
            ft.Container(
                expand=True,
                content=ft.Column(controls=question_controls),   
                alignment=ft.Alignment.CENTER_RIGHT
            )
        )

    def match_page():
        page.controls.clear()
        page.floating_action_button = None

        message = ft.Text(value="Click on a character to check how much you have in common!", size=16, weight="bold", color=ft.Colors.PINK_300)
        feedback = ft.Text(size=16)
        results = [
            "0%  -  No, just no...",
            "13%  -  Maybe not...",
            "27%  -  It's okay...",
            "41%  -  There is a chance.",
            "59%  -  It's looking good!",
            "73%  -  You guys are quite similar!",
            "87%  -  It's looking compatible!!",
            "100%  -  You two are perfect for eachother!!!"
        ]

        def find_match_irene(e):
            result = current_user.match(people[0])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_vince(e):
            result = current_user.match(people[1])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_pearl(e):
            result = current_user.match(people[2])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_bianca(e):
            result = current_user.match(people[3])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_harvey(e):
            result = current_user.match(people[4])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_morgan(e):
            result = current_user.match(people[5])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_ezra(e):
            result = current_user.match(people[6])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_jasmine(e):
            result = current_user.match(people[7])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_nicole(e):
            result = current_user.match(people[8])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_riko(e):
            result = current_user.match(people[9])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_theresa(e):
            result = current_user.match(people[10])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]
        def find_match_parker(e):
            result = current_user.match(people[11])
            for x in range(7):
                if result == x:
                    feedback.value = results[x]      
 
        Irene = ft.Button("Irene", on_click=find_match_irene, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Vince = ft.Button("Vince", on_click=find_match_vince, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Pearl = ft.Button("Pearl", on_click=find_match_pearl, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Bianca = ft.Button("Bianca", on_click=find_match_bianca, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Harvey = ft.Button("Harvey", on_click=find_match_harvey, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Morgan = ft.Button("Morgan", on_click=find_match_morgan, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Ezra = ft.Button("Ezra", on_click=find_match_ezra, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Jasmine = ft.Button("Jasmine", on_click=find_match_jasmine, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Nicole = ft.Button("Nicole", on_click=find_match_nicole, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Riko = ft.Button("Riko", on_click=find_match_riko, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Theresa = ft.Button("Theresa", on_click=find_match_theresa, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)
        Parker = ft.Button("Parker", on_click=find_match_parker, icon=ft.Icons.MONITOR_HEART, icon_color=ft.Colors.RED_300)

        page.add(
            ft.Container(
                content=ft.Column(
                    controls=[
                        message,
                        Irene, Vince, Pearl, Bianca, Harvey, Morgan, Ezra, Jasmine, Nicole, Riko, Theresa, Parker,
                        feedback
                    ]
                ),
                alignment=ft.Alignment.CENTER
            )
        )

    start_page()

ft.run(main)