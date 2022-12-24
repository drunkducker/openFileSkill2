import subprocess

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler

class OpenFileSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        
    def open_file(self, filename):
        """Opens the specified file in a text editor."""
        subprocess.run(["gedit", filename])
    
    @intent_handler(IntentBuilder("OpenFileIntent").require("filename"))
    def handle_open_file_intent(self, message):
        """Handles the OpenFileIntent intent."""
        # Extract the filename from the message
        filename = message.data.get("filename")
        
        # Open the file in a text editor
        self.open_file(filename)
        
        # Send a response back to the user
        self.speak_dialog("file.opened", {"filename": filename})

def create_skill():
    return OpenFileSkill()
