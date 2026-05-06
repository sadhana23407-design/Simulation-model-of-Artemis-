import numpy as np
import matplotlib.pyplot as plt
G = 6.67e-11
m1 = 5.97e24   
m2 = 1000      
p1 = np.array([0.0, 0.0])      

p2 = np.array([9e6, 0.0])      
v2 = np.array([0.0, 8700])     

t = 1                         
pos = []
for i in range(6000):

    r = p2 - p1
    d = np.linalg.norm(r)
    F = (G * m1 * m2) / (d**2)
    dir = r / d
    acc = (-F * dir) / m2
    v2 += acc * t
    p2 += v2 * t

    pos.append(p2.copy())

pos = np.array(pos)
plt.figure(figsize=(6,6))
plt.plot(pos[:,0], pos[:,1])
plt.scatter(0, 0, color='red')

plt.axis("equal")
plt.legend()
plt.title("Artemis II Orbital Simulation ")
plt.xlabel("X Position ")
plt.ylabel("Y Position ")
plt.show()
dis = np.linalg.norm(pos, axis=1)

periapsis = np.min(dis)
apoapsis = np.max(dis)

print("Periapsis :", periapsis)
print("Apoapsis :", apoapsis)
start_d = dis[0]
period= None

for i in range(1, len(dis)):
    if abs(dis[i] - start_d) < 1e5:
        period = i
        break

if period:
    orbital_period = period * t
    print("Orbital Period-approx:", orbital_period, "seconds")
else:
    print("Orbital period not clearly detected")