#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 19:28:11 2019

@author: UpcaseM

This script simulates a turtle eats fishes.
"""


import turtle
import random


class MyTurtle(turtle.Turtle):
    """
    The Myturtle class that create a turtle to eat fish.
    """

    def __init__(self,
                 life=100,
                 speed=2,
                 pond_size=(500, 500)):
        """
        Init a MyTurtle class with life, speed of the turtle and the pond size.

        Parameters
        ----------
        life : integer, optional
            Total ife of the turtle.
        speed : integer, optional
            The speed of the turtle. The default is 2.
        pond_size : list, optional
            The size of the pond. The default is [500, 500].

        Returns
        -------
        None.

        """
        super().__init__()
        self.shape('turtle')
        self.shapesize(2, 2, 2)
        self.color('#004490')
        self.speed(2)
        self.life = life
        self.pos_x = random.randint(-pond_size[0], pond_size[0])
        self.pos_y = random.randint(-pond_size[1], pond_size[1])
        self.x_range = [-pond_size[0], pond_size[0]]
        self.y_range = [-pond_size[1], pond_size[1]]
        self.penup()

    def move(self):
        """
        Turtle moves steps randomly.

        Returns
        -------
        self.pos_x, self.pos_y : integer
            Position of the turtle after move.

        """
        direction = random.randint(1, 4)
        steps = random.randint(100, 200)
        if direction == 1:
            self.setheading(0)
            if self.pos_x + steps > self.x_range[1]:
                steps *= -1
            self.pos_x += steps
        elif direction == 2:
            self.setheading(180)
            if self.pos_x - steps < self.x_range[0]:
                steps *= -1
            self.pos_x -= steps
        elif direction == 3:
            self.setheading(90)
            if self.pos_y + steps > self.y_range[1]:
                steps *= -1
            self.pos_y += steps
        else:
            self.setheading(270)
            if self.pos_y - steps < self.y_range[0]:
                steps *= -1
            self.pos_y -= steps
        self.life -= 1
        self.goto(self.pos_x, self.pos_y)
        return (self.pos_x, self.pos_y)

    def eat(self):
        """
        The turtle eat a fish.

        Returns
        -------
        None.

        """
        self.life += 40

    def get_pos(self):
        """
        Get the current position of the turtle.

        Returns
        -------
        self.pos_x, self.pos_y : integer
            Position of the turtle after move.
        """
        return (self.pos_x, self.pos_y)

    def get_life(self):
        """
        Get the current life of the turtle.
        If the life <= 0, game over.

        Returns
        -------
        self.life
            Number of life.
        """
        return self.life


class Fish(turtle.Turtle):
    lst_color = ['blue', 'red', 'orange', 'purple', 'yellow']
    lst_size = ['small', 'medium', 'large']

    def __init__(self,
                 pond_size=(500, 500)):
        """
        Init a fish object.

        Parameters
        ----------
        pond_size : list, optional
            Pond size. The default is [500, 500].

        Returns
        -------
        None.

        """
        super().__init__()
        self.color(Fish.lst_color[random.randint(0, 4)])
        self.size = Fish.lst_size[random.randint(0, 2)]
        self.pos_x = random.randint(-pond_size[0], pond_size[0])
        self.pos_y = random.randint(-pond_size[1], pond_size[1])
        self.x_range = [-pond_size[0], pond_size[0]]
        self.y_range = [-pond_size[1], pond_size[1]]
        # We use a circle to present a fish.
        self.speed(random.randint(3, 8))
        self.shape('circle')
        self.shapesize(random.randint(1, 2),
                       random.randint(1, 2),
                       random.randint(1, 10))
        self.penup()

    def move(self):
        """
        Fish moves steps randomly.

        Returns
        -------
        self.pos_x, self.pos_y : integer
            Position of the fish after move.

        """
        # Fish changes its direction before every movement
        direction = random.randint(1, 4)
        steps = random.randint(10, 50)
        if direction == 1:
            if self.pos_x + steps > self.x_range[1]:
                self.pos_x -= steps
            else:
                self.pos_x += steps
        elif direction == 2:
            if self.pos_x - steps < self.x_range[0]:
                self.pos_x += steps
            else:
                self.pos_x -= steps
        elif direction == 3:
            if self.pos_y + steps > self.y_range[1]:
                self.pos_y -= steps
            else:
                self.pos_y += steps
        else:
            if self.pos_y - steps < self.y_range[0]:
                self.pos_y += steps
            else:
                self.pos_y -= steps
        self.goto(self.pos_x, self.pos_y)
        return (self.pos_x, self.pos_y)

    def get_pos(self):
        """
        Get the current position of the fish.

        Returns
        -------
        self.pos_x, self.pos_y : integer
            Position of the fish after move.
        """
        return (self.pos_x, self.pos_y)
        return (self.pos_x, self.pos_y)

    def get_att(self):
        """
        Get the size of the fish.

        Returns
        -------
        self.size : string
            The size of the fish
        """
        return self.size


class pond:
    """
    Pond class that generates a pond and start the simulation.
    """

    def __init__(self,
                 my_turtle,
                 lst_fish,
                 pond_size=(500, 500),
                 num_fish=10):
        """
        Init the pond with the size of the pond and
        number of fishes in the pond.

        Parameters
        ----------
        my_turtle : object
            A MyTurtle object.
        lst_fish : list
            A list contains quantity num_fish fish objects.
        pond_size : list
            A list with two elements. The first one is the width
            and the second is the height.
        num_fish : interger
            Number of fishes in the pond.

        Returns
        -------
        None.

        """
        self.pond_size = pond_size
        self.num_fish = num_fish
        self.turtle = my_turtle
        self.lst_fish = lst_fish

    def run(self):
        """
        Function to start the simulation.

        Returns
        -------
        None.

        """
        # Init the pond
        # Create a window for the game
        wd = turtle.Screen()
        wd.title('Turle Game')
        wd.bgcolor('#8dcbe3')
        wd.setup(width=1200, height=1200)
        # Init the position of the turtle.
        self.turtle.goto(self.turtle.get_pos()[0],
                         self.turtle.get_pos()[1])
        while True:
            # Game ends when turtle dies or no fish in the pond
            if len(self.lst_fish) == 0 or self.turtle.get_life() == 0:
                print('Game Over')
                if self.turtle.get_life() == 0:
                    print('The Turtle is dead!')
                else:
                    print(f'''No fish left in the pond.
                              The Turtle has {self.turtle.get_life()} life'
                           ''')
                break

            # The turtle will eat the fish if there are any fish on its spot.
            for fish in self.lst_fish:
                if fish.distance(t) < 40:
                    self.turtle.eat()
                    print(f'''The Turtle is eating a {fish.get_att()[0]} size fish!''')
                    print(f'There are {len(self.lst_fish)} fishes in the pond')
                    print(f'The turtle has {self.turtle.get_life()} life left')
                    fish.ht()
                    self.lst_fish.remove(fish)
                    print('=========================================')
                fish.move()
            self.turtle.move()
        wd.mainloop()


if __name__ == '__main__':
    # Pond size
    # pond_size = [500, 500]
    # Generate a turtle
    # t_life = 100
    t = MyTurtle()
    # Genenerate fishe list
    lst_fish = []
    num_fishes = 10
    for i in range(num_fishes):
        lst_fish.append(Fish())
    print(t.get_pos())
    # Init a pond
    p = pond(t, lst_fish)
    p.run()
