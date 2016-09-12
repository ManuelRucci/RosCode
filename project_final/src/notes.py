
class TwistType(object):
    def __init__(self):
        self.init_go_straight()
        self.init_go_right()
        self.init_go_left()
        self.init_stop()
        
    def init_go_straight(self):
        self.GO_STRAIGHT = Twist()
        self.GO_STRAIGHT.linear.x = 0.05
        self.GO_STRAIGHT.linear.y  = 0.0
        self.GO_STRAIGHT.linear.z  = 0.0
        self.GO_STRAIGHT.angular.x  = 0.0
        self.GO_STRAIGHT.angular.y = 0.0
        self.GO_STRAIGHT.angular.z = 0.3
        
    def init_go_left(self):
        self.GO_LEFT = Twist()
        self.GO_LEFT.linear.x = 0.05
        self.GO_LEFT.linear.y  = 0.0
        self.GO_LEFT.linear.z  = 0.0
        self.GO_LEFT.angular.x  = 0.0
        self.GO_LEFT.angular.y = 0.0
        self.GO_LEFT.angular.z = 0.3
        
    def init_go_right(self):
        self.GO_RIGHT = Twist()
        self.GO_RIGHT.lear.x = 0.05
        self.GO_RIGHT.linear.y  = 0.0
        self.GO_RIGHT.linear.z  = 0.0
        self.GO_RIGHT.angular.x  = 0.0
        self.GO_RIGHT.angular.y = 0.0
        self.GO_RIGHT.angular.z = 0.3
        
    def init_stop(self):
        self.STOP = Twist()
        self.STOP.linear.x = 0.05
        self.STOP.linear.y  = 0.0
        self.STOP.linear.z  = 0.0
        self.STOP.angular.x  = 0.0
        self.STOP.angular.y = 0.0
        self.STOP.angular.z = 0.3
    
    def get_direction(self, direction):
        if (direction == "GO_STRAIGHT"):
            return self.GO_STRAIGHT
        elsif (direction == "GO_LEFT"):
            return self.GO_LEFT
        elsif (direction == "GO_RIGHT"):
            return self.GO_RIGHT
        elsif (direction == "STOP"):
            return self.STOP


def MotionPlanning(Action):
    
    if ( Action == 1 ):
        return "GO_STRAIGHT"
                
    elif ( Action == 2):
        return "GO_RIGHT"
            
    elif ( Action == 3):
        return "GO_STRAIGHT"
            
    elif ( Action == 4 ):
        return "GO_LEFT"
            
    elif (Action == 5):
        return "GO_STRAIGHT"
            
    else:
        return "STOP"