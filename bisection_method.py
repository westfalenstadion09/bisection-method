# BISECTION METHOD

# Define the function
def f(x):
    return x**3 - x - 2   # Example equation

# Define the Bisection Method
def bisection(a, b, tolerance, max_iterations=50):
    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs!")
        return None

    print(f"{'Step':<5}{'a':<12}{'b':<12}{'p':<12}{'f(p)':<12}")
    print("-" * 50)

    for i in range(1, max_iterations + 1):
        p = (a + b) / 2
        fp = f(p)
        print(f"{i:<5}{a:<12.6f}{b:<12.6f}{p:<12.6f}{fp:<12.6f}")

        if abs(fp) < tolerance:
            print("\nRoot found at:", round(p, 6))
            print("Stopped after", i, "iterations.")
            return p

        if f(a) * fp < 0:
            b = p  # root is in left half
        else:
            a = p  # root is in right half

    print("\nApproximate root after", max_iterations, "iterations:", round(p, 6))
    return p

# Run the method
bisection(1, 2, 0.001)
