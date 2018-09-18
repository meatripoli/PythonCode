#This program calculates the area and perimeter
#of this rectangle
height=input("What is the height of the rectangle?")
lenght=input("What is the length of the rectangle?")
rectangle_height=float(height)
rectangle_width=float(lenght) #width of rectangle
rectangle_area=rectangle_height*rectangle_width
rectangle_perimeter=2*(rectangle_height*rectangle_width)
print("The area of the rectangle is ",rectangle_area)
print("The perimeter of the rectangle is ",rectangle_perimeter)
