
import math

def boltbending(bolt_diameter, bolt_yield_strength, bending_moment):
  """Calculates the bending stress in a bolt.

  Args:
    bolt_diameter: The diameter of the bolt in inches.
    bolt_yield_strength: The yield strength of the bolt in psi.
    bending_moment: The bending moment in inch-pounds.

  Returns:
    The bending stress in psi.
  """

  # Calculate the cross-sectional area of the bolt.
  bolt_area = math.pi * (bolt_diameter / 2) ** 2

  # Calculate the bending stress.
  bending_stress = bending_moment / bolt_area


  return bending_stress

def Sub2Nums(x, y):
    return x - y

def Mult2Nums(x, y):
    return x * y

def Div2Nums(x, y):
    result = x / y
    result = round(result, 2)
    return result

def KineticEnergy(m, v):
    result = .5 * m * pow(v, 2)
    return result