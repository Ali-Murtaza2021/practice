class MyCar (object):
    condition  = "new"
    def __init__(self,model,color,mpg):
        """  
            "Car discription."
        >>> @param : model -> [str]    The models of the car.
        >>> @param : color -> [str]    The color of the car.
        >>> @param : mpg   -> [float]  The miles per gallon of the
                                       car.

        """
        self.model = model
        self.color = color
        self.mpg   = mpg
    def dispaly_car(self):
        """
           "display_car"
        >>> @param :  -> [float,str]color,model,mgp
        >>> @return : ->The return statement return the three
                      values from the display_car.  
        """

        return ("This is a %s %s car with %s MGP.") %(self.color,self.model,self.mpg)
    def drive_car(self):
        self.condition="used"

class ElectricCar(Car):
    """
       Module to perform the electric car system
    """
    def __init__(self, model, color, mpg, battery_type):
        self._model          = model
        self._color          = color
        self._mpg            = mpg
        self._battery_type   = battery_type
    def drive_car(self):
        self.condition="like new"

my_car = ElectricCar("DeLorean", "silver", 88,"molten salt")

print (MyCar.condition())
my_car.drive_car()
print (my_car.condition)