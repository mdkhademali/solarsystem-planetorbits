import matplotlib.pyplot as plt
import numpy as np

# Planetary orbit sizes and positions (distances in AU)
planet_orbits = {
    'Mercury': 0.39,
    'Venus': 0.72,
    'Earth': 1.0,
    'Mars': 1.52,
    'Jupiter': 5.2,
    'Saturn': 9.58,
    'Uranus': 19.18,
    'Neptune': 30.07
}

# Angles for plotting the orbits
theta = np.linspace(0, 2 * np.pi, 100)

# Plot the orbits of the planets
plt.figure(figsize=(6,6))
for planet, distance in planet_orbits.items():
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    plt.plot(x, y, label=planet)

# Plot the Sun at the center
plt.scatter(0, 0, color='yellow', s=100, label='Sun')  # Sun

# Title and labels
plt.title('Solar System - Planet Orbits')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.legend()

# Ensure equal aspect ratio and show grid
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

# Display the plot
plt.show()