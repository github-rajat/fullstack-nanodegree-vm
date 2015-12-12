import turtle
import math

def triangle(t,a,k):
  if k==3:    
    t.fill(True)
    for i in range(1,4):
      t.forward(a)
      t.left(120)
    t.fill(False)
  else:
    triangle(t,a/2,k+1)
    t.forward(a/2)
    triangle(t,a/2,k+1)
    t.left(120)
    t.forward(a/2)
    t.right(120)
    triangle(t,a/2,k+1)
    t.right(120)
    t.forward(a/2)
    t.left(120)    
  

def main():
  bud = turtle.Turtle()
  window = turtle.Screen()
  window.bgcolor("white")
  bud.color("green")
  triangle(bud,200,0)
  window.exitonclick()

if __name__ == '__main__':
  main()
  
  
