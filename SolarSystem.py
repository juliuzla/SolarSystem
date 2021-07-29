from vpython import*

e_graph = gcurve(color=color.blue)

def gforce(p1, p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1  # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos - p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec / r_mag
    # Calculate force magnitude.
    force_mag = G * p1.mass * p2.mass / r_mag ** 2
    # Calculate force vector.
    force_vec = -force_mag * r_hat

    return force_vec


star = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow,
              mass=1000, momentum=vector(0, 0, 0), make_trail=True)

planet1 = sphere(pos=vector(1, 0, 0), radius=0.05, color=color.blue,
                 mass=1, momentum=vector(0, 30, 0), make_trail=True)

planet2 = sphere(pos=vector(0, 3, 0), radius=0.075, color=color.red,
                 mass=2, momentum=vector(-35, 0, 0), make_trail=True)

planet3 = sphere(pos=vector(0, -4, 0), radius=0.1, color=color.green,
                 mass=10, momentum=vector(160, 0, 0), make_trail=True)

dt = 0.0001
t = 0
while (True):
    rate(1000)

    # Calculate forces.
    star.force = gforce(star, planet1) + gforce(star, planet2) + gforce(star, planet3)
    planet1.force = gforce(planet1, star) + gforce(planet1, planet2) + gforce(planet1, planet3)
    planet2.force = gforce(planet2, star) + gforce(planet2, planet1) + gforce(planet2, planet3)
    planet3.force = gforce(planet3, star) + gforce(planet3, planet1) + gforce(planet3, planet2)

    # Update momenta.
    star.momentum = star.momentum + star.force * dt
    planet1.momentum = planet1.momentum + planet1.force * dt
    planet2.momentum = planet2.momentum + planet2.force * dt
    planet3.momentum = planet3.momentum + planet3.force * dt

    # Update positions.
    star.pos = star.pos + star.momentum / star.mass * dt
    planet1.pos = planet1.pos + planet1.momentum / planet1.mass * dt
    planet2.pos = planet2.pos + planet2.momentum / planet2.mass * dt
    planet3.pos = planet3.pos + planet3.momentum / planet3.mass * dt

    t = t + dt


