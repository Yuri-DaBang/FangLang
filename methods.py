from time import sleep
import json
import interpreter
import requests
import os
import random , math
from colors import Colors

class console:
    class output:
        def success(script, args):
            message = args[0]
    
            if type(message) is str:
                message = interpreter.resolveString(script, message)
            else:
                message = str(message)

            Colors.general.success(message)

        def error(script, args):
            message = args[0]
    
            if type(message) is str:
                message = interpreter.resolveString(script, message)
            else:
                message = str(message)

            Colors.general.big_error(message)
            
        def warning(script, args):
            message = args[0]
    
            if type(message) is str:
                message = interpreter.resolveString(script, message)
            else:
                message = str(message)

            Colors.general.warning(message)
            
        def output(script, args):
            message = args[0]
    
            if type(message) is str:
                message = interpreter.resolveString(script, message)
            else:
                message = str(message)

            Colors.general.output(message)
            

    def println(script, args):
        message = args[0]
    
        message = str(message)

        print(message)
import matplotlib.pyplot as plt
import numpy as np

class GraphicsLibrary:
    @staticmethod
    def plot(x, y, xlabel=None, ylabel=None, title=None):
        plt.plot(x, y)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if title:
            plt.title(title)
        plt.grid(True)
        plt.show()

    @staticmethod
    def scatter(x, y, xlabel=None, ylabel=None, title=None):
        plt.scatter(x, y)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if title:
            plt.title(title)
        plt.grid(True)
        plt.show()

    @staticmethod
    def histogram(data, bins='auto', xlabel=None, ylabel=None, title=None):
        plt.hist(data, bins=bins)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if title:
            plt.title(title)
        plt.grid(True)
        plt.show()

    @staticmethod
    def bar(x, y, xlabel=None, ylabel=None, title=None):
        plt.bar(x, y)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if title:
            plt.title(title)
        plt.grid(True)
        plt.show()

    @staticmethod
    def pie(sizes, labels=None, explode=None, autopct='%1.1f%%', startangle=90):
        plt.pie(sizes, labels=labels, explode=explode, autopct=autopct, startangle=startangle)
        plt.axis('equal')
        plt.show()

    @staticmethod
    def plot_3d(x, y, z, xlabel=None, ylabel=None, zlabel=None, title=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        if zlabel:
            ax.set_zlabel(zlabel)
        if title:
            plt.title(title)
        plt.show()

    @staticmethod
    def imshow(image, cmap=None, title=None):
        plt.imshow(image, cmap=cmap)
        if title:
            plt.title(title)
        plt.axis('off')
        plt.show()

    @staticmethod
    def quiver(x, y, u, v, scale=1, width=0.005, color='blue'):
        plt.quiver(x, y, u, v, scale=scale, width=width, color=color)
        plt.show()

    @staticmethod
    def contour(x, y, z, levels=None, cmap=None):
        plt.contour(x, y, z, levels=levels, cmap=cmap)
        plt.colorbar()
        plt.show()

    @staticmethod
    def boxplot(data, labels=None):
        plt.boxplot(data, labels=labels)
        plt.show()

    @staticmethod
    def violinplot(data, labels=None):
        plt.violinplot(data, labels=labels)
        plt.show()

    @staticmethod
    def errorbar(x, y, xerr=None, yerr=None, fmt='o', ecolor='red', capsize=5):
        plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=fmt, ecolor=ecolor, capsize=capsize)
        plt.show()

    @staticmethod
    def stem(x, y, linefmt='-', markerfmt='o', basefmt='r-'):
        plt.stem(x, y, linefmt=linefmt, markerfmt=markerfmt, basefmt=basefmt)
        plt.show()

    @staticmethod
    def hexbin(x, y, gridsize=30, cmap='Blues'):
        plt.hexbin(x, y, gridsize=gridsize, cmap=cmap)
        plt.colorbar()
        plt.show()

    @staticmethod
    def polar(theta, r, title=None):
        plt.polar(theta, r)
        if title:
            plt.title(title)
        plt.show()

    @staticmethod
    def streamplot(x, y, u, v, density=1, color='blue'):
        plt.streamplot(x, y, u, v, density=density, color=color)
        plt.show()

    @staticmethod
    def plot_date(dates, y, fmt='o', color='blue'):
        plt.plot_date(dates, y, fmt=fmt, color=color)
        plt.show()

    @staticmethod
    def eventplot(lines, colors=None, lineoffsets=None, linelengths=None, orientation='horizontal'):
        plt.eventplot(lines, colors=colors, lineoffsets=lineoffsets, linelengths=linelengths, orientation=orientation)
        plt.show()

    @staticmethod
    def step(x, y, where='pre'):
        plt.step(x, y, where=where)
        plt.show()

    @staticmethod
    def fill(x, y, color='blue', alpha=0.5):
        plt.fill(x, y, color=color, alpha=alpha)
        plt.show()

    @staticmethod
    def stackplot(x, data, labels=None):
        plt.stackplot(x, data, labels=labels)
        plt.legend()
        plt.show()

    @staticmethod
    def imshow_extent(image, extent, cmap=None):
        plt.imshow(image, extent=extent, cmap=cmap)
        plt.show()

