from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ReportScreen(BoxLayout):
    def __init__(self, orgs, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.orgs = orgs

        self.report_label = Label(text="Report for All Organizations\n", font_size=30)
        self.add_widget(self.report_label)

        self.total_volunteers = 0
        self.total_hours = 0

        for org in orgs:
            self.total_volunteers += org["volunteers"]
            self.total_hours += org["hours"]
            org_label = Label(text="Report for " + org["name"] + "\nVolunteers: " + str(org["volunteers"]) + "\nHours: " + str(org["hours"]), font_size=20)
            self.add_widget(org_label)

        self.total_label = Label(text="\nTotal Volunteers: " + str(self.total_volunteers) + "\nTotal Hours: " + str(self.total_hours), font_size=30)
        self.add_widget(self.total_label)

class MainScreen(BoxLayout):
    def __init__(self, orgs, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.orgs = orgs

        self.report_btn = Button(text="Generate Reports", font_size=25)
        self.report_btn.bind(on_press=self.show_report)
        self.add_widget(self.report_btn)

    def show_report(self, instance):
        report_screen = ReportScreen(orgs=self.orgs)
        self.clear_widgets()
        self.add_widget(report_screen)

class MyApp(App):
    def __init__(self, orgs, **kwargs):
        super().__init__(**kwargs)
        self.orgs = orgs

    def build(self):
        return MainScreen(orgs=self.orgs)

if __name__ == '__main__':
    orgs = [{"name": "Org A", "volunteers": 10, "hours": 40},
            {"name": "Org B", "volunteers": 20, "hours": 80},
            {"name": "Org C", "volunteers": 15, "hours": 60}]

    MyApp(orgs=orgs).run()