"""
Register 1 Blueprint: Net Radiative Cooling Power (P_cool) Simulation
Models the thermodynamic balance of PDRC metasurfaces on maritime assets.
[span_2](start_span)Ref: P_cool = P_rad - P_atm - P_sun - P_cond/conv[span_2](end_span)
"""

import numpy as np

def calculate_net_cooling_power(emissivity, reflectivity, t_surf, t_amb, h_conv=5.0):
    """
    Calculates P_cool (W/m^2).
    
    Args:
        emissivity (float): Spectral emissivity in the 8-13 um window (0 to 1).
        reflectivity (float): Solar reflectivity in the 0.3-2.5 um window (0 to 1).
        t_surf (float): Surface temperature of the metasurface (Kelvin).
        t_amb (float): Ambient air temperature (Kelvin).
        h_conv (float): Combined conductive/convective heat transfer coefficient (W/m^2K).
        
    Returns:
        p_cool (float): Net cooling power (W/m^2).
    """
    # Physical Constants
    sigma = 5.67e-8  # Stefan-Boltzmann constant (W/m^2K^4)
    solar_intensity = 1000  # Incident solar radiation (W/m^2)
    
    # Radiative Emission (P_rad - P_atm)
    # Simplified net radiative flux in the atmospheric window
    p_rad_net = emissivity * sigma * (t_surf**4 - t_amb**4)
    
    # Solar Absorption (P_sun)
    p_sun = solar_intensity * (1 - reflectivity)
    
    # Conductive/Convective Losses (P_cond/conv)
    p_conv = h_conv * (t_surf - t_amb)
    
    # Total Cooling Power
    # We define positive as net cooling (heat rejection)
    p_cool = p_rad_net - p_sun - p_conv
    
    return p_cool

# --- Simulation Execution ---
# Optimized Metasurface Parameters
t_surface = 300  # 27 Celsius
t_ambient = 300  # 27 Celsius
[span_3](start_span)emissivity_val = 0.95 # Near-unity emissivity[span_3](end_span)
[span_4](start_span)reflectivity_val = 0.96 # High solar reflectivity[span_4](end_span)

cooling_power = calculate_net_cooling_power(emissivity_val, reflectivity_val, t_surface, t_ambient)

print(f"--- Register 1 Thermal Simulation ---")
print(f"Emissivity: {emissivity_val}")
print(f"Solar Reflectivity: {reflectivity_val}")
print(f"Net Cooling Power (P_cool): {cooling_power:.2f} W/m^2")

if cooling_power > 0:
    print("Result: Net cooling achieved.")
else:
    print("Result: Surface is heating up.")
  
