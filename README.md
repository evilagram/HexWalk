# HexWalk

This is a small turtle program that runs a function called HexWalk, which uses Turtle to draw a series of repeating polygons of varying size and color.

I started the project by figuring out how to draw a shape in turtle by calculating the angles of the shape relative to the desired number of sides (all angles in a shape always add up to 360, so I just need to tell the turtle to rotate by the number of sides / 360), then calculated the interior angle ((sides-2)*180) to rotate the turtle inwards, move it in a little bit, scaled down the distance, and then reversed the rotation, so the next iteration would produce a smaller version of the same shape inside the previous one. In the version of hexwalk.py on this repo, the interior angle was calculated incorrectly (calculated for a pentagon), and I mismatched the correction angle afterwards, causing it to rotate across iterations, producing interesting visual effects.

After I got successive iterations of shapes decreasing in size, I decided to try changing the pencolor, which takes 3 parameters, each being floats ranging from 0.0 to 1.0. I wanted it to smoothly shift between colors across each iteration, so I made 3 sets of 2 variables each, a starting and ending color for each RGB color component. I also wrote a function, called Lerp, which Linearly interpolates across a range. For each iteration I passed the lerp function into pencolor, using the starting RGB values, the end RGB values, and a calculation of how far through the iteration process the function currently was (the current iteration, i, versus the total, reps, converted to floats so as to avoid an integer answer). As I continued, I found starting and ending with just RGB values to be limiting, so I made another function to calculate color, lerpcolor, which linearly interpolates through the colors of the rainbow, using the lerp function internally. It passes these results out as an array of 3 float values, so the pencolor function can simply call the function 3 times, requesting a different color from the array each time. Within the lerpcolor function, I define 5 ranges across which each color transition occurs, returning the appropriate lerp for that color transition when the float value passed into the color lerp function is within that range.

I didn't quite calculate the scaling correctly, so across iterations each successive shape tends to get displaced a little. This produces an interesting visual effect, so I didn't fix it.

![step 1](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2015_47_01.png)
![step 2](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2015_53_13.png)
![step 3](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2016_28_37.png)
![step 4](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2016_34_43.png)
![step 5](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2016_36_26.png)
![step 6](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2016_37_27.png)
![step 7](https://github.com/evilagram/HexWalk/blob/master/Picture%202017-06-15%2016_38_20.png)
