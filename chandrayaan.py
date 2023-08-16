class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction
        self.prevdirection = direction

    # logic for movement of the spacecraft

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        if self.direction == 'S':
            self.y -= 1
        if self.direction == 'W':
            self.x += 1
        elif self.direction == 'E':
            self.x -= 1
        if self.direction == 'U':
            self.z += 1
        elif self.direction == 'D':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        if self.direction == 'S':
            self.y += 1
        if self.direction == 'W':
            self.x -= 1
        elif self.direction == 'E':
            self.x += 1
        if self.direction == 'U':
            self.z -= 1
        elif self.direction == 'D':
            self.z += 1


    def rotate_left(self):        
        print("left")


    def rotate_right(self):
        print("right")


    def adjust_angle_up(self):
        print("up")


    def adjust_angle_down(self):
        print("down")



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




# Taking user input
initial_position = (0, 0, 0)
initial_direction = 'N'

chandrayaan_3 = Spacecraft(*initial_position, initial_direction)

while True:
    k = input("Enter your command or Press e to EXIT !")
    if k == "e":
        break
    else:
        chandrayaan_3.process_commands(k)
        