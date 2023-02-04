import tkinter
import customtkinter
from automata import Automata


class App:
    def __init__(self):
        self.tkinter = tkinter
        self.custom_tkinter = customtkinter
        self.automata = Automata()

    def app_run(self):

        # SET SCREEN MODE
        self.custom_tkinter.set_appearance_mode("dark")

        self.automata.save_data()

        # SET UI THEME
        self.custom_tkinter.set_default_color_theme("green")

        # CALL CUSTOMTKINTER APP
        app = self.custom_tkinter.CTk()

        app.title('AUTOMATA')

        # SET SCREEN SIZE
        app.geometry("1080x920")

        # APP DEVELOPMENT START
        app.mainloop()


if __name__ == '__main__':
    # ENTRY APP START
    app = App()
    app.app_run()