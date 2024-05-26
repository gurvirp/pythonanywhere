import requests
import sys
import json
import time

from database_manager.database_manager import Database_Manager

class Historic_Data_Manager:

    def __init__(self,theDatabaseManager):
        self.theDatabaseManager = theDatabaseManager
        pass

    def updateHistoricData(self):
        print("Getting F1 Champions Data")
        championsData = self.obtainF1ChampionsData()

        for champion in championsData:
            year = int(champion["season"])
            for driver in champion['DriverStandings']:
                driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
                print({year},{driver_name})


    def obtainF1ChampionsData(self):
        try:
            # Ergast API URL for driver standings
            ergast_url = "http://ergast.com/api/f1/driverStandings/1.json?limit=100"

            response = requests.get(ergast_url)
            response.raise_for_status()  # Raise an exception if the request fails
            data = response.json()

            champions_data = []
            for driver in data["MRData"]["StandingsTable"]["StandingsLists"]:
                champions_data.append(driver)



            return champions_data
        except requests.RequestException as e:
            print(f"Error fetching data from Ergast API: {e}")
            return []

