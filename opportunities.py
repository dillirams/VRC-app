import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class AddVolunteerOpportunityScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='Date (MM/DD/YYYY):'))
        self.date = TextInput(multiline=False)
        self.add_widget(self.date)

        self.add_widget(Label(text='Time (HH:MM AM/PM):'))
        self.time = TextInput(multiline=False)
        self.add_widget(self.time)

        self.add_widget(Label(text='Location:'))
        self.location = TextInput(multiline=False)
        self.add_widget(self.location)

        self.add_widget(Label(text='Number of Volunteers Needed:'))
        self.num_volunteers = TextInput(multiline=False)
        self.add_widget(self.num_volunteers)

        self.add_widget(Label())
        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.submit_opportunity)
        self.add_widget(self.submit)

    def submit_opportunity(self, instance):
        date = self.date.text
        time = self.time.text
        location = self.location.text
        num_volunteers = self.num_volunteers.text

        # Show a confirmation message
        print(f"Volunteer opportunity added: {date}, {time}, {location}, {num_volunteers} volunteers needed.")

        # Clear the input fields
        self.date.text = ''
        self.time.text = ''
        self.location.text = ''
        self.num_volunteers.text = ''


class VolunteerOpportunitiesScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text='Volunteer Opportunities'))


        self.add_widget(Button(text='Add Volunteer Opportunity', on_press=self.add_opportunity))

    def add_opportunity(self, instance):
        # Show the "Add Volunteer Opportunity" screen
        self.clear_widgets()
        self.add_widget(AddVolunteerOpportunityScreen())


class VolunteerApp(App):

    def build(self):
        return VolunteerOpportunitiesScreen()

if __name__ == '__main__':
    VolunteerApp().run()