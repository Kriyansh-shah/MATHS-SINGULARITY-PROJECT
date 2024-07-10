import numpy as np
import matplotlib.pyplot as plt

def plot_exponential_growth_and_phase(func, xmin, xmax, ymin, ymax, num_points=1000):
    x = np.linspace(xmin, xmax, num_points)
    y = np.linspace(ymin, ymax, num_points)
    X, Y = np.meshgrid(x, y)
    Z = func(X + 1j * Y)
    
    magnitude = np.abs(Z)
    phase = np.angle(Z)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.contourf(X, Y, np.log(magnitude), cmap='viridis')
    plt.colorbar(label='Log Magnitude')
    plt.title('Exponential Growth of Magnitude')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    
    plt.subplot(1, 2, 2)
    plt.contourf(X, Y, phase, cmap='hsv')
    plt.colorbar(label='Phase Angle')
    plt.title('Phase Angle')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    
    plt.show()

def complex_differentiation(func, z, h=1e-5):
    try:
        return (func(z + h) - func(z)) / h
    except ZeroDivisionError:
        return float('nan') 
    except:
        return None  

def is_singular(func, z):
    try:
        func(z)
        return False
    except ZeroDivisionError:
        return True
    except:
        return None


def is_analytic(func, z):
    try:
        
        func_value = func(z)
    except:
        return False  
    
   
    if is_singular(func, z):
        return False 
    
    try:
        derivative = complex_differentiation(func, z)
        if derivative is None:
            return False  
    except:
        return False 
    
    return True  



def user_defined_function(z):
    return np.sin(z) / z


user_function = input("Enter your complex function (e.g., 'np.sin(z)/z'): ")
func = eval("lambda z: " + user_function)


plot_exponential_growth_and_phase(func, -5, 5, -5, 5)


point = complex(input("Enter a complex number to compute its derivative at (e.g., 1+2j): "))
derivative = complex_differentiation(func, point)
if derivative is None:
    print("Function does not exist at point {}".format(point))
elif np.isnan(derivative):
    print("Function has a singularity at point {}".format(point))
else:
    print("Derivative at {}: {}".format(point, derivative))


print("Is {} a singularity of the function? {}".format(point, is_singular(func, point)))


print("Is the function analytic at {}? {}".format(point, is_analytic(func, point)))