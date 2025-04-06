import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()


def main():
    while True:
        try:
            order = int(input("Enter the order of the Koch curve: "))
            if order >= 0:
                break
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            size = int(input("Enter the size of the Koch curve: "))
            if size > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    draw_koch_curve(order, size)

if __name__ == "__main__":
    main()

