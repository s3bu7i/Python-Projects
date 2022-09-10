from optparse import Values
import PySimpleGUIQt as sg

form = sg.FlexForm("My GUI")
layout = [ [sg.Text('Enter your name' , size = (15,1)) , sg.InputText()],
           [sg.Text('Enter your surname' , size = (15,1)) , sg.InputText()],
           [sg.Text('Enter your phone' , size = (15,1)) , sg.InputText()],
           [sg.Text('Enter your age ' , size = (15,1)) , sg.InputText()],
           [sg.OK() , sg.Cancel()] ]

button , values = form.Layout(layout).Read()
name = values[0]
surname = values[1]
phone = values[2]
age = values[3]

print(f"""
    Name :{name}
    Surname :{surname} 
    Phone :{phone} 
    Age :{age}
    """)


#window = s.Window(title="MyGUI" , size=(600,480) , layout = [[s.Text("")] , [s.Button("Click me")]])
#window.read()
