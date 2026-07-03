import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")
def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(app, from_=0, to=100, command=slider_event)