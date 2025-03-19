import configparser
# import mysql.connector
# from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

# connect_config = {
#     'user': getConfig()['SQL']['user'],
#     'password': getConfig()['SQL']['password'],
#     'database': getConfig()['SQL']['database'],
#     'host': getConfig()['SQL']['host']
# }
def getPassword():
    return "Monty@9358"

# def getDBConnection():
#     try:
#         conn = mysql.connector.connect(**connect_config)
#         if conn.is_connected():
#             print("connection successful")
#             return conn
#
#     except Error as e:
#         print(e)

