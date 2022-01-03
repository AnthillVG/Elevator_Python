class Elevator:
    passenger_list = []
    elevator_capacity = 250

    def add_passenger(self, passenger):
        self.passenger_list.append(passenger)

    def is_overloaded(self):
        sum_weight = 0
        for person in self.passenger_list:
            sum_weight += person.weight
        return sum_weight >= self.elevator_capacity

    def floor_selection(self):
        for person in self.passenger_list:
            person.floor_selection()

    def remove_passenger(self, floor):
        passengers_left = []
        for person in self.passenger_list:
            if floor == person.floor:
                self.passenger_list.remove(person)
                passengers_left.append(person)
        return passengers_left

    def _max_floor(self):
        max_floor = self.passenger_list[0].floor
        for passenger in self.passenger_list:
            if max_floor < passenger.floor:
                max_floor = passenger.floor
        return max_floor

    def elevator_moving(self):
        floor_dict = {}
        for floor in range(1, self._max_floor() + 1):
            passengers_left = self.remove_passenger(floor)
            if len(passengers_left) > 0:
                floor_dict[floor] = passengers_left
        return floor_dict
