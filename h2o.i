[Mesh]
	type = GeneratedMesh
	dim = 1
	xmin = 0
	xmax = 1
	nx = 1
[]

[Variables]
	# ODE variables
	[e]
		family = SCALAR
		order = FIRST
		initial_condition = 2.366889807e17
	[]
	[H]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[H+]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[H-]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O+]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O++]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O+++]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O-]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[H2]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[H2+]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O2]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[O2+]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[OH]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[OH+]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[OH-]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
	[H2O]
		family = SCALAR
		order = FIRST
		initial_condition = 1.577926538e20
	[]
	[H2O+]
		family = SCALAR
		order = FIRST
		initial_condition = 2.366889807e17
	[]
	[H3O+]
		family = SCALAR
		order = FIRST
		initial_condition = 0
	[]
[]

[ScalarKernels]
	[de_dt]
		type = ODETimeDerivative
		variable = e
	[]
	[dH_dt]
		type = ODETimeDerivative
		variable = H
	[]
	[dH+_dt]
		type = ODETimeDerivative
		variable = H+
	[]
	[dH-_dt]
		type = ODETimeDerivative
		variable = H-
	[]
	[dO_dt]
		type = ODETimeDerivative
		variable = O
	[]
	[dO+_dt]
		type = ODETimeDerivative
		variable = O+
	[]
	[dO++_dt]
		type = ODETimeDerivative
		variable = O++
	[]
	[dO+++_dt]
		type = ODETimeDerivative
		variable = O+++
	[]
	[dO-_dt]
		type = ODETimeDerivative
		variable = O-
	[]
	[dH2_dt]
		type = ODETimeDerivative
		variable = H2
	[]
	[dH2+_dt]
		type = ODETimeDerivative
		variable = H2+
	[]
	[dO2_dt]
		type = ODETimeDerivative
		variable = O2
	[]
	[dO2+_dt]
		type = ODETimeDerivative
		variable = O2+
	[]
	[dOH_dt]
		type = ODETimeDerivative
		variable = OH
	[]
	[dOH+_dt]
		type = ODETimeDerivative
		variable = OH+
	[]
	[dOH-_dt]
		type = ODETimeDerivative
		variable = OH-
	[]
	[dH2O_dt]
		type = ODETimeDerivative
		variable = H2O
	[]
	[dH2O+_dt]
		type = ODETimeDerivative
		variable = H2O+
	[]
	[dH3O+_dt]
		type = ODETimeDerivative
		variable = H3O+
	[]
[]

