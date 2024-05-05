def add(num1, num2):
  """Adds two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers (handles zero division)."""
  if num2 == 0:
    return "Error: Cannot divide by zero"
  return num1 / num2
