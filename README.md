# Simulation-model-of-Artemis-
This project simulates the orbital trajectory of a spacecraft inspired by Artemis II using Newtonian gravity.
Assuming the Earth's position is fixed at the origin because of its large mass compared to the object, and thus, movement is neglected. The vector pointing in the direction from Earth to the object is calculated, and the distance between Earth and the object is measured using [d = np.linalg.norm(r)]
Using gravitational equations, the gravity is calculated and so is acceleration, and the velocity of the object is updated, making it move and result in a curved orbit.
Python, Numpy, and Matplotlib were used to handle the mathematical calculations and plot the orbital motion of the Earth and the object.
Gravitational equation: F=Gm1m2/r^2
Periapsis, apoapsis, and orbital period were calculated.



References:
I referred to online resources and tools to understand how to implement mathematical calculations and use numpy and libraries, and then modified the code based on my understanding.
