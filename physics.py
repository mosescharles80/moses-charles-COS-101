def calculate_force(mass, acceleration):
    """Calculates Force (Newton's Second Law): F = m * a"""
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """Calculates Kinetic Energy: KE = 0.5 * m * v^2"""
    return 0.5 * mass * (velocity ** 2)

def calculate_potential_energy(mass, height, gravity=9.8):
    """Calculates Gravitational Potential Energy: PE = m * g * h"""
    return mass * gravity * height

def calculate_ohms_law_voltage(current, resistance):
    """Calculates Voltage using Ohm's Law: V = I * R"""
    return current * resistance

def calculate_speed(distance, time):
    """Calculates Speed/Velocity: v = d / t"""
    if time == 0:
        return "Time cannot be zero"
    return distance / time