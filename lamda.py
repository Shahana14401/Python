s=lambda a:a*a
r=lambda l,w:l*w
t=lambda b,h:1/2*b*h
a=int(input("Enter the side of the square:"))
print("Area of square is:",s(a))
l=int(input("Enter the height of the rectangle:"))
w=int(input("Enter the width of the rectangle:"))
print("Area of rectangle is:",r(l,w))
h=int(input("Enter the height of the triangle:")) 
b=int(input("Enter the width of the triangle:"))
print("Area of triangle is:",t(b,h))
