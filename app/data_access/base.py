from .cosmos_client_singleton import CosmosDBClientSingleton


class BaseDataAccess:
    def __init__(self, container_name: str) -> None:
        """
        :param db_name: The name of the database to connect to
        :param container_name: The name of the container e.g users
        """
        self.db_name = "set-tracker-db"
        self.container_name = container_name
        self.client = CosmosDBClientSingleton().client
        self.db = self.client.get_database_client(self.db_name)
        self.container = self.db.get_container_client(self.container_name)