G = 6.674 * 10**(-11)
M_earth = 5.974 * 10**24
R_earth = 6378100
r = 1.2
h = 0

M = 0.029
R = 8.31
T = 273

S = 0.0314
Cq = 0.5
m = 100
m_second = 40
m_end = 10.5
V_jet = 1500
mu = 1.15
V = 0

t = 0
dt = 0.1

#while (h <= 30000):
#    g = -G*M_earth/(R_earth + h)**2
#    dh = 10
#    dr = M*r*g*dh/(R*T)
#    h += dh
#    r += dr

#    print(h,'meters   ',r,'kg/m^3')
    
while (m > 52):

    if (m > m_end):   
        F_traction = mu*V_jet
    else:
        F_traction = 0
    g = -G*M_earth/(R_earth + h)**2
    F_gravity = g*m
    Q = -Cq*r*V**2/2*S

    a = (F_traction + F_gravity + Q)/m
    dV = a*dt
    dh = V*dt + a*dt**2/2
    dr = M*r*g*dh/(R*T)
    if (m > m_end):   
        dm = -mu * dt
    else:
        dm = 0

    V += dV
    h += dh
    r += dr
    m += dm
    t += dt

    #print(r)
    print(V,'m/s   ',h,'meters   ',a,'m/s^2    ',m,'kg   ',t)

m = 40

while (V >= 0):

    if (m > m_end):   
        F_traction = mu*V_jet
    else:
        F_traction = 0
    g = -G*M_earth/(R_earth + h)**2
    F_gravity = g*m
    Q = -Cq*r*V**2/2*S

    a = (F_traction + F_gravity + Q)/m
    dV = a*dt
    dh = V*dt + a*dt**2/2
    dr = M*r*g*dh/(R*T)
    if (m > m_end):   
        dm = -mu * dt
    else:
        dm = 0

    V += dV
    h += dh
    r += dr
    m += dm
    t += dt

    #print(r)
    print(V,'m/s   ',h,'meters   ',a,'m/s^2    ',m,'kg   ',t)

