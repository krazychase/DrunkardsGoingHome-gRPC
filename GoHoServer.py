'''
Go Home Server
Chase Brown
'''
import grpc
from concurrent import futures
import protobufs.goho_pb2 as pb2
import protobufs.goho_pb2_grpc as pb2_grpc
from pathlib import Path
import sqlite3

from user import User
from ride import Ride

class GoHoService(pb2_grpc.GoHoServiceServicer):
    '''
    gRPC Service
    '''
    def __init__(self):
        self.db = Path().cwd() / 'data' / 'data.db'

    def GetUser(self, request, context):
        '''
        Returns User information
        '''
        userID = request.userid
        with sqlite3.connect(self.db) as conn:      # Get user info from DB
            cur = conn.cursor()
            sql, params = '''   SELECT *
                                FROM Users
                                WHERE UserID=? ''', (userID,)
            cur.execute(sql, params)
            data = cur.fetchone()
        user = User(data[0], data[1], data[2], data[3])
        response = {'userid':user.userid, 'username':user.username, 'password':user.password, 
                    'home_location':user.homeLocation}

        return pb2.User(**response)

    def AddUser(self, request, context):
        '''
        Adds user to DB
        Returns confirmation
        '''
        user = User(None, request.username, request.password, request.home_location)
        with sqlite3.connect(self.db) as conn:      # Add user to DB
            cur = conn.cursor()
            sql, params = '''   INSERT INTO Users
                                VALUES (?,?,?,?) ''', (user.userid, user.username, user.password, user.homeLocation)
            cur.execute(sql, params)
            conn.commit()
            sql = '''   SELECT MAX(UserID)
                        FROM Users '''      # Get newest user
            cur.execute(sql)
            newestUser = cur.fetchone()[0]
        response = {'response':f'User {newestUser}', 'code':0}

        return pb2.Confirmation(**response)

    def GetRide(self, request, context):
        '''
        Returns ride information
        '''
        rideid = request.rideid
        with sqlite3.connect(self.db) as conn:      # Get user info from DB
            cur = conn.cursor()
            sql, params = '''   SELECT *
                                FROM Rides
                                WHERE RideID=? ''', (rideid,)
            cur.execute(sql, params)
            data = cur.fetchone()
        ride = Ride(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        response = {'rideid':ride.rideid, 'rider':ride.rider, 'driver':ride.driver, 
                    'destination':ride.destination, 'location':ride.location, 'time':ride.time, 
                    'status':ride.status}

        return pb2.Ride(**response)

    def AddRide(self, request, context):
        '''
        Adds ride to DB
        Returns confirmation
        '''
        ride = Ride(None, request.rider, request.driver, request.destination, 
                    request.location, request.time, request.status)
        with sqlite3.connect(self.db) as conn:      # Add ride to DB
            cur = conn.cursor()
            sql, params = '''   INSERT INTO Rides
                                VALUES (?,?,?,?,?,?,?) ''', (ride.rideid, ride.rider, ride.driver, 
                                            ride.destination, ride.location, ride.time, ride.status)
            cur.execute(sql, params)
            conn.commit()
            sql = '''   SELECT MAX(RideID)
                        FROM Rides '''      # Get newest ride
            cur.execute(sql)
            newestRide = cur.fetchone()[0]
        response = {'response':f'Ride {newestRide}', 'code':0}

        return pb2.Confirmation(**response)

    def UpdateRide(self, request, context):
        '''
        Updates ride on DB
        Returns Confirmation
        '''
        ride = Ride(request.rideid, request.rider, request.driver, request.destination, 
                    request.location, request.time, request.status)

        rideDict = {}       # Determine what info to update
        if ride.rider:
            rideDict['Rider'] = ride.rider
        if ride.driver:
            rideDict['Driver'] = ride.driver
        if ride.destination:
            rideDict['Destination'] = ride.destination
        if ride.location:
            rideDict['Location'] = ride.location
        if ride.time:
            rideDict['Time'] = ride.time
        if ride.status:
            rideDict['Status'] = ride.status

        with sqlite3.connect(self.db) as conn:      # Update ride in DB
            cur = conn.cursor()
            # TODO: Figure out a better way to do dynamic updates
            for field, data in rideDict.items():
                sql, params = f'''  UPDATE Rides
                                    SET {field} = ?
                                    WHERE rideid = ? ''', (data,ride.rideid)
                cur.execute(sql, params)
            conn.commit()
        response = {'response':f'Ride {ride.rideid}', 'code':0}

        return pb2.Confirmation(**response)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GoHoServiceServicer_to_server(GoHoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()