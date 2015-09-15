import qingcloud.iaas


class API_Connection(object):
    # access_key_id = "OVNQCDZGCMAMQCYQZTPQ"
    access_key_id = "MGJYTHJRQYNGAOHKCQPK"
    # secret_access_key = "fZmFLDKjswA5ZobyPfmFPgvXXNubgPcJ2QRevVs8"
    secret_access_key = "WalqP1YzFK2tFMI2qm9EA1YDezLGFis9NQSd7ir5"

    def get_connection(self, zone ):
        conn = qingcloud.iaas.connect_to_zone(
                                          zone,
                                          self.access_key_id,
                                          self.secret_access_key)
        return conn

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #
    #         orig = super(API_Connection, cls)
    #         cls._instance = orig.__new__(cls, *args, **kwargs)
    #     return cls._instance
