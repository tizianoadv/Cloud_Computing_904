import os
import pymysql

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

def get_players_info():

    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)
    
    with cnx.cursor() as cursor:
        cursor.execute('select * from vote;')
        players = cursor.fetchall()
    cnx.close()

    return players

def update_vote(selected_player, vote):

    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password, host=host, db=db_name)

    with cnx.cursor() as cursor:
        new_vote = vote + 1
        query = """UPDATE vote SET player_vote=%s WHERE player_name=%s"""
        variables = (new_vote,selected_player)
        cursor.execute(query,variables)
    cnx.commit()
    cnx.close()