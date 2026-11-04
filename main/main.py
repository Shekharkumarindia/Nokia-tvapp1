import os
from kivy.app import App
from kivy.uix.label import Label

# AUTO CREATE FOLDERS - This fixes your error
def create_folders():
    folders = ["assets", "images", "data", "bin"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

create_folders()

__version__ = "1.0"

class NokiaTVApp(App):
    def build(self):
        return Label(text="NokiaTV Ready\nGitHub Build Success!")

if __name__ == "__main__":
    NokiaTVApp().run()
