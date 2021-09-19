# Pile-of-Sand

## The project
I've watched [Science étonnante](https://www.youtube.com/c/ScienceEtonnante)'s last video yesterday. 
This [great video](https://www.youtube.com/watch?v=MrsjMiL9W9o) is about the modelisation of daily fluctations in the stock market. In the video he uses a python modelisation to explain the "Self-organised Criticality" principle. I found interresting to code it by myself with python.
So here is a small modelisation of a pile of sand on which some grains of sand would be dropped regularly. When you launch the simulation, you can see some avalanches sometimes, result of the dropped grains and of the "Self-organised Criticality" phenomenom.

##
The "Self-organised Criticality" principle (applied to a sand pile) is the way the grains make avalanches when they're too unstable but that always stay near an unstable balance when the avalanche stops. The goal with my program is to simulate the evolution of the organisation of the grains when some new grains are dropped on the pile. I wanted to see these avalanches created by my own program and not just in somebody's video.

This simulation is lead by 2 simple rules, that remembers those of Conway's life game  :
- **1** : A new grain of sand is dropped on the pile at each round
- **2** : If there're more than 4 grains on the same cell, they're pushed to the 4 cells around (top, bottom, right, left) *(Note : I used a variable in my program to be able to change this "critical threshold")

Here is a run of my simulation :

![](https://github.com/Studioaxs/Pile-of-Sand/blob/main/sand-pile-reshaped.gif)



This is how my program works : 
- A ndArray is created with the wanted shape. It's filled with zeros
- A *for* loop is used to create the rounds. A randome cell is incremented.
- Then all cells are scanned and if the number of grains on it is over the critical threshold, I put a 0 on the cell, and increment the four cells around.
- A *for* loop is used to create all the steps of the animation
- The function matplotlib.animation.ArtistAnimation is used to animate the steps

## Some ways of improvement : 
- I could add a color scale;
- When I run the script, a second empty matplotlib window opens. I don't know why but I think it's possible to solve it; 


## Some informations
- Written with python 3.6;
- Uses numpy arrays to simulate the grid, and matplotlib.animation to display and animate the simulation;

### Here are some documentation parts and examples that helped me throught this mini project :
- The video : https://www.youtube.com/watch?v=MrsjMiL9W9o
- A post on stackoverflow that helped me to understand how to animate a plot with matplotlib.animation : https://stackoverflow.com/questions/62411273/how-to-use-matplotlib-funcanimation-to-animate-a-heatmap
- A really useful example with matplotlib.animation : https://matplotlib.org/2.1.2/gallery/animation/basic_example.html
- The documentation of matplotlib.animation : https://matplotlib.org/stable/api/animation_api.html
