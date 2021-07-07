class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.trip = defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, checkin_station: str, t: int) -> None:
        '''
        T: O(1) and S: O(n); n = # of visitors
        '''
        self.checkin[id] = [checkin_station, t]

    def checkOut(self, id: int, checkout_station: str, t: int) -> None:
        '''
        T: O(1) and S: O(m^2); m = # of stations; space for each pair of station
        '''
        checkin_station, checkin_time = self.checkin.pop(id)
        self.trip[(checkin_station, checkout_station)][0] += (t - checkin_time)
        self.trip[(checkin_station, checkout_station)][1] += 1

    def getAverageTime(self, checkin_station: str, checkout_station: str) -> float:
        '''
        T: O(1) and S: O(1)
        '''
        trip_time, trip_count = self.trip[checkin_station, checkout_station]
        
        return trip_time / trip_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
