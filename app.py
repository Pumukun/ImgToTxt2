import tkinter
import customtkinter as ctk

languages_list = {
        'English': 'eng',
        'Françias': 'fra',
        'Русский': 'rus'
}

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

languages_list = {
        'English': 'eng',
        'Françias': 'fra',
        'Русский': 'rus'
}

class TextWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Custom Text Window")

        # Create input field
        self.input_field = ctk.CTkEntry(self)
        self.input_field.pack(side=ctk.TOP, pady=10)

        # Create language selection menu
        self.language_var = ctk.StringVar(self)
        self.language_var.set("English")
        self.language_menu = ctk.CTkOptionMenu(self,
                                               values=list(languages_list.keys()))
        self.language_menu.pack(side=ctk.RIGHT, anchor=ctk.N, pady=40)

        # Create text fields
        self.text_widget1 = ctk.CTkTextbox(self, width=300, height=500)
        self.text_widget1.pack(side=ctk.LEFT, padx=10)
        self.text_widget2 = ctk.CTkTextbox(self, width=300, height=500)
        self.text_widget2.pack(side=ctk.LEFT, padx=10)

        # Create button to read text
        self.read_button = ctk.CTkButton(self, text="Read Text", command=self.read_text)
        self.read_button.pack(side=ctk.RIGHT, anchor=ctk.N)

    def read_text(self):
        text1 = self.text_widget1.get("1.0", "end-1c")
        text2 = self.text_widget2.get("1.0", "end-1c")
        print(f"Reading {language} text 1: {text1}")
        print(f"Reading {language} text 2: {text2}")

# Create a new instance of the TextWindow and run the mainloop
if __name__ == '__main__':
    app = TextWindow()
    app.mainloop()
