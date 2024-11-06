import turtle
import time

def draw_triangle(vertices, color, my_turtle, steps=20):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()

    # 平滑過渡移動到每個頂點
    smooth_move(my_turtle, vertices[0], vertices[1], steps)
    smooth_move(my_turtle, vertices[1], vertices[2], steps)
    smooth_move(my_turtle, vertices[2], vertices[0], steps)

    my_turtle.end_fill()

def smooth_move(turtle, start, end, steps):
    x0, y0 = start
    x1, y1 = end
    dx = (x1 - x0) / steps
    dy = (y1 - y0) / steps

    for _ in range(steps):
        x0 += dx
        y0 += dy
        turtle.goto(x0, y0)
        time.sleep(0.01)  # 減少延遲以增加平滑感

def sierpinski(vertices, level, my_turtle):
    colors = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(vertices, colors[level], my_turtle)
    if level > 0:
        sierpinski([vertices[0],
                    get_mid(vertices[0], vertices[1]),
                    get_mid(vertices[0], vertices[2])],
                   level-1, my_turtle)
        sierpinski([vertices[1],
                    get_mid(vertices[0], vertices[1]),
                    get_mid(vertices[1], vertices[2])],
                   level-1, my_turtle)
        sierpinski([vertices[2],
                    get_mid(vertices[2], vertices[1]),
                    get_mid(vertices[0], vertices[2])],
                   level-1, my_turtle)

def get_mid(point1, point2):
    return ((point1[0]+point2[0])/2, (point1[1]+point2[1])/2)

def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    turtle.bgcolor('black')
    vertices = [[-200, -100], [0, 200], [200, -100]]
    level = 3  # 調整迭代層數
    sierpinski(vertices, level, my_turtle)
    turtle.done()

if __name__ == '__main__':
    main()
