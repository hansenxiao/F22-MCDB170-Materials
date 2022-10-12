class TrafficLight:
    '''This is an class traffic lights'''
    # Class variable
    traffic_light_address = 'UCSB Campus Beachpoint'
    color = ''

    def __init__(self, color):
        # Instance variable assigned inside the class constructor
        self.color = color

    def action(self):
        if self.color=='red':
            # Instance variable assigned inside a class method
            self.next_color = 'yellow'
            print('Stop & wait')
        elif self.color=='yellow':
            self.next_color = 'green'
            print('Prepare to stop')
        elif self.color=='green':
            self.next_color = 'red'
            print('Go')
        else:
            self.next_color = 'Whisky'
            print('Stop drinking :P')