from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\HP\\PycharmProjects\\practice\\configurations\\config.ini")
    return config.get(category, key)
