
import numpy as np

from optiland import optic, optimization

lens = optic.Optic()
lens2 = optic.Optic()

# add surfaces
lens.add_surface(index=0, radius=np.inf, thickness=np.inf)
lens.add_surface(index=1, radius=50, thickness=3, material="SK16", is_stop=True,surface_type="even_asphere", coefficients=[-2.248851e-4, -4.690412e-6, -6.404376e-8])
lens.add_surface(index=2, radius=-50, thickness=30,surface_type="even_asphere", coefficients=[0, 0, 0])
lens.add_surface(index=3)

# set aperture
lens.set_aperture(aperture_type="EPD", value=10)


# set fields
lens.set_field_type(field_type="angle")
lens.add_field(y=0)

# set wavelengths
lens.add_wavelength(value=0.48)
lens.add_wavelength(value=0.55, is_primary=True)
lens.add_wavelength(value=0.65)

lens.draw()

print("Before")
print(lens.surface_group.surfaces[1].geometry.coefficients)
print(lens.surface_group.surfaces[2].geometry.coefficients)
    
    
lens.pickups.add(
    source_surface_idx=1,
    attr_type="coefficients",
    target_surface_idx=2,
)
    
print("After")
print(lens.surface_group.surfaces[1].geometry.coefficients)
print(lens.surface_group.surfaces[2].geometry.coefficients)