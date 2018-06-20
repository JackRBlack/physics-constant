# This is a module including physical constant.

# The author is Wenjie Chen. Contact me via E-mail: wenjiechen@pku.edu.cn

# Established on Jun 18th, 2018.
# Last edited on Jun 20th, 2018.

# Part 1: physical contant

# Universal constants

c = 299792458 # <c> [m s^-1] {defined} <the speed of light in vacuum>

G = 6.67408e-11 # <G> [m^3 kg^-1 s^-2] {4.7e-5} <Newtonian constant of gravitation>

h = 6.626070040e-34 # <h> [J s] {1.2e-8} <Planck constant>

hbar = 1.054571800e-34 # <\hbar> [J s] {1.2e-8} <reduced Planck constant, hbar = h/(2*pi)>

# Electromagnetic constants

mu_0 = 1.256637061e-6 # <\mu_0> [N A^-2] {defined} <magnetic constant (vacuum permeability), defined to be 4*pi*1e-7>

e_0 = 8.854187817e-12 # <\epsilon_0> [F m^-1] {defined} <electric constant (vacuum permittivity), defined to be 1/(mu_0*c^2)>

k_e = 8.9875517873681764e9 # <k_e> [kg m^3 s^-4 A^-2] {defined} <Coulomb's constant, defined to be 1/(4*pi*e_0)>

e = 1.6021766208e-19 # <e> [C] {6.1e-9} <elementary charge>

# Atomic and nuclear constants

a = 7.2973525664e-3 # <\alpha> [] {2.3e-10} <fine-structure constant, defined to be e^2/(4*pi*e_0*hbar*c)>

m_e = 9.10938356e-31 # <m_e> [kg] {1.2e-8} <electron mass>

m_p = 1.672621898e-27 # <m_e> [kg] {1.2e-8} <proton mass>

a_0 = 5.2917721067e-11 # <a_0> [m] {2.3e-9} <Bohr radius, defined to be hbar/(a*m_e*c)>

r_e = 2.8179403227e-15 # <r_e> [m] {6.8e-10} <classical electron radius, defined to be e^2/(4*pi*e_0*m_e*c^2)>

# Physico-chemical constants

N_A = 6.022140858e23 # <N_A> [mol^-1] {1.2e-8} <Avogadro constant>

k_B = 1.38064853e-23 # <k_B> [J K^-1] {5.7e-7} <Boltzmann constant>

R = 8.3144598 # <R> [J mol^-1 K^-1] {5.7e-7} <gas constant, R = N_A * k_B>

m_u = 1.660539040e-27 # <m_u> [kg] {1.2e-8} <atomic mass constant>

# Adopted values

g_n = 9.80665 # <g_n> [m s^-2] {defined} <standard acceleration of gravity>

atm = 101325 # <atm> [Pa] {defined} <standard atmosphere>


# Part 2: unit conversion

# Temperature

def C_2_F(varA):
    '''
        Convert Celsius to Fahrenheit.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Celsius.
            
        returns:
            varB : [double] A value in Fahrenheit.
            
        example:
            T_F = C_2_F(26.5)
    '''
    
    if varA < -273.15:
        raise ValueError('Temperature cannot be lower than -273.15 °C (0 K)!')
    varB = varA * 1.8 + 32
    return varB

def F_2_C(varA):
    '''
        Convert Fahrenheit to Celsius.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Fahrenheit.
            
        returns:
            varB : [double] A value in Celsius.
            
        example:
            T_C = F_2_C(40.5)
    '''
    
    if varA < -459.67:
        raise ValueError('Temperature cannot be lower than -459.67 °F (0 K)!')
    varB = (varA - 32) / 1.8
    return varB

def C_2_K(varA):
    '''
        Convert Celsius to Kelvin.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Celsius.
            
        returns:
            varB : [double] A value in Kelvin.
            
        example:
            T_K = C_2_K(26.5)
    '''
    if varA < -273.15:
        raise ValueError('Temperature cannot be lower than -273.15 °C (0 K)!')
    varB = varA + 273.15
    return varB

def K_2_C(varA):
    '''
        Convert Kelvin to Celsius.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Kelvin.
            
        returns:
            varB : [double] A value in Celsius.
            
        example:
            T_C = K_2_C(0)
    '''
    if varA < 0:
        raise ValueError('Temperature cannot be lower than 0 K!')
    varB = varA - 273.15
    return varB

def F_2_K(varA):
    '''
        Convert Fahrenheit to Kelvin.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Fahrenheit.
            
        returns:
            varB : [double] A value in Kelvin.
            
        example:
            T_K = F_2_K(40.5)
    '''
    
    if varA < -459.67:
        raise ValueError('Temperature cannot be lower than -459.67 °F (0 K)!')
    varB = (varA - 32) / 1.8 + 273.15
    return varB

def K_2_F(varA):
    '''
        Convert Kelvin to Fahrenheit.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Kelvin.
            
        returns:
            varB : [double] A value in Fahrenheit.
            
        example:
            T_F = K_2_F(0)
    '''
    if varA < 0:
        raise ValueError('Temperature cannot be lower than 0 K!')
    varB = (varA - 273.15) * 1.8 + 32
    return varB

# Energy

def J_2_eV(varA):
    '''
        Convert joule to electronvolt.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in joule.
            
        returns:
            varB : [double] A value in electronvolt.
            
        example:
            E_eV = J_2_eV(5.0)
    '''
    varB = varA / e
    return varB

def eV_2_J(varA):
    '''
        Convert electronvolt to joule.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in electronvolt.
            
        returns:
            varB : [double] A value in joule.
            
        example:
            E_J = eV_2_J(1.0)
    '''
    varB = varA * e
    return varB

