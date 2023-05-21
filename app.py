import tkinter
import customtkinter as ctk

from PIL import Image
import pytesseract as ptsr

import easygui

filetypes = ['.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg',
             '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm',
             '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm']

languages_list = {
        'English': 'eng',
        'Françias': 'fra',
        'Русский': 'rus'
}

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

class TextWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title('Custom Text Window')
        self.resizable(False, False)
        self.language = 'eng'

        ## Main frame
        self.main_frame = ctk.CTkFrame(master=self, fg_color='transparent')
        self.main_frame.grid(row=1, column=0, padx=(10, 10), sticky='nsew')
        

        ## Input frame
        self.input_frame = ctk.CTkFrame(master=self)
        self.input_frame.grid(row=2, column=0, sticky='ew', padx=(10, 10), pady=(10, 0))

        # input field label
        self.inputf_label = ctk.CTkLabel(master=self.input_frame, text='path:')
        self.inputf_label.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))

        # input field
        self.input_field = ctk.CTkEntry(master=self.input_frame, width=567)
        self.input_field.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), sticky='w')

        # explorer button
        self.explorer_button = ctk.CTkButton(master=self.input_frame, 
                                             text='explorer', 
                                             height=4, width=70, 
                                             command=self.open_explorer)
        self.explorer_button.grid(row=2, column=1, padx=(5, 0), pady=(2, 5), sticky='w')

        # clipboard button
        self.clipboard_button = ctk.CTkButton(master=self.input_frame,
                                              text='clipboard',
                                              height=4, width=70,
                                              command=self.clipboard_add)
        self.clipboard_button.grid(row=2, column=1, padx=(80, 0), pady=(2, 5), sticky='w')
        

        ## Text fields
        self.text_widget1 = ctk.CTkTextbox(master=self.main_frame, width=300, height=500)
        self.text_widget1.grid(row=2, column=0, padx=(0, 5), pady=(20, 0))

        self.text_widget2 = ctk.CTkTextbox(master=self.main_frame, width=300, height=500)
        self.text_widget2.grid(row=2, column=1, padx=(5, 0), pady=(20, 0))
        
        ## Button frame
        self.button_frame = ctk.CTkFrame(master=self, fg_color='transparent')
        self.button_frame.grid(row=1, column=1, padx=(0, 0), sticky='sew')
        
        # language selection menu
        self.language_var = ctk.StringVar(master=self.button_frame)
        self.language_menu = ctk.CTkOptionMenu(master=self.button_frame,
                                               values=list(languages_list.keys()), 
                                               command=self.option_menu_callback, 
                                               width=165)
        self.language_menu.grid(row=0, column=0, padx=(0, 0), pady=(90, 0))
        self.language_menu.set('English')

        # button to read text
        self.read_button = ctk.CTkButton(master=self.button_frame, text='Read Text', command=self.read_text, width=165)
        self.read_button.grid(row=1, column=0, padx=(0, 0), pady=(335, 0))
        
        # translate button
        self.translate_button = ctk.CTkButton(master=self.button_frame, 
                                              text='Translate', 
                                              command=self.translate_text, width=165)
        self.translate_button.grid(row=2, column=0, padx=(0, 0), pady=(10, 0))

    def check_filetype(self, file_path: str) -> bool:
        if file_path[file_path.find('.')::] in filetypes:
            return True
        return False 
   
    def clipboard_add(self):
        pass

    def open_explorer(self):
        self.input_field.delete(0, 100)
        self.input_field.insert(0, easygui.fileopenbox(filetypes=filetypes))

    def option_menu_callback(self, choice: str):
        self.language = languages_list[choice]

    def read_text(self, *args, **kwargs):
        file_path = self.input_field.get()

        if file_path != '' and self.check_filetype(file_path):
            try:
                main_img = Image.open(file_path)
                width, height = main_img.size
                new_size = (width * 2, height * 2)
                main_img = main_img.resize(new_size)
                main_img.save('/home/pumukun/GitHub/ImgToTxt2/test_img/anal.png')
            except:
                self.input_field.delete(self, 0, 100)
                self.input_field.insert(0, '*Incorrect image*')
            result = ptsr.image_to_string(main_img, lang=self.language, config='--psm 3')
            self.text_widget1.delete('0.0', '1000.0')
            self.text_widget1.insert('1.0', text=result)
        else:
            self.input_field.delete(0, 100)
            self.input_field.insert(0, '*Incorrect filetype*')
    
    def translate_text(self):
        pass

    


if __name__ == '__main__':
    app = TextWindow()
    app.mainloop()
