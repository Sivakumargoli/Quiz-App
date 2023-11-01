import kivy
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class QuizApp(App):
    def build(self):
        self.icon='quiz.png'
        self.questions = [
            {
                'question': 'What is the capital of India?',
                'options': ['Agra', 'New Delhi', 'Tirupati', 'Maharashtra'],
                'correct': 'New Delhi',
            },
            {
                'question': 'What is the opposite word of hell?',
                'options': ['Paradise', 'Peace', 'Angry', 'None of these'],
                'correct': 'Paradise',
            },
            {
                'question':'What is the National heritage animal of India ?',
                'options':['Lion','Tiger','Elephant','Deer'],
                'correct':'Elephant',
            },
            {
                'question':'Where the Taj Mahal is located in India ?',
                'options':['Kerala','Agra','Manipur','Uttarakhand'],
                'correct':'Agra',
            },
            {
                'question':'Where the main headquaters of ISRO is located ?',
                'options':['Andhra pradesh','Tamilnadu','Benguluru','Kerala'],
                'correct':'Benguluru',
            },
            {
                "question": "What is the capital of France?",
                "options": ["London", "Madrid", "Paris", "Rome"],
                "correct": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Earth"],
                "correct": "Mars"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
                "correct": "Blue Whale"
            },
            {
                "question": "What is the national fruit of India?",
                "options": ["Apple", "Mango", "Banana", "Orange"],
                "correct": "Mango"
            },
            {
                "question": "What is the national sport of India?",
                "options": ["Cricket", "Tennis", "Football", "Hockey"],
                "correct": "Hockey"
            },
        ]
        random.shuffle(self.questions)
        self.question_index = 0
        self.score = 0

        self.layout = BoxLayout(orientation='vertical')
        self.question_label = Label(text=self.questions[self.question_index]["question"],color='white',font_size=30)
        self.layout.add_widget(self.question_label)

        self.option_buttons = []
        for option in self.questions[self.question_index]["options"]:
                button = Button(text=option,font_size=30,color='black',
                            size_hint=(0.5,0.5),
                            border=(10,10,10,10),
                            pos_hint={"center_x":0.5,"center_y":0.5},
                            background_color=(0,1,1,1)
                            )
                button.bind(on_release=self.check_answer)
                self.option_buttons.append(button)
                self.layout.add_widget(button)

        return self.layout

    def check_answer(self, instance):
        selected_option = instance.text
        correct_option = self.questions[self.question_index]["correct"]

        if selected_option == correct_option:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.question_label.text = self.questions[self.question_index]["question"]
            for button in self.option_buttons:
                button.text = self.questions[self.question_index]["options"][self.option_buttons.index(button)]
        else:
            self.layout.clear_widgets()
            result_label = Label(text=f'Quiz completed!\nYour score: {self.score}/{len(self.questions)}',color='green',font_size=30)
            self.layout.add_widget(result_label)

QuizApp().run()
