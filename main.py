#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import turtle  # 使用turtle画图
from random import randint

# 地图尺寸
WIDTH = 20
HEIGHT = 20

# 图块大小
BLOCK_SIZE = 10

# 蛇位置数据
Snake = [(0, 0)]

# 蛇方向，默认朝左
Dir = (-1, 0)

# 食物位置数据
Food = (randint(int(-WIDTH / 2), int(WIDTH / 2)),
        randint(int(-HEIGHT / 2), int(HEIGHT / 2)))


def move():
    """
    处理蛇移动
    """
    global Snake, Food, Dir

    head = Snake[0]  # 蛇头位置

    # 根据当前蛇头朝向，计算出蛇头下一个位置
    new_head = (head[0] + Dir[0], head[1] + Dir[1])

    # 判断蛇头是否撞墙或撞到自己
    if new_head[0] < -WIDTH / 2 or new_head[0] > WIDTH / 2 or \
        new_head[1] < -HEIGHT / 2 or new_head[1] > HEIGHT / 2 or \
            new_head in Snake:
        return False

    # 将新的蛇头位置加入蛇的数据中
    Snake.insert(0, new_head)

    # 判断是否能吃到食物
    if new_head == Food:
        # 重新生成食物位置
        Food = (randint(-WIDTH // 2, WIDTH // 2),
                randint(-HEIGHT // 2, HEIGHT // 2))

        # 避免食物生成到蛇的身体里
        while Food in Snake:
            Food = (randint(-WIDTH // 2, WIDTH // 2),
                    randint(-HEIGHT // 2, HEIGHT // 2))

    else:
        Snake.pop()  # 如果没吃到食物，就要将蛇尾移除，相当于把蛇尾移动到了蛇头

    return True


def draw_rect(x, y, size, name):
    """
    绘制矩形
    """
    # 将x y 放大BLOCK_SIZE
    x *= BLOCK_SIZE
    y *= BLOCK_SIZE

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()


def draw_wall():
    """
    绘制边界
    """
    for i in range(-WIDTH // 2 - 1, WIDTH // 2 + 2):
        draw_rect(i, -HEIGHT // 2 - 1, 8, 'black')
        draw_rect(i, HEIGHT // 2 + 1, 8, 'black')

    for i in range(-HEIGHT // 2 - 1, HEIGHT // 2 + 2):
        draw_rect(-WIDTH // 2 - 1, i, 8, 'black')
        draw_rect(WIDTH // 2 + 1, i, 8, 'black')


def draw_snake():
    global Snake
    for body in Snake:
        draw_rect(body[0], body[1], 8, 'black')


def draw_food():
    global Food
    draw_rect(Food[0], Food[1], 8, 'red')


def draw():
    """
    绘制实现
    """
    turtle.clear()  # 清空屏幕
    draw_wall()  # 绘制边界
    draw_snake()  # 绘制蛇
    draw_food()  # 绘制食物


def change_dir(x, y):
    """
    改变蛇的朝向
    """
    global Dir

    # 如果蛇已经在水平移动，则不能再改变左右朝向
    if Dir == (1, 0) or Dir == (-1, 0):
        x = 0

    # 同理
    if Dir == (0, 1) or Dir == (0, -1):
        y = 0

    if x != 0 or y != 0:
        Dir = (x, y)


def main_loop():
    """
    游戏主循环
    """

    # 1 移动蛇
    ret = move()

    # 2 绘制
    draw()

    # 3 如果移动成功，则继续执行
    if ret:
        turtle.ontimer(main_loop, 200)
    else:
        print('Game Over')


def main():
    # 初始化 turtle
    turtle.setup(420, 420, 370, 0)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.listen()

    # 添加响应键盘事件
    turtle.onkey(lambda: change_dir(1, 0), 'Right')
    turtle.onkey(lambda: change_dir(-1, 0), 'Left')
    turtle.onkey(lambda: change_dir(0, 1), 'Up')
    turtle.onkey(lambda: change_dir(0, -1), 'Down')

    main_loop()

    turtle.done()


if __name__ == '__main__':
    main()
