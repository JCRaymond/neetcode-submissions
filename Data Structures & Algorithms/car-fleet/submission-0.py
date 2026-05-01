class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_idxs = sorted(list(range(len(position))), reverse=True, key=lambda i: position[i])
        
        fleets = 1
        leader_idx = car_idxs[0]
        leader_pos = position[leader_idx]
        leader_vel = speed[leader_idx]
        leader_time = (target - leader_pos) / leader_vel
        
        i = 1
        while i < len(car_idxs):
            car_idx = car_idxs[i]
            car_pos = position[car_idx]
            car_vel = speed[car_idx]
            car_time = (target - car_pos) / car_vel

            if car_time > leader_time:
                fleets += 1
                leader_time = car_time
            
            i += 1
        
        return fleets

