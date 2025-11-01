from database import DB_connect
from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        cnx=DB_connect.get_connection()
        if cnx is None:
            return None
        cursor = cnx.cursor()
        query="SELECT * FROM automobile"
        cursor.execute(query)
        automobili=[]
        for row in cursor:
            auto=Automobile(row[0], row[1], row[2], row[3], row[4],row[5])
            automobili.append(auto)
        cursor.close()
        cnx.close()
        return automobili

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        cnx=DB_connect.get_connection()
        if cnx is None:
            return None
        cursor = cnx.cursor()
        query=f'SELECT * FROM automobile WHERE modello="{modello}"'
        cursor.execute(query)
        risultato=[]
        for row in cursor:
            auto=Automobile(row[0], row[1], row[2], row[3], row[4],row[5])
            risultato.append(auto)
        cursor.close()
        cnx.close()
        return risultato


