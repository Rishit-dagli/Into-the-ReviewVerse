from mysql.connector import connect, MySQLConnection
from mysql.connector.cursor import MySQLCursor


def get_connection(autocommit: bool = True) -> MySQLConnection:
    connection = connect(
        host="gateway01.eu-central-1.prod.aws.tidbcloud.com", user="3Hm9NyBr4AkTTFJ.root", password="sYz7jHuK7qU0wOB6", port=4000, database="test",
        autocommit=autocommit,
        ssl_ca='<ca_path>',
        ssl_verify_identity=True
    )
    connection.autocommit = autocommit
    return connection

def ex():
    with get_connection(autocommit=True) as connection:
        with connection.cursor() as cur:
            cur.execute("CREATE TABLE reviewData (product VARCHAR(255), store VARCHAR(255), reviewNums VARCHAR(255))")

ex()