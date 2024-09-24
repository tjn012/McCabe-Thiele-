import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate equilibrium curve (y = alpha * x / (1 + (alpha - 1) * x))
def equilibrium_curve(x, alpha):
    return alpha * x / (1 + (alpha - 1) * x)

# Function to calculate the rectifying section operating line
def rectifying_line(x, R, xd):
    return (R / (R + 1)) * x + xd / (R + 1)

# Function to calculate the stripping section operating line
def stripping_line(x, xb, xf, q):
    if q == 1:
    # Handle the case where q is 1 (e.g., return a default value)
        return xb  # Replace with your desired behavior when q is 1
    else:
        return (q / (q - 1)) * (x - xb) + xb

# Streamlit app interface
st.title("Distillation Column Calculator using McCabe-Thiele Method")

# Input section for column design
st.header("Input Data for Distillation Column")

alpha = st.number_input("Relative Volatility (α)", value=2.0)
xf = st.number_input("Feed Mole Fraction (xF)", value=0.4, min_value=0.0, max_value=1.0)
xd = st.number_input("Distillate Mole Fraction (xD)", value=0.95, min_value=0.0, max_value=1.0)
xb = st.number_input("Bottom Mole Fraction (xB)", value=0.05, min_value=0.0, max_value=1.0)
R = st.number_input("Reflux Ratio (R)", value=1.5)
q = st.number_input("Feed Condition (q)", value=1.0, help="q = 1 for saturated liquid, q = 0 for saturated vapor")

# Generate x values for plotting (mole fractions)
x = np.linspace(0, 1, 500)
# Call the equilibrium_curve function and ensure it returns a numpy array
y_eq = np.array(equilibrium_curve(x, alpha))  # Convert to numpy array if necessary

# Now you can use y_eq for plotting or further calculations

# Calculate points for operating lines
y_rectifying = rectifying_line(x, R, xd)
y_stripping = stripping_line(x, xb, xf, q)

# McCabe-Thiele plot
st.header("McCabe-Thiele Diagram")

# Plotting equilibrium curve and operating lines
fig, ax = plt.subplots()

# Plot equilibrium curve
ax.plot(x, y_eq, label="Equilibrium Curve", color='blue')

# Plot rectifying section operating line
ax.plot(x, y_rectifying, label="Rectifying Line (R)", linestyle='--', color='green')

# Plot stripping section operating line
ax.plot(x, y_stripping, label="Stripping Line (q)", linestyle='--', color='red')

# Plot x = y line (45-degree line)
ax.plot(x, x, label="y = x", linestyle=':', color='black')

# Add labels and title
ax.set_xlabel("Mole Fraction of Light Component (x)")
ax.set_ylabel("Mole Fraction of Light Component (y)")
ax.set_title("McCabe-Thiele Diagram")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Conclusion and analysis
st.write("""
This McCabe-Thiele diagram shows the equilibrium curve and the operating lines for the rectifying and stripping sections of the distillation column. The reflux ratio, feed condition, and relative volatility all influence the number of theoretical stages required for the separation process.
""")