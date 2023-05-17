from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class Shift:
    def __init__(self, volunteer_name, date_time, organization_name):
        self.volunteer_name = volunteer_name
        self.date_time = date_time
        self.organization_name = organization_name

class SchedulingApp(App):
    shifts = []  # list to store the scheduled shifts

    def build(self):
        return ScheduleLayout()

class ScheduleLayout(BoxLayout):
    volunteer_name_input = ObjectProperty(None)
    date_time_input = ObjectProperty(None)
    organization_name_input = ObjectProperty(None)

    def schedule_shift(self):
        volunteer_name = self.volunteer_name_input.text
        date_time = self.date_time_input.text
        organization_name = self.organization_name_input.text

        if volunteer_name == "" or date_time == "" or organization_name == "":
            popup = Popup(title="Missing Information", content=Label(text="Please enter all required fields."), size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            shift = Shift(volunteer_name, date_time, organization_name)
            SchedulingApp.shifts.append(shift)

            popup = Popup(title="Shift Scheduled", content=Label(text="Your shift has been scheduled."), size_hint=(None, None), size=(400, 200))
            popup.open()

    def view_schedule(self):
        schedule_text = ""

        for shift in SchedulingApp.shifts:
            schedule_text += "Volunteer Name: {}\nDate and Time: {}\nOrganization Name: {}\n\n".format(shift.volunteer_name, shift.date_time, shift.organization_name)

        if schedule_text == "":
            popup = Popup(title="No Scheduled Shifts", content=Label(text="You have not scheduled any shifts yet."), size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title="Scheduled Shifts", content=Label(text=schedule_text), size_hint=(None, None), size=(400, 400))
            popup.open()

if __name__ == '__main__':
    SchedulingApp().run()