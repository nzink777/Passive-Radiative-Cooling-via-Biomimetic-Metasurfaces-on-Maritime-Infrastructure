"""
Register 1 Blueprint: Volumetric Contraction Model
Calculates the volumetric reduction of surface water based on localized 
temperature shifts induced by PDRC metasurfaces.
"""

def calculate_volume_reduction(area_m2, depth_m, delta_t, beta=2.1e-4):
    """
    Args:
        area_m2 (float): Surface area of the maritime node (m^2)
        depth_m (float): Depth of the affected water column (m)
        delta_t (float): Temperature reduction (Celsius)
        beta (float): Volumetric expansion coefficient for seawater (~2.1e-4 K^-1)
        
    Returns:
        delta_v (float): Volume reduction in cubic meters (m^3)
    """
    initial_volume = area_m2 * depth_m
    delta_v = beta * initial_volume * delta_t
    return delta_v

# Example Parameters
node_area = 500  # Example: Surface area of a standard shipping container array
water_depth = 1.0  # Top layer influence depth
cooling_delta = 2.0  # Achieved temperature reduction

reduction = calculate_volume_reduction(node_area, water_depth, cooling_delta)

print(f"--- Register 1 Simulation ---")
print(f"Surface Area: {node_area} m^2")
print(f"Targeted Depth: {water_depth} m")
print(f"Achieved Cooling: {cooling_delta} C")
print(f"Volumetric Contraction per node: {reduction:.6f} m^3")
