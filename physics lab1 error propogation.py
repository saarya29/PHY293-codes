def error(V, I, R, V_err, I_err, R_err):
    #Step 1: 
    R_i_values = []
    for i in range(len(R)):
        R_amm = V[i]/I[i] - R[i]
        #Step 2: error propogation (V/I)error
        R_total_err = (((V_err[i]/V[i])**2 + (I_err[i]/I[i])**2)**0.5)*(V[i]/I[i])
        #Step 3: 
        r_amm_error = (R_total_err**2 + R_err[i]**2)**0.5
        print("R_amm =", R_amm, "±", r_amm_error)
        R_i_values.append(R_amm)
    return R_i_values

R1 = [99.17, 2699.9, 26890, 101460]
R_err1 = [0.19834, 5.3998, 53.78, 202.92]
V1 = [6.496,6.5, 6.5,6.5]
V_err1 = [5.25E-03, 5.25E-03, 5.25E-03, 5.25E-03]
I1 = [0.0648,0.0018, -0.0001, -0.0003]	
I_err1 = [6.30E-04, 5.04E-04, 5.00E-04, 5.01E-04]

error(V1, I1, R1, V_err1, I_err1, R_err1)




def option2_error(R, V, I, R_err, V_err, I_err):
    #Step 1:
    R_v_values = []
    for i in range(len(R)):
        I_resistor = V[i]/R[i]
        I_resistor_err = (((R_err[i]/R[i])**2 + (V_err[i]/V[i])**2)**0.5)*(I_resistor)
        I_amm = I[i] - I_resistor
        I_amm_err = (I_resistor_err**2 + I_err[i]**2)**0.5
        R_voltmeter = V[i]/I_amm
        R_voltmeter_err = (((V_err[i]/V[i])**2 + (I_amm_err/I_amm)**2)**0.5)*(R_voltmeter)
        print("R_voltmeter =", R_voltmeter, "±", R_voltmeter_err)
        R_v_values.append(R_voltmeter) 
    return R_v_values
    
R = [99.17, 2699.9, 26890, 101460]
R_err = [0.19834, 5.3998, 53.78, 202.92]
V = [6.496,6.5, 6.5,6.5]
V_err = [5.25E-03, 5.25E-03, 5.25E-03, 5.25E-03]
I = [6.50E-05, 2.00E-06, -3.00E-08, -3.00E-08]
I_err = [3.30E-04, 2.01E-04, 2.01E-04, 2.01E-04]

option2_error(R, V, I, R_err, V_err, I_err)


def part3(r,v,i, r_err, v_errr,i_err,):
    r1_values = []
    for j in range(len(r)):
        #First we calculate m1 and its error
        m_1 = v[j]/i[j]
        m1_err = (((v_errr[j]/v[j])**2 + (i_err[j]/i[j])**2)**0.5)*(m_1)
        R_1 = (m_1*r)/(m_1 + r)
        R1_numerator_err = (((m1_err/m_1)**2 + (r_err[j]/r[j])**2)**0.5)*(m_1*r[j])
        R1_denominator_err = (((m1_err)**2 + (r[j])**2)**0.5)
        R1_err = ((R1_numerator_err/(m_1*r[j]))**2 + (R1_denominator_err/(m_1 + r[j]))**2)**0.5 *(R_1)
        print("R1 =", R_1, "±", R1_err)
        r1_values.append(R_1)
    return r1_values

