class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction
        self.prevdirection = direction

    # logic for movement of the spacecraft

    def move_forward(self):
       

    def move_backward(self):
        

    def rotate_left(self):        
      

    def rotate_right(self):
        

    def adjust_angle_up(self):
       

    def adjust_angle_down(self):
        

    # processing the user commands
    
    def process_commands(self, command):    
        if command == 'f':
            self.move_forward()
        elif command == 'b':
            self.move_backward()
        elif command == 'l':
            self.rotate_left()
        elif command == 'r':
            self.rotate_right()
        elif command == 'u':
            self.adjust_angle_up()
        elif command == 'd':
            self.adjust_angle_down()
        else :
            print("Invalid command")

        # Displaying final position and direction
        print("Final Position:", (self.x, self.y, self.z))
        print("Final Direction:", self.direction)