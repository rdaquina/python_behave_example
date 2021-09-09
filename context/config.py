import os
import json

settings = None
sett_path = os.path

class Settings(object):
    """Simple singleton class for managing and accessing settings"""

    def __init__(self) -> None:
        super().__init__()
        with open(sett_path.join(sett_path.dirname(sett_path.abspath(__file__)), 'testsettings.json')) as sett_file:
            settings = json.load(sett_file)
            self.browser = settings['browser']
            self.portal_url = settings['portal_url']
            
settings = Settings()