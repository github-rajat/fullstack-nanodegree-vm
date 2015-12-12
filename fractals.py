import turtle

def fractals(t,order,size):
  if order==0:
    t.forward(size)
  else:
    fractals(t,order-1,size/3)
    t.left(60)
    fractals(t,order-1,size/3)
    t.right(120)
    fractals(t,order-1,size/3)
    t.left(60)
    fractals(t,order-1,size/3)

def main():
  
  bud = turtle.Turtle()
  window = turtle.Screen()
  window.bgcolor("green")
  bud.color("white")
  bud.goto(-200,0)
  fractals(bud,3,600)
  window.exitonclick()

if __name__ == '__main__':
  main()
