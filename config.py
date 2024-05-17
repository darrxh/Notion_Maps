from json import dumps, load

class Config():

    def __init__(self):
        self.settings = {}
        self.interval = 3600

    def reset_settings(self):
        self.settings["delete_duplicates"] = False
        self.settings["delete_closed"] = False
        self.settings["autofill_properties"] = False

    # loader for config.json file
    def config_fetcher(self):
        try:
            config_file = open('./config.json', 'r')
            json_object = load(config_file)
        except FileNotFoundError:
            print(f"No config.json file found. ")
            self.create_config()
        else:
            config_file.close()
            return json_object

    # loads config.json values / Initializes a config.json file if one is not found
    def load_config(self):
        json_object = self.config_fetcher()
        if (json_object == None):
            return
        self.interval = json_object["interval"]
        self.settings = json_object["settings"]

    def update_config(self):
        new_file = open('config.json', 'w')
        json_object = dumps(self.__dict__, indent=2)
        new_file.write(json_object)
        new_file.close()

    def create_config():
        print(f"Creating new config.json file.")
        new_file = open('config.json', 'x')
        new_file.close()
        print("New config.json file created. Type and enter 'help' for info on adding players and servers.")
