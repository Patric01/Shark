import turtle

# Creăm un obiect Turtle
shark = turtle.Turtle()

# Setăm viteza desenului
shark.speed(2)

# Setăm culoarea peniței pentru contur
shark.color("black")

# Setăm culoarea de umplere pentru corpul rechinului
shark.begin_fill()
shark.color("#5e5e5e")  # Gri închis
shark.circle(100)
shark.end_fill()

# Desenăm aripa dreaptă
shark.penup()
shark.goto(30, 30)
shark.pendown()
shark.begin_fill()
shark.color("#5e5e5e")  # Gri închis
shark.goto(150, 40)
shark.goto(120, -30)
shark.goto(30, 30)
shark.end_fill()

# Desenăm aripa stângă
shark.penup()
shark.goto(-30, 30)
shark.pendown()
shark.begin_fill()
shark.color("#5e5e5e")  # Gri închis
shark.goto(-150, 40)
shark.goto(-120, -30)
shark.goto(-30, 30)
shark.end_fill()

# Desenăm înotătoarea dorsală
shark.penup()
shark.goto(0, 80)
shark.pendown()
shark.begin_fill()
shark.color("#333333")  # Gri închis
shark.goto(0, 160)
shark.goto(30, 130)
shark.goto(0, 80)
shark.end_fill()

# Desenăm înotătoarea caudală
shark.penup()
shark.goto(80, -30)
shark.pendown()
shark.begin_fill()
shark.color("#333333")  # Gri închis
shark.goto(140, -50)
shark.goto(160, -100)
shark.goto(80, -30)
shark.end_fill()

# Desenăm gura
shark.penup()
shark.goto(-10, -10)
shark.pendown()
shark.circle(35, 180)

# Desenăm ochiul drept
shark.penup()
shark.goto(20, 60)
shark.pendown()
shark.begin_fill()
shark.color("white")
shark.circle(15)
shark.end_fill()

# Desenăm pupila dreaptă
shark.penup()
shark.goto(20, 60)
shark.pendown()
shark.begin_fill()
shark.color("black")
shark.circle(7)
shark.end_fill()

# Desenăm ochiul stâng
shark.penup()
shark.goto(-20, 60)
shark.pendown()
shark.begin_fill()
shark.color("white")
shark.circle(15)
shark.end_fill()

# Desenăm pupila stângă
shark.penup()
shark.goto(-20, 60)
shark.pendown()
shark.begin_fill()
shark.color("black")
shark.circle(7)
shark.end_fill()

# Ascundem obiectul Turtle
shark.hideturtle()

# Păstrăm fereastra deschisă până când este închisă manual
turtle.done()