[ChemicalReactions]
	[ScalarNetwork]
		species = 'e H H+ H- O O+ O++ O+++ O- H2 H2+ O2 O2+ OH OH+ OH- H2O H2O+ H3O+'
		file_location = 'data'

		equation_constants = 'kB pi mH mO'
		equation_values = '1.380649e-23 3.141592 1.673823e-27 2.656696e-26'
		equation_variables = 'Tg'
		sampling_variable = 'Tg'

		reactions = 'e + H2O -> e + H2O        : EEDF (elastic)                            # R1
		            e + H2O -> e + e + H2O+    : EEDF (ionization_H2Op)                    # R2
		            e + H2O -> e + e + H + OH+ : EEDF (ionization_OHp)                     # R3
		            e + H2O -> O+ + H2 + e + e : EEDF (ionization_Op)                      # R4
		            e + H2O -> e + e + H+ + OH : EEDF (ionization_Hp)                      # R5
		            e + H2O -> O + H2+ + e + e : EEDF (ionization_H2p)                     # R6
		            e + H2O -> H + OH + e      : EEDF (dissociation)                       # R7
		            e + H2O -> H- + OH         : EEDF (attachment_Hm)                      # R8
		            e + H2O -> H2 + O-         : EEDF (attachment_Om)                      # R9
		            e + H2O -> OH- + H         : EEDF (attachment_OHm)                     # R10
		            H2O+ + H2O -> H30+ + OH    : 2.10e-15                                  # R11
		            OH+ + H2O -> H30+ + O      : 1.30e-15                                  # R12
		            e + H3O+ -> H2O + H        : {1.74e-14 / Tg^(0.5)}                     # R13
		            e + H3O+ -> OH + H + H     : {4.15e-14 / Tg^(0.5)}                     # R14
		            e + OH -> e + e + OH+      : {1.99e-16 * Tg^(1.78) * exp(-13.8  / Tg)} # R15
		            e + OH -> e + O + H        : {2.08e-13 / Tg^(0.76) * exp(-6.91  / Tg)} # R16
		            e + OH+ -> e + O + H+      : {1.64e-10 / Tg^(2.04) * exp(-15.1  / Tg)} # R17
		            e + H2 -> e + e + H2+      : {1.03e-14 * Tg^(1.61) * exp(-17.9  / Tg)} # R18
		            e + H2 -> e + H + H        : {2.51e-13 / Tg^(0.8)  * exp(-10.9  / Tg)} # R19
		            e + H2+ -> e + H+ + H      : {1.79e-13 / Tg^(0.87) * exp(-6.92  / Tg)} # R20
		            H + H + H -> H2 + H        : {1.55e-46 / Tg}                           # R21
		            H + H + H2 -> H2 + H2      : {1.55e-46 / Tg}                           # R22
		            O + OH -> H + O2           : {3.74e-17 * Tg^(0.28)}                    # R23
		            H + H + OH -> H2O + H      : {4.61e-46 / Tg^(2)}                       # R24
		            e + H -> e + e + H+        : {7.78e-15 * Tg^(0.41) * exp(-13.6  / Tg)} # R25
		            e + e + H+ -> H + e        : {6.38e-43 * Tg^(1.09)}                    # R26
		            e + O -> e + e + O+        : {1.57e-14 * Tg^(0.43) * exp(-14.75 / Tg)} # R27
		            e + e + O+ -> O + e        : {2.59e-42 / Tg^(1.07) * exp(-1.13  / Tg)} # R28
		            e + O+ -> e + e + O++      : {5.87e-15 * Tg^(0.41) * exp(-36.84 / Tg)} # R29
		            e + e + O++ -> O+ + e      : {9.72e-43 / Tg^(1.09) * exp(-1.72  / Tg)} # R30
		            e + O++ -> e + e + O+++    : {2.02e-15 * Tg^(0.45) * exp(-55.94 / Tg)} # R31
		            e + e + O+++ -> O++ + e    : {3.35e-43 / Tg^(1.05) * exp(-1     / Tg)} # R32
		            e + O2 -> e + O + O        : {5.72e-16 * Tg^(0.5)  * exp(-8.4   / Tg)} # R33
		            O2 + O2 -> O + O + O2      : {5.80e-15 / Tg^(0.83) * exp(-5.12  / Tg)} # R34
		            O2 + O -> O + O + O        : {1.30e-14 / Tg        * exp(-5.12  / Tg)} # R35
		            O + O + O2 -> O2 + O2      : {8.60e-46 / Tg^(0.33)}                    # R36
		            O + O + O -> O2 + O        : {1.90e-45 / Tg^(0.5)}                     # R37
		            e + e + H2O+ -> H2O + e    : {4.92e-42 / Tg^(1.27) * exp(-6     / Tg)} # R38
		            e + O2 -> e + e + O2+      : {1.27e-15 * Tg^(1.36) * exp(-11.41 / Tg)} # R39
		            e + O2+ -> O + O           : {2.10e-14 / Tg^(0.5)}'                    # R40
					# H + H -> H2                : {3e-2 * (8 * kB * Tg / (pi * mH))^(0.5) / 4.0} # R41
					# O + O -> O2                : {2e-2 * (8 * kB * Tg / (pi * mO))^(0.5) / 4.0}' # R42
	[]
[]

[AuxVariables]
	[Tg_kelvin]
		order = FIRST
		family = SCALAR
		initial_condition = 7354.7
	[]
	[Tg]
		order = FIRST
		family = SCALAR
	[]
[]

[AuxScalarKernels]
	[temperature_convert]
		type = ParsedAuxScalar
		variable = Tg
		constant_names = 'kB qe'
		constant_expressions = '1.380649e-23 1.602176634e-19'
		args = 'Tg_kelvin'
		function = 'Tg_kelvin * kB / qe'
		execute_on = 'INITIAL'
	[]
[]

[Debug]
	show_var_residual_norms = true
[]

[Executioner]
	type = Transient
	end_time = 5e-6
	solve_type = 'linear'
	dt = 0.02e-6
[]

[Preconditioning]
	[smp]
		type = SMP
		full = true
	[]
[]

[Outputs]
	[out]
		type = CSV
		time_step_interval = 1
	[]
	[console]
		type = Console
		execute_scalars_on = 'none'
	[]
[]

# Case			Paper
# No.	Temp	No.		Gap		H2O				e/i
# 1		5325.7	3-exp	0.5e-6	1.371957576e20	2.057936365e17
# 2		6171.1	5-exp	0.5e-6	1.371957576e20	2.057936365e17
# 3		6184.7	1-num	0.5e-6	1.371957576e20	2.057936365e17
# 4		6691.5	5-num	0.5e-6	1.371957576e20	2.057936365e17
# 5		6789.0	3-num	0.5e-6	1.371957576e20	2.057936365e17
# 6		7181.5	1-exp	0.5e-6	1.371957576e20	2.057936365e17
# 11	5602.5	4-exp	1.0e-6	1.577926538e20	2.366889807e17
# 12	6446.5	2-exp	1.0e-6	1.577926538e20	2.366889807e17
# 13	6576.8	6-exp	1.0e-6	1.577926538e20	2.366889807e17
# 14	6668.9	2-num	1.0e-6	1.577926538e20	2.366889807e17
# 15	7250.1	6-num	1.0e-6	1.577926538e20	2.366889807e17
# 16	7354.7	4-num	1.0e-6	1.577926538e20	2.366889807e17
