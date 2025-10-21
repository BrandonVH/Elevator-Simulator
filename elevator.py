# FEATURES INCLUDED:
# 1. THE NUMBER OF FLOORS IN THE BUILDING MUST BE BETWEEN 1 AND 100 IN ORDER FOR THE ELEVATOR TO FUNCTION (doesn't make sense for an elevator to exist in a 1 floor building, and 100 floors is unrealistic)
# 2. THE ELEVATOR PRIORITIZES THE OLDEST REQUEST WHEN THERE ARE REQUESTS FOR FLOORS BOTH ABOVE AND BELOW THE CURRENT FLOOR

# FEATURES NOT INCLUDED:
# 1. THE ELEVATOR CANNOT TAKE REQUESTS FOR FLOORS WHILE IT IS MOVING. IT MUST BE STOPPED AT A FLOOR BEFORE IT CAN PROCESS REQUESTS

class Elevator():
    def __init__(self, floors):
        if not isinstance(floors, int):
            raise ValueError('Number of floors must be an integer')
        if floors > 100 or floors <= 1:
            raise ValueError('Number of floors is not valid')
        self.floors = floors # number of floors
        self.direction = True # True signifies the elevator is going up 
        self.stops = [] # floors the elevator needs to stop at
        self.current = 1 # current floor the elevator is on
        
    def request_floor(self, floor):
        if floor < 1 or floor > self.floors:
            print(f"Invalid floor: {floor}")
        elif floor == self.current:
            print(f"You are already on floor {floor}.")
        elif floor not in self.stops:
            self.stops.append(floor)
            print(f"Floor {floor} added to stops.")
        else:
            print(f"Floor {floor} is already in the queue.")
            
    # Switch direction if all requests are above/below current floor, otherwise, prioritize the oldest request
    def choose_direction(self):
        if not self.stops:
            return
        if all(floor < self.current for floor in self.stops):
            self.direction = False
        elif all(floor > self.current for floor in self.stops):
            self.direction = True
        else:
            if self.current < self.stops[0]:
                self.direction = True
            else:
                self.direction = False

    def move(self):
        self.choose_direction()
        
        if self.direction:
            self.current += 1
        else:
            self.current -= 1
        print(f"Elevator moved to floor {self.current}.")

        if self.current in self.stops:
            print(f"Stopping at floor {self.current}. Doors opening...")
            self.stops.remove(self.current)
            print("Doors closing...")

    def initiate(self):
        print("Elevator initialized. Type 'exit' to stop.")
        while True:
            user_input = input("\nEnter a floor to request or press Enter to move: ")
            if user_input.lower() == 'exit':
                print("Shutting down elevator.")
                break
            elif user_input.strip().isdigit():
                self.request_floor(int(user_input))
            else:
                if self.stops:
                    self.move()
                else:
                    print("No pending stops. Elevator is idle at floor", self.current, '\n')
            
if __name__ == '__main__':
    while True:
        floors = input("How many floors are in the building: ")
        if floors.strip().isdigit():
            if int(floors.strip()) > 100 or int(floors.strip()) <= 1:
                raise ValueError('Number of floors is not valid')
            break
        else:
            print("Enter a valid number")
        
    elevator = Elevator(int(floors.strip()))
    elevator.initiate()
    
    
    
    
    
    
    
    
    
    
    
    
            
