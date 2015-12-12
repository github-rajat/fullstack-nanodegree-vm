#!/usr/bin/python -tt
import turtle

def draw_square():
  window = turtle.Screen()
  window.bgcolor("red")

  t=turtle.Turtle()
  t.shape("turtle")
  t.color("yellow")
  t.speed(6)
  angle = 0
  while angle<360:
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    angle+=5
    t.right(5)
  
  
  window.exitonclick()

def main():
  draw_square()
  

if __name__ == '__main__':
  main()
