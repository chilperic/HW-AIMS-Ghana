<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/python3
=======
#!/usr/local/bin/python3
=======
#!/usr/bin/env python3
>>>>>>> origin/master

>>>>>>> origin/master
import numpy as np
import midpoint

def intf(x):
<<<<<<< HEAD
    return x-x**2

rangex = np.linspace(0,1,100)

print(midpoint.integrate(intf, rangex))
=======
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}"

print(out.format(
    "midpoint",
    rangex[0], rangex[-1],
    midpoint.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
    quad(intf, rangex[0], rangex[-1])
))
>>>>>>> origin/master
