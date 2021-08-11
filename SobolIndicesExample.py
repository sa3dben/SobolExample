# Copyright
# Saad Benjelloun
# all rights reserved
# example inspired from the one in Sobol's paper : 
from sympy import *
#init_printing(use_unicode=False, wrap_line=False)
x, x1, x2 ,x3 = symbols('x  x1  x2  x3')
phi1 = abs(4*x1-2);
phi2 = abs(4*x2-2);
phi3 = abs(4*x3-2)/4 + 3 /4;
integrate(phi1, (x1,0,1))
integrate(phi2, (x2,0,1))
integrate(phi3, (x3,0,1))
# construct f as the product of the three function
f = phi1*phi2*phi3
f
# conpute integral of f
f0= integrate( integrate (integrate(f, (x3,0,1)), (x2,0,1)), (x1,0,1))
f0
f1 = phi1 - f0; f2 = phi2 - f0; f3 = phi3 - f0;

f1 = phi1 - 1; f2 = phi2 - 1; f3 = phi3 -1;
f23 = phi2*phi3 - phi2 - phi3 + 1
f123 = f - phi1*phi2 -  phi1*phi3 - phi2*phi3 + phi1 + phi2 + phi3 - 1  
f12 = phi1*phi2 - phi1 - phi2 + 1
f13 = phi1*phi3 - phi1 - phi3 + 1
# 22/27
V = integrate( integrate (integrate(f**2, (x3,0,1)), (x2,0,1)), (x1,0,1))  - 1
V
V1 = integrate(f1**2,  (x1,0,1)) 
V1
V2 = integrate(f2**2,  (x2,0,1)) 
V2
V3 = integrate(f3**2,  (x3,0,1)) 
V3
V12 = integrate (integrate(f12**2, (x1,0,1)), (x2,0,1)); 
V13 = integrate (integrate(f13**2, (x1,0,1)), (x3,0,1)); 
V23 = integrate (integrate(f23**2, (x2,0,1)), (x3,0,1));
V123 = integrate( integrate (integrate(f123**2, (x3,0,1)), (x2,0,1)), (x1,0,1)) 
V123
# = V = 22/27
V1+V2+V3+V12+V13+V23+V123
S1 = V1/V; S2 = V2/V; S3= V3/V; 
S12 = V12/V; S13 = V13/V; S23= V23/V; 
S123= V123/V;
