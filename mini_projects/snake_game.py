#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:43:27 2020

@author: UpcaseM

A snake game using turtle.
"""

import turtle
import random
import time


class Snake:
    lst_direction = ('up', 'down', 'right', 'left')

    def __init__(self,
                 pool_size=(400, 400)):
        """
        Init a Snake class.

        Parameters
        ----------
        pool_size : tuple, optional
            Size of the pool. The default is (400, 400).

        Returns
        -------
        None.

        """
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape('square')
        self.head.color('black')
        self.head.penup()
        self.direction = 'stop'
        self.body = []
        self.boundary = pool_size

    def move(self):
        """
        Move the snake.
        """
        y = self.head.ycor()
        x = self.head.xcor()
        if self.direction == 'up':
            y += 15
        elif self.direction == 'down':
            y -= 15
        elif self.direction == 'right':
            x += 15
        elif self.direction == 'left':
            x -= 15
        lst_pos = [(self.head.xcor(), self.head.ycor())]
        for b in self.body:
            lst_pos.append((b.xcor(), b.ycor()))
        # If the game window is closed, then pass.
        try:
            self.head.goto(x, y)
            for i, b in enumerate(self.body):
                b.goto(lst_pos[i][0],
                       lst_pos[i][1])
        except:
            pass

    def go_up(self):
        """
        Change the direction of the snake to up.
        """
        if self.direction != 'down':
            self.direction = 'up'

    def go_down(self):
        """
        Change the direction of the snake to down.
        """
        if self.direction != 'up':
            self.direction = 'down'

    def go_right(self):
        """
        Change the direction of the snake to right.
        """
        if self.direction != 'left':
            self.direction = 'right'

    def go_left(self):
        """
        Change the direction of the snake to left.
        """
        if self.direction != 'right':
            self.direction = 'left'

    def add_body(self):
        """
        Add one body to the snake.
        """
        b = turtle.Turtle()
        b.shape('square')
        b.color('grey')
        b.speed(0)
        b.penup()
        b.goto(self.head.xcor(),
               self.head.ycor())
        self.body.append(b)


class Pool:

    def __init__(self,
                 snake,
                 pool_size=(400, 400)):
        """
        Init the Pool class.

        Parameters
        ----------
        snake : Snake isntance
            An Snake instance.
        pool_size : tuple, optional
            The pool size. The default is (400, 400).

        Returns
        -------
        None.

        """
        self.pool_size = pool_size
        self.snake = snake
        self.delay = 0.1
        self.high_score = 0
        self.score = 0
        self.pen = self.init_score()
        self.food = self.init_food()

    def run(self):
        """
        Function to run the snake game.

        Returns
        -------
        None.

        """
        # Init the window
        wd = turtle.Screen()
        wd.tracer(0)
        wd.title('Snake Game by UpcaseM')
        wd.bgcolor('#8dcbe3')
        wd.setup(width=self.pool_size[0]+50,
                 height=self.pool_size[1]+50)
        wd.listen()
        wd.onkey(self.snake.go_up, 'Up')
        wd.onkey(self.snake.go_down, 'Down')
        wd.onkey(self.snake.go_right, 'Right')
        wd.onkey(self.snake.go_left, 'Left')

        # Main game loop
        while True:
            wd.update()
            self.snake.move()
            # Check border collisions
            if self.snake.head.xcor() > self.pool_size[0]/2+10 \
                or self.snake.head.xcor() < -self.pool_size[0]/2-10 \
                or self.snake.head.ycor() > self.pool_size[1]/2+10 \
                or self.snake.head.ycor() < -self.pool_size[1]/2-10:
                time.sleep(1)
                self.reset_game()
            # Check body collisions
            for b in self.snake.body:
                if b.distance(self.snake.head) < 15:
                    time.sleep(1)
                    self.reset_game()
            # If eat, move food
            if self.food.distance(self.snake.head) < 20:
                self.snake.add_body()
                # Reduce the delay when you eat a food.
                self.delay -= 0.005
                self.food.goto(random.randint(-self.pool_size[0]/2,
                                              self.pool_size[0]/2),
                               random.randint(-self.pool_size[1]/2,
                                              self.pool_size[1]/2))
                # Increase the score
                self.add_score()
            time.sleep(self.delay)
        wd.mainloop()

    def init_score(self):
        """
        Init a pen instance to record the score.
        """
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape('square')
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, self.pool_size[0]/2 - 10)
        pen.write(f'Score: 0    High Score: {self.high_score}',
                  align='center',
                  font=('Courier', 24, 'normal'))
        return pen

    def add_score(self):
        """
        Add 10 score when the snake eat a food.
        """
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.pen.clear()
        self.pen.write(f'Score: {self.score}    High Score: {self.high_score}',
                       align='center',
                       font=('Courier', 24, 'normal'))

    def init_food(self):
        """
        Init a food instance.
        """
        food = turtle.Turtle()
        food.speed(0)
        food.shape('circle')
        food.color('red')
        food.penup()
        food.shapesize(0.7, 0.7)
        food.goto(random.randint(-self.pool_size[0]/2, self.pool_size[0]/2),
                  random.randint(-self.pool_size[1]/2, self.pool_size[1]/2))
        return food

    def reset_game(self):
        """
        Reset the game.
        """
        # Reset the snake
        for b in self.snake.body:
            b.hideturtle()
        self.snake.body.clear()
        self.snake.head.goto(0, 0)
        self.snake.direction = 'stop'
        # Clear the score
        self.score = 0
        self.pen.clear()
        self.pen.write(f'Score: {self.score}    High Score: {self.high_score}',
                       align='center',
                       font=('Courier', 24, 'normal'))
        # Reset the delay time
        self.delay = 0.1


if __name__ == '__main__':
    s = Snake()
    p = Pool(s)
    p.run()
