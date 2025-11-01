import psycopg2


class DBManager:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
    

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
        )
        self.cursor = self.connection.cursor()
        return self
    def __exit__(self,ex_type,ex_value,ex_traceback):
        self.connection.commit()
        self.connection.close()


