import kivy
from kivy.app import App
from kivy.uix.label import Label
from  kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initializez the infinite keywords
    def __init__(self,**kwargs):
        #call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)
        # set columns9
        self.cols=1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        #lets create second gridlayout taht will span the submmit buttom
        self.top_grid=GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=300
        )
        self.top_grid.cols=2

        self.top_grid.add_widget(Label(text="name: ",

                                       #font_size=32,
                                      # size_hint_y=None,
                                       #height=50,
                                       #size_hint_x=None,
                                       #width=400
                                       ))
        # add input box
        self.name=TextInput(multiline=False,
                           # font_size=32,
                           # size_hint_y=None,
                           # height=50,
                           # size_hint_x=None,
                           # width=800
                            )
        #if the name is lengthy and writen in multiline than it will return false
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(text="village: "))
        # add input box
        self.village = TextInput(multiline=False)
        self.top_grid.add_widget(self.village)
        self.top_grid.add_widget(Label(text="dzongkag: "))
        # add input box
        self.dzongkag = TextInput(multiline=False)
        self.top_grid.add_widget(self.dzongkag)

        self.top_grid.add_widget(Label(text="email: "))
        # add input box
        self.email = TextInput(multiline=False)
        self.top_grid.add_widget(self.email)
        self.top_grid.add_widget(Label(text="contct no: "))
        # add input box
        self.contact= TextInput(multiline=False)
        self.top_grid.add_widget(self.contact)
        self.top_grid.add_widget(Label(text="cid: "))
        # add input box
        self.cid = TextInput(multiline=False)
        self.top_grid.add_widget(self.cid)

        #add the new top_grid to our app
        self.add_widget(self.top_grid)

        #lets create the submit buttom
        self.submit=Button(text="submit",
            font_size=32,
            size_hint_y=None,
            height=50,
            size_hint_x=None,
            width=100
                           )
        #we have the submit buttom but doesnt do anythong so do it we bind the buttom
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name=self.name.text
        village=self.village.text
        dzongkag=self.dzongkag.text
        qualification=self.qualification.text
        self.add_widget(Label(text=f"hello {name},your data provides that you are from {village},{dzongkag} and your qualification is {qualification}"))

        print(f"hello {name},your data provides that you are from {village},{dzongkag} and your qualification is {qualification}")
        # after pressing the submit clear the boxes
        self.name.text=" "
        self.dzongkag.text=" "
        self.village.text=" "
        self.qualification.text=" "

class MyApp(App):
    def build(self):
        return MyGridLayout()



if __name__=='__main__':
    MyApp().run()


