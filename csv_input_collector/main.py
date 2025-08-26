from tkinter import *
import pandas
import os
windows = Tk()
windows.config (bg = "black")
windows.minsize(width= 700, height= 400)
windows.title("CSV COLLECTOR")

label_title = Label(text= "CSV PROCESSOR", font= ("georgia", 20), bg= "black", fg= "white")
label_title.pack(side="top")

ID_title = Label(text= "ID: ", font= ("georgia", 12), bg= "black", fg= "white")
ID_title.pack(side="top")
id = Entry()
id.pack()

firstname_label = Label(text= "first name: ", font= ("georgia", 10), bg= "black", fg= "white")
firstname_label.pack(side="top")
first_name = Entry()
first_name.pack()

lastname_label = Label(text= "last name: ", font= ("georgia", 10), bg= "black", fg= "white")
lastname_label.pack(side="top")
last_name = Entry()
last_name.pack()

age_label = Label(text= "age: ", font= ("georgia", 10), bg= "black", fg= "white")
age_label.pack(side="top")
age = Entry()
age.pack()

csv_complete = Label(text= "enter data", font= ("georgia", 10))
csv_complete.pack(side= "bottom", anchor= "se")
 
creator = Label(text= "created by Hakuryu Acosta Kato",font= ("georgia", 7), bg= "black", fg= "white")
date = Label(text= "date: 08/26/2025", font= ("georgia", 7), bg= "black", fg= "white")
creator.pack(side= "bottom", anchor= "nw")
date.pack(side= "bottom", anchor= "nw")

def event_process():
    data_validation = id.get().lower()
    get_firstname = first_name.get().lower()
    get_lastname = last_name.get().lower()
    get_age = age.get().lower()
    df = pandas.DataFrame([[int(data_validation), get_firstname, get_lastname, int(get_age)]], columns= ["ID", "first_name", "last_name", "age"])
    pd =pandas.read_csv("csv_file.csv")
    if len(data_validation) == 9 and data_validation.isdigit() and  get_age.isdigit() and (data_validation) not in pd["ID"].values and not data_validation in pd["ID"].astype(str).values:

        df.to_csv("csv_file.csv", mode= "a", index= False, header= not os.path.exists("csv_file.csv"))
        csv_complete.config(text= "processes complete!", fg= "blue")

    else:
        csv_complete.config(text= "invalid csv", fg= "red")
    
    

button = Button(text= "please click to process", font=("georgia", 12), bg= "red", fg= "white", command= event_process)
button.pack(side= "bottom")

windows.mainloop()
