from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\Users\\DELL\\PycharmProjects\\Sprint2\\ConfigurationData\\config.ini")
    return config.get(section, Key)