class MathPhysics:
    class Calculations:
        # Basic Arithmetic
        @staticmethod
        def add(script, args):
            return args[0] + args[1]

        @staticmethod
        def subtract(script, args):
            return args[0] - args[1]

        @staticmethod
        def multiply(script, args):
            return args[0] * args[1]

        @staticmethod
        def divide(script, args):
            if args[1] == 0:
                raise ValueError("Cannot divide by zero")
            return args[0] / args[1]

        @staticmethod
        def power(script, args):
            return math.pow(args[0], args[1])

        @staticmethod
        def sqrt(script, args):
            return math.sqrt(args[0])

        @staticmethod
        def factorial(script, args):
            return math.factorial(args[0])

        # Trigonometry
        @staticmethod
        def sine(script, args):
            return math.sin(args[0])

        @staticmethod
        def cosine(script, args):
            return math.cos(args[0])

        @staticmethod
        def tangent(script, args):
            return math.tan(args[0])

        @staticmethod
        def arcsine(script, args):
            return math.asin(args[0])

        @staticmethod
        def arccosine(script, args):
            return math.acos(args[0])

        @staticmethod
        def arctangent(script, args):
            return math.atan(args[0])

        @staticmethod
        def sinh(script, args):
            return math.sinh(args[0])

        @staticmethod
        def cosh(script, args):
            return math.cosh(args[0])

        @staticmethod
        def tanh(script, args):
            return math.tanh(args[0])

        # Logarithms
        @staticmethod
        def log(script, args):
            return math.log(args[0], args[1] if len(args) > 1 else math.e)

        @staticmethod
        def log10(script, args):
            return math.log10(args[0])

        @staticmethod
        def log2(script, args):
            return math.log2(args[0])

        @staticmethod
        def exp(script, args):
            return math.exp(args[0])

        # Geometry
        @staticmethod
        def distance(script, args):
            x1, y1, x2, y2 = args
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        @staticmethod
        def circle_area(script, args):
            radius = args[0]
            return math.pi * radius**2

        @staticmethod
        def rectangle_area(script, args):
            length, width = args
            return length * width

        @staticmethod
        def triangle_area(script, args):
            base, height = args
            return 0.5 * base * height

        @staticmethod
        def sphere_volume(script, args):
            radius = args[0]
            return (4/3) * math.pi * radius**3

        @staticmethod
        def cylinder_volume(script, args):
            radius, height = args
            return math.pi * radius**2 * height

        @staticmethod
        def cone_volume(script, args):
            radius, height = args
            return (1/3) * math.pi * radius**2 * height

        # Statistics
        @staticmethod
        def mean(script, args):
            return sum(args) / len(args)

        @staticmethod
        def median(script, args):
            sorted_args = sorted(args)
            n = len(args)
            mid = n // 2
            if n % 2 == 0:
                return (sorted_args[mid - 1] + sorted_args[mid]) / 2
            else:
                return sorted_args[mid]

        @staticmethod
        def mode(script, args):
            counts = {num: args.count(num) for num in args}
            return max(counts, key=counts.get)

        @staticmethod
        def variance(script, args):
            mean_value = MathPhysics.Calculations.mean(script, args)
            return sum((x - mean_value) ** 2 for x in args) / len(args)

        @staticmethod
        def standard_deviation(script, args):
            return math.sqrt(MathPhysics.Calculations.variance(script, args))

        @staticmethod
        def correlation(script, args):
            x, y = args
            n = len(x)
            mean_x = MathPhysics.Calculations.mean(script, x)
            mean_y = MathPhysics.Calculations.mean(script, y)
            covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
            std_dev_x = MathPhysics.Calculations.standard_deviation(script, x)
            std_dev_y = MathPhysics.Calculations.standard_deviation(script, y)
            return covariance / (std_dev_x * std_dev_y)

        # Calculus
        @staticmethod
        def derivative(script, args):
            func, x, dx = args
            return derivative(func, x, dx=dx)

        @staticmethod
        def integral(script, args):
            func, a, b = args
            result, _ = quad(func, a, b)
            return result

        # Physics
        @staticmethod
        def velocity(script, args):
            distance, time = args
            if time == 0:
                raise ValueError("Time cannot be zero")
            return distance / time

        @staticmethod
        def acceleration(script, args):
            velocity, time = args
            if time == 0:
                raise ValueError("Time cannot be zero")
            return velocity / time

        @staticmethod
        def force(script, args):
            mass, acceleration = args
            return mass * acceleration

        @staticmethod
        def kinetic_energy(script, args):
            mass, velocity = args
            return 0.5 * mass * velocity**2

        @staticmethod
        def potential_energy(script, args):
            mass, height, gravity = args
            return mass * height * gravity

        @staticmethod
        def momentum(script, args):
            mass, velocity = args
            return mass * velocity

        @staticmethod
        def work(script, args):
            force, distance = args
            return force * distance

        @staticmethod
        def power_physics(script, args):
            work, time = args
            if time == 0:
                raise ValueError("Time cannot be zero")
            return work / time

        @staticmethod
        def pressure(script, args):
            force, area = args
            if area == 0:
                raise ValueError("Area cannot be zero")
            return force / area

        @staticmethod
        def density(script, args):
            mass, volume = args
            if volume == 0:
                raise ValueError("Volume cannot be zero")
            return mass / volume

        @staticmethod
        def circular_motion(script, args):
            radius, angular_velocity = args
            return radius * angular_velocity**2

        @staticmethod
        def gravitational_force(script, args):
            mass1, mass2, distance = args
            G = 6.67430e-11
            if distance == 0:
                raise ValueError("Distance cannot be zero")
            return G * (mass1 * mass2) / distance**2

        @staticmethod
        def ohms_law(script, args):
            voltage, resistance = args
            if resistance == 0:
                raise ValueError("Resistance cannot be zero")
            return voltage / resistance

        @staticmethod
        def coulombs_law(script, args):
            charge1, charge2, distance = args
            k = 8.9875517873681764e9
            if distance == 0:
                raise ValueError("Distance cannot be zero")
            return k * (charge1 * charge2) / distance**2

        @staticmethod
        def buoyant_force(script, args):
            fluid_density, volume, gravity = args
            return fluid_density * volume * gravity

        @staticmethod
        def refraction(script, args):
            n1, n2, angle1 = args
            angle1_rad = math.radians(angle1)
            sin_angle2 = (n1 / n2) * math.sin(angle1_rad)
            if abs(sin_angle2) > 1:
                raise ValueError("Total internal reflection occurs")
            angle2_rad = math.asin(sin_angle2)
            return math.degrees(angle2_rad)

        @staticmethod
        def doppler_effect(script, args):
            source_freq, velocity_source, velocity_observer, sound_speed = args
            return ((sound_speed + velocity_observer) / (sound_speed - velocity_source)) * source_freq

        @staticmethod
        def planck_energy(script, args):
            frequency = args[0]
            h = 6.62607015e-34
            return h * frequency

        @staticmethod
        def einstein_mass_energy(script, args):
            mass = args[0]
            c = 299792458
            return mass * c**2

        # Built-in math functions
        @staticmethod
        def fabs(script, args):
            return math.fabs(args[0])

        @staticmethod
        def ceil(script, args):
            return math.ceil(args[0])

        @staticmethod
        def floor(script, args):
            return math.floor(args[0])

        @staticmethod
        def fmod(script, args):
            return math.fmod(args[0], args[1])

        @staticmethod
        def gcd(script, args):
            return math.gcd(args[0], args[1])

        @staticmethod
        def isfinite(script, args):
            return math.isfinite(args[0])

        @staticmethod
        def isinf(script, args):
            return math.isinf(args[0])

        @staticmethod
        def isnan(script, args):
            return math.isnan(args[0])

        @staticmethod
        def degrees(script, args):
            return math.degrees(args[0])

        @staticmethod
        def radians(script, args):
            return math.radians(args[0])

        @staticmethod
        def copysign(script, args):
            return math.copysign(args[0], args[1])

        @staticmethod
        def comb(script, args):
            return math.comb(args[0], args[1])

        @staticmethod
        def perm(script, args):
            return math.perm(args[0], args[1])

        @staticmethod
        def ldexp(script, args):
            return math.ldexp(args[0], args[1])

        @staticmethod
        def frexp(script, args):
            return math.frexp(args[0])

        @staticmethod
        def modf(script, args):
            return math.modf(args[0])

        @staticmethod
        def trunc(script, args):
            return math.trunc(args[0])

    @staticmethod
    def println(script, args):
        print(args[0])

