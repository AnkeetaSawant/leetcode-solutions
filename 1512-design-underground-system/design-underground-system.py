class UndergroundSystem:

    def __init__(self):
        self.total_time_map = {}
        self.checkin_time_per_cust = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_time_per_cust[id] = (stationName,t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = (self.checkin_time_per_cust[id][0], stationName)
        prev_distance, prev_count = self.total_time_map.get(key,(0,0))
        self.total_time_map[key] = (
            prev_distance + (t -  self.checkin_time_per_cust[id][1]),
            prev_count + 1
        )
        del self.checkin_time_per_cust[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_count = self.total_time_map.get((startStation, endStation))
        return total_time/total_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)