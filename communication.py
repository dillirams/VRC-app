from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MessagingSystem(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        # scrollable area to display messages
        self.message_area = ScrollView()
        self.message_layout = GridLayout(cols=1, size_hint_y=None)
        self.message_layout.bind(minimum_height=self.message_layout.setter('height'))
        self.message_area.add_widget(self.message_layout)
        self.add_widget(self.message_area)

        # text input area for users to enter new messages
        self.new_message = TextInput(multiline=False, size_hint_y=None, height=50)
        self.add_widget(self.new_message)

        #  send button to submit new messages
        self.send_button = Button(text="Send", size_hint_y=None, height=50)
        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)

    def send_message(self, instance):
        # Get the user's message from the text input area
        message_text = self.new_message.text

        # Create a new label to display the message in the message area
        message_label = Label(text=message_text, size_hint_y=None, height=50)

        # Add the new message label to the message layout
        self.message_layout.add_widget(message_label)

        # Clear the text input area
        self.new_message.text = ""


class MessagingApp(App):

    def build(self):
        return MessagingSystem()


if __name__ == '__main__':
    MessagingApp().run()