class panic:
    def error(script, args):
        message = args[0]
    
        if type(message) is str:
            message = interpreter.resolveString(script, message)
        else:
            message = str(message)

        Colors.general.error(message)
        exit()
        
    def warning(script, args):
        message = args[0]
    
        if type(message) is str:
            message = interpreter.resolveString(script, message)
        else:
            message = str(message)

        Colors.general.warning(message)
        exit()
        
#####
#####
#####

def bark(script, args):
    message = args[0]
    
    if type(message) is str:
        message = interpreter.resolveString(script, message)
    else:
        message = str(message)

    print(message)

def paw(script, args):
    args[0].value += args[1]

def sweep(script, args):
    sleep(args[0])

def bite(script, args):
    del script.variables[args[0].name]

def pwompt(script, args):
    return input(args[0])

def fetch(script, args):
    if len(args) > 1:
        return requests.get(args[0], headers={'User-Agent': args[1]}).text
    else:
        return requests.get(args[0]).text

def fetchjson(script, args):
    if len(args) > 1:
        return requests.get(args[0], headers={'User-Agent': args[1]}).json()
    else:
        return requests.get(args[0]).json()

def stash(script, args):
    url = args[0]
    path = args[1]
    user_agent = None

    if len(args) > 2:
        user_agent = args[2]

    dir = path[:path.rfind('/')]
    if not os.path.exists(dir):
        os.makedirs(dir)

    # download file from url at path
    with open(path, 'wb') as f:
        if user_agent:
            f.write(requests.get(url, headers={'User-Agent': user_agent}).content)
        else:
            f.write(requests.get(url).content)

def wandom(script, args):
    if len(args) == 1:
        return random.randint(1, args[0])
    else:
        return random.randint(args[0], args[1])

def removeQuotes(string):
    if string.startswith('"') and string.endswith('"'):
        return string[1:-1]
    return string

########################
### SELF ADDED FUNCS ###
### MORE FUNCS ADDED ###
########################

def type(script, args):
    var_name = args[0]
    if var_name in script.variables:
        var_type = type(script.variables[var_name].value).__name__
        return var_type
    else:
        raise Exception(f"Variable {var_name} not found in script")