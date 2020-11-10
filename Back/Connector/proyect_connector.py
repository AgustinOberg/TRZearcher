from Back.Connector.spyder_connector import Connector

__data = []
with open("./Back/Connector/temp_connector.txt", "r") as data_connector:
    for data in data_connector:
        __data.append(str(data).strip())

Connector(__data[0], __data[1], __data[2], __data[3], __data[4], __data[5], __data[6]).execute_connector()
