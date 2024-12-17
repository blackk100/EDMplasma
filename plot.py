import numpy as np
import matplotlib.pyplot as plt

# filenames = ["01", "02", "03", "04", "05", "06", "11", "12", "13", "14", "15", "16"]
filenames = ["01", "02", "06", "11", "12", "13"]
time  = []
H     = []
H_p   = []
H_m   = []
H2    = []
H2_p  = []
H2O   = []
H2O_p = []
H3O_p = []
O     = []
O_p   = []
O_2p  = []
O_3p  = []
O_m   = []
O2    = []
O2_p  = []
OH    = []
OH_p  = []
OH_m  = []
TeV   = []
Tg    = []
e     = []
# k1    = []
# k2    = []
# k3    = []
# k4    = []
# k5    = []
# k6    = []
# k7    = []
# k8    = []
# k9    = []
# k10   = []
# k11   = []
# k12   = []
# k13   = []
# k14   = []
# k15   = []
# k16   = []
# k17   = []
# k18   = []
# k19   = []
# k20   = []
# k21   = []
# k22   = []
# k23   = []
# k24   = []
# k25   = []
# k26   = []
# k27   = []
# k28   = []
# k29   = []
# k30   = []
# k31   = []
# k32   = []
# k33   = []
# k34   = []
# k35   = []
# k36   = []
# k37   = []
# k38   = []
# k39   = []
# k40   = []
# k41   = []
# k42   = []

for i in range(len(filenames)):
	filename = f'h2o_out{filenames[i]}.csv'
	data = np.genfromtxt(filename, delimiter=',', skip_header=1)
	if i == 0:
		time = data[:, 0]
	H.append(data[:, 1])
	H_p.append(data[:, 2])
	H_m.append(data[:, 3])
	H2.append(data[:, 4])
	H2_p.append(data[:, 5])
	H2O.append(data[:, 6])
	H2O_p.append(data[:, 7])
	H3O_p.append(data[:, 8])
	O.append(data[:, 9])
	O_p.append(data[:, 10])
	O_2p.append(data[:, 11])
	O_3p.append(data[:, 12])
	O_m.append(data[:, 13])
	O2.append(data[:, 14])
	O2_p.append(data[:, 15])
	OH.append(data[:, 16])
	OH_p.append(data[:, 17])
	OH_m.append(data[:, 18])
	TeV.append(data[0, 19])
	Tg.append(data[0, 20])
	e.append(data[:, 21])
	# k1.append(data[0, 22])
	# k2.append(data[0, 23])
	# k3.append(data[0, 34])
	# k4.append(data[0, 45])
	# k5.append(data[0, 56])
	# k6.append(data[0, 57])
	# k7.append(data[0, 58])
	# k8.append(data[0, 59])
	# k9.append(data[0, 60])
	# k10.append(data[0, 61])
	# # k5.append(data[0, 59])
	# # k6.append(data[0, 60])
	# # k7.append(data[0, 61])
	# # k8.append(data[0, 62])
	# # k9.append(data[0, 63])
	# k11.append(data[0, 24])
	# k12.append(data[0, 25])
	# k13.append(data[0, 26])
	# k14.append(data[0, 27])
	# k15.append(data[0, 28])
	# k16.append(data[0, 29])
	# k17.append(data[0, 30])
	# k18.append(data[0, 31])
	# k19.append(data[0, 32])
	# k20.append(data[0, 33])
	# k21.append(data[0, 35])
	# k22.append(data[0, 36])
	# k23.append(data[0, 37])
	# k24.append(data[0, 38])
	# k25.append(data[0, 39])
	# k26.append(data[0, 40])
	# k27.append(data[0, 41])
	# k28.append(data[0, 42])
	# k29.append(data[0, 43])
	# k30.append(data[0, 44])
	# k31.append(data[0, 46])
	# k32.append(data[0, 47])
	# k33.append(data[0, 48])
	# k34.append(data[0, 49])
	# k35.append(data[0, 50])
	# k36.append(data[0, 51])
	# k37.append(data[0, 52])
	# k38.append(data[0, 53])
	# k39.append(data[0, 54])
	# k40.append(data[0, 55])
	# # k41.append(data[0, 57])
	# # k42.append(data[0, 58])

time  = np.array(time)
H     = np.array(H)
H_p   = np.array(H_p)
H_m   = np.array(H_m)
H2    = np.array(H2)
H2_p  = np.array(H2_p)
H2O   = np.array(H2O)
H2O_p = np.array(H2O_p)
H3O_p = np.array(H3O_p)
O     = np.array(O)
O_p   = np.array(O_p)
O_2p  = np.array(O_2p)
O_3p  = np.array(O_3p)
O_m   = np.array(O_m)
O2    = np.array(O2)
O2_p  = np.array(O2_p)
OH    = np.array(OH)
OH_p  = np.array(OH_p)
OH_m  = np.array(OH_m)
TeV   = np.array(TeV)
Tg    = np.array(Tg)
e     = np.array(e)

# # Species
# # Single Temp
# for i in range(len(filenames)):
# 	# All
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'All species density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k-' , label=r'$e^-$'        , linewidth=1)
# 	plt.plot(time, H[8]    , 'r-' , label=r'$H$'          , linewidth=1)
# 	plt.plot(time, H_p[8]  , 'r:' , label=r'$H^+$'        , linewidth=1)
# 	plt.plot(time, H_m[8]  , 'r-.', label=r'$H^-$'        , linewidth=1)
# 	plt.plot(time, H2[8]   , 'b-' , label=r'$H_2$'        , linewidth=1)
# 	plt.plot(time, H2_p[8] , 'b:' , label=r'$H_2^+$'      , linewidth=1)
# 	plt.plot(time, H2O[8]  , 'g-' , label=r'$H_2O$'       , linewidth=1)
# 	plt.plot(time, H2O_p[8], 'g:' , label=r'${H_2O}^+$'   , linewidth=1)
# 	plt.plot(time, H3O_p[8], 'g-.', label=r'${H_3O}^+$'   , linewidth=1)
# 	plt.plot(time, O[8]    , 'm-' , label=r'$O$'          , linewidth=1)
# 	plt.plot(time, O_p[8]  , 'm:' , label=r'$O^+$'        , linewidth=1)
# 	plt.plot(time, O_m[8]  , 'm-.', label=r'$O^-$'        , linewidth=1)
# 	plt.plot(time, O_2p[8] , 'y-' , label=r'$O^{+\!+}$'   , linewidth=1)
# 	plt.plot(time, O_3p[8] , 'y:' , label=r'$O^{+\!+\!+}$', linewidth=1)
# 	plt.plot(time, O2[8]   , 'c-' , label=r'$O_2$'        , linewidth=1)
# 	plt.plot(time, O2_p[8] , 'c:' , label=r'$O_2^+$'      , linewidth=1)
# 	plt.plot(time, OH[8]   , '-'  , label=r'$OH$'         , linewidth=1, color='tab:brown')
# 	plt.plot(time, OH_p[8] , ':'  , label=r'${OH}^+$'     , linewidth=1, color='tab:brown')
# 	plt.plot(time, OH_m[8] , '-.' , label=r'${OH}^-$'     , linewidth=1, color='tab:brown')
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_all_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# Neutrals
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'Neutral species density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k-' , label=r'$e^-$'        , linewidth=1)
# 	plt.plot(time, H[8]    , 'r-' , label=r'$H$'          , linewidth=1)
# 	plt.plot(time, H2[8]   , 'b-' , label=r'$H_2$'        , linewidth=1)
# 	plt.plot(time, H2O[8]  , 'g-' , label=r'$H_2O$'       , linewidth=1)
# 	plt.plot(time, O[8]    , 'm-' , label=r'$O$'          , linewidth=1)
# 	plt.plot(time, O2[8]   , 'c-' , label=r'$O_2$'        , linewidth=1)
# 	plt.plot(time, OH[8]   , '-'  , label=r'$OH$'         , linewidth=1, color='tab:brown')
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_neu_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# H
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'$H$-atom density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k-' , label=r'$e^-$'        , linewidth=1)
# 	plt.plot(time, H[8]    , '-'  , label=r'$H$'          , linewidth=1)
# 	plt.plot(time, H_p[8]  , '-'  , label=r'$H^+$'        , linewidth=1)
# 	plt.plot(time, H_m[8]  , '-'  , label=r'$H^-$'        , linewidth=1)
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_h_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# H2
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'$H_2$ density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k:' , label=r'$e^-$'         , linewidth=1)
# 	plt.plot(time, H2[8]   , '-'  , label=r'$H_2$'         , linewidth=1)
# 	plt.plot(time, H2_p[8] , '-'  , label=r'$H_2^+$'       , linewidth=1)
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_h2_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# H2O
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'$H_2O$ density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k:' , label=r'$e^-$'          , linewidth=1)
# 	plt.plot(time, H2O[8]  , '-'  , label=r'$H_2O$'         , linewidth=1)
# 	plt.plot(time, H2O_p[8], '-'  , label=r'${H_2O}^+$'     , linewidth=1)
# 	plt.plot(time, H3O_p[8], '-'  , label=r'${H_3O}^+$'     , linewidth=1)
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_h2o_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# O
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'$O$-atom density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k:' , label=r'$e^-$'        , linewidth=1)
# 	plt.plot(time, O[8]    , '-'  , label=r'$O$'          , linewidth=1)
# 	plt.plot(time, O_p[8]  , '-'  , label=r'$O^+$'        , linewidth=1)
# 	plt.plot(time, O_m[8]  , '-'  , label=r'$O^-$'        , linewidth=1)
# 	plt.plot(time, O_2p[8] , '-'  , label=r'$O^{+\!+}$'   , linewidth=1)
# 	plt.plot(time, O_3p[8] , '-'  , label=r'$O^{+\!+\!+}$', linewidth=1)
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_o_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# O2
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'$O_2$ density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , '-'  , label=r'$e^-$'         , linewidth=1)
# 	plt.plot(time, O2[8]   , '-'  , label=r'$O_2$'         , linewidth=1)
# 	plt.plot(time, O2_p[8] , '-'  , label=r'$O_2^+$'       , linewidth=1)
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_o2_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# 	# OH
# 	plt.figure()
# 	plt.xlabel('Time [s]')
# 	plt.ylabel(r'Density $[m^{-3}]$')
# 	plt.title(r'$OH$ density vs Time for $T = $' + str(Tg[i]) + r'$K$')
# 	plt.grid(True)
# 	plt.xlim(time[0], time[-1])
# 	plt.yscale('log')
# 	plt.plot(time, e[8]    , 'k:' , label=r'$e^-$'         , linewidth=1)
# 	plt.plot(time, OH[8]   , '-'  , label=r'$OH$'          , linewidth=1)
# 	plt.plot(time, OH_p[8] , ''   , label=r'${OH}^+$'      , linewidth=1)
# 	plt.plot(time, OH_m[8] , '-'  , label=r'${OH}^-$'      , linewidth=1)
# 	plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
# 	plt.savefig('conc_oh_' + str(filenames[i]) + '.pdf', bbox_inches='tight', dpi=300)

# Final time
# All
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'All species density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e-1, 1e23)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
# plt.plot(Tg, H[:, -1]    , 'r.' , label=r'$H$'          , markersize=5)
plt.plot(Tg, H_p[:, -1]  , 'r+' , label=r'$H^+$'        , markersize=5)
plt.plot(Tg, H_m[:, -1]  , 'r*' , label=r'$H^-$'        , markersize=5)
# plt.plot(Tg, H2[:, -1]   , 'b.' , label=r'$H_2$'        , markersize=5)
# plt.plot(Tg, H2_p[:, -1] , 'b+' , label=r'$H_2^+$'      , markersize=5)
plt.plot(Tg, H2O[:, -1]  , 'g.' , label=r'$H_2O$'       , markersize=5)
plt.plot(Tg, H2O_p[:, -1], 'g+' , label=r'${H_2O}^+$'   , markersize=5)
# plt.plot(Tg, H3O_p[:, -1], 'gx' , label=r'${H_3O}^+$'   , markersize=5)
plt.plot(Tg, O[:, -1]    , 'm.' , label=r'$O$'          , markersize=5)
# plt.plot(Tg, O_p[:, -1]  , 'm+' , label=r'$O^+$'        , markersize=5)
plt.plot(Tg, O_m[:, -1]  , 'm*' , label=r'$O^-$'        , markersize=5)
# plt.plot(Tg, O_2p[:, -1] , 'y^' , label=r'$O^{+\!+}$'   , markersize=5)
# plt.plot(Tg, O_3p[:, -1] , 'yv' , label=r'$O^{+\!+\!+}$', markersize=5)
plt.plot(Tg, O2[:, -1]   , 'c.' , label=r'$O_2$'        , markersize=5)
# plt.plot(Tg, O2_p[:, -1] , 'c+' , label=r'$O_2^+$'      , markersize=5)
plt.plot(Tg, OH[:, -1]   , 'y.' , label=r'$OH$'         , markersize=5)
plt.plot(Tg, OH_p[:, -1] , 'y+' , label=r'${OH}^+$'     , markersize=5)
plt.plot(Tg, OH_m[:, -1] , 'y*' , label=r'${OH}^-$'     , markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_all_t.pdf', bbox_inches='tight', dpi=300)

# Neutrals
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'Neutral species density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e4, 1e22)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
plt.plot(Tg, H[:, -1]    , 'rv' , label=r'$H$'          , markersize=5)
plt.plot(Tg, H2[:, -1]   , 'b^' , label=r'$H_2$'        , markersize=5)
plt.plot(Tg, H2O[:, -1]  , 'g<' , label=r'$H_2O$'       , markersize=5)
plt.plot(Tg, O[:, -1]    , 'm>' , label=r'$O$'          , markersize=5)
plt.plot(Tg, O2[:, -1]   , 'cx' , label=r'$O_2$'        , markersize=5)
plt.plot(Tg, OH[:, -1]   , '+'  , label=r'$OH$'         , markersize=5, color='tab:brown')
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_neu_t.pdf', bbox_inches='tight', dpi=300)

# H
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'$H$-atom density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e-7, 1e21)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
plt.plot(Tg, H[:, -1]    , 'rv' , label=r'$H$'          , markersize=5)
plt.plot(Tg, H_p[:, -1]  , 'b^' , label=r'$H^+$'        , markersize=5)
plt.plot(Tg, H_m[:, -1]  , 'g<' , label=r'$H^-$'        , markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_h_t.pdf', bbox_inches='tight', dpi=300)

# H2
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'$H_2$ density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e-13, 1e19)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
plt.plot(Tg, H2[:, -1]   , 'rv' , label=r'$H_2$'        , markersize=5)
plt.plot(Tg, H2_p[:, -1] , 'b^' , label=r'$H_2^+$'      , markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_h2_t.pdf', bbox_inches='tight', dpi=300)

# H2O
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'$H_2O$ density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e16, 1e21)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
plt.plot(Tg, H2O[:, -1]  , 'rv' , label=r'$H_2O$'       , markersize=5)
plt.plot(Tg, H2O_p[:, -1], 'b^' , label=r'${H_2O}^+$'   , markersize=5)
# plt.plot(Tg, H3O_p[:, -1], 'g<' , label=r'${H_3O}^+$'   , markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_h2o_t.pdf', bbox_inches='tight', dpi=300)

# O
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'$O$-atom density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e-107, 1e28)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
plt.plot(Tg, O[:, -1]    , 'rv' , label=r'$O$'          , markersize=5)
plt.plot(Tg, O_p[:, -1]  , 'b^' , label=r'$O^+$'        , markersize=5)
plt.plot(Tg, O_m[:, -1]  , 'g<' , label=r'$O^-$'        , markersize=5)
plt.plot(Tg, O_2p[:, -1] , 'm>' , label=r'$O^{+\!+}$'   , markersize=5)
plt.plot(Tg, O_3p[:, -1] , 'yx' , label=r'$O^{+\!+\!+}$', markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_o_t.pdf', bbox_inches='tight', dpi=300)

# O2
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'$O_2$ density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e-12, 1e20)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'        , markersize=5)
plt.plot(Tg, O2[:, -1]   , 'rv' , label=r'$O_2$'        , markersize=5)
plt.plot(Tg, O2_p[:, -1] , 'b^' , label=r'$O_2^+$'      , markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_o2_t.pdf', bbox_inches='tight', dpi=300)

# OH
plt.figure()
plt.xlabel('Temperature [K]')
plt.ylabel(r'Density $[m^{-3}]$')
plt.title(r'$OH$ density vs Temperature')
plt.grid(True)
plt.xlim(5250, 7250)
plt.ylim(1e-2, 1e19)
plt.yscale('log')
plt.plot(Tg, e[:, -1]    , 'k.' , label=r'$e^-$'       , markersize=5)
plt.plot(Tg, OH[:, -1]   , 'rv' , label=r'$OH$'        , markersize=5)
plt.plot(Tg, OH_p[:, -1] , 'b^' , label=r'${OH}^+$'    , markersize=5)
plt.plot(Tg, OH_m[:, -1] , 'g<' , label=r'${OH}^-$'    , markersize=5)
plt.plot(Tg, e[:, -1]    , 'k.' , markersize=5)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('conc_oh_t.pdf', bbox_inches='tight', dpi=300)

# Reactions
kB = 1.380649e-23 # J / K
e  = 1.602176634e-19 # C
mH = 1.673823e-27 # kg
mO = 2.656696e-26 # kg

data = np.genfromtxt('data/elastic.txt', delimiter='	')
temps = data[:, 0]
k1  = data[:, 1]
k1[k1 == 0.0] = np.nan

data = np.genfromtxt('data/ionization_H2Op.txt', delimiter='	')
k2  = data[:, 1]
k2[k2 == 0.0] = np.nan

data = np.genfromtxt('data/ionization_OHp.txt', delimiter='	')
k3  = data[:, 1]
k3[k3 == 0.0] = np.nan

data = np.genfromtxt('data/ionization_Op.txt', delimiter='	')
k4  = data[:, 1]
k4[k4 == 0.0] = np.nan

data = np.genfromtxt('data/ionization_Hp.txt', delimiter='	')
k5  = data[:, 1]
k5[k5 == 0.0] = np.nan

data = np.genfromtxt('data/ionization_H2p.txt', delimiter='	')
k6  = data[:, 1]
k6[k6 == 0.0] = np.nan

data = np.genfromtxt('data/dissociation.txt', delimiter='	')
k7  = data[:, 1]
k7[k7 == 0.0] = np.nan

data = np.genfromtxt('data/attachment_Hm.txt', delimiter='	')
k8  = data[:, 1]
k8[k8 == 0.0] = np.nan

data = np.genfromtxt('data/attachment_Om.txt', delimiter='	')
k9  = data[:, 1]
k9[k9 == 0.0] = np.nan

data = np.genfromtxt('data/attachment_OHm.txt', delimiter='	')
k10 = data[:, 1]
k10[k10 == 0.0] = np.nan

k11 = 2.10e-15 * np.ones(np.size(temps))
k12 = 1.30e-15 * np.ones(np.size(temps))
k13 = 1.74e-14 / temps**0.5
k14 = 4.15e-14 / temps**0.5
k15 = 1.99e-16 * temps**1.78 * np.exp(-13.8  / temps)
k16 = 2.08e-13 / temps**0.76 * np.exp(-6.91  / temps)
k17 = 1.64e-10 / temps**2.04 * np.exp(-15.1  / temps)
k18 = 1.03e-14 * temps**1.61 * np.exp(-17.9  / temps)
k19 = 2.51e-13 / temps**0.8  * np.exp(-10.9  / temps)
k20 = 1.79e-13 / temps**0.87 * np.exp(-6.92  / temps)
k21 = 1.55e-46 / temps
k22 = 1.55e-46 / temps
k23 = 3.74e-17 * temps**0.28
k24 = 4.61e-46 / temps**2
k25 = 7.78e-15 * temps**0.41 * np.exp(-13.6  / temps)
k26 = 6.38e-43 * temps**1.09
k27 = 1.57e-14 * temps**0.43 * np.exp(-14.75 / temps)
k28 = 2.59e-42 / temps**1.07 * np.exp(-1.13  / temps)
k29 = 5.87e-15 * temps**0.41 * np.exp(-36.84 / temps)
k30 = 9.72e-43 / temps**1.09 * np.exp(-1.72  / temps)
k31 = 2.02e-15 * temps**0.45 * np.exp(-55.94 / temps)
k32 = 3.35e-43 / temps**1.05 * np.exp(-1     / temps)
k33 = 5.72e-16 * temps**0.5  * np.exp(-8.4   / temps)
k34 = 5.80e-15 / temps**0.83 * np.exp(-5.12  / temps)
k35 = 1.30e-14 / temps       * np.exp(-5.12  / temps)
k36 = 8.60e-46 / temps**0.33
k37 = 1.90e-45 / temps**0.5
k38 = 4.92e-42 / temps**1.27 * np.exp(-6     / temps)
k39 = 1.27e-15 * temps**1.36 * np.exp(-11.41 / temps)
k40 = 2.10e-14 / temps**0.5

temps *= e / kB # Convert to K

# k41 = 3e-2 * (8 * kB * temps / (np.pi * mH))**(0.5) / 4.0
# k42 = 2e-2 * (8 * kB * temps / (np.pi * mO))**(0.5) / 4.0

# temps *= e / kB # Convert to K

# EEDF - k1 k2 k3 k4 k5 k6 k7 k8 k9 k10

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Electron-impact reactions with EEDFs')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-30, 1e-12)
plt.yscale('log')
plt.plot(temps, k1 , '-' , label='R01 - T1', linewidth=1)
plt.plot(temps, k2 , '-.', label='R02 - T2', linewidth=1)
plt.plot(temps, k3 , '-.', label='R03 - T2', linewidth=1)
plt.plot(temps, k4 , '-.', label='R04 - T2', linewidth=1)
plt.plot(temps, k5 , '-.', label='R05 - T2', linewidth=1)
plt.plot(temps, k6 , '-.', label='R06 - T2', linewidth=1)
plt.plot(temps, k7 , '-' , label='R07 - T3', linewidth=1)
plt.plot(temps, k8 , ':' , label='R08 - T4', linewidth=1)
plt.plot(temps, k9 , ':' , label='R09 - T4', linewidth=1)
plt.plot(temps, k10, ':' , label='R10 - T4', linewidth=1)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('rxn_eedf.pdf', bbox_inches='tight', dpi=300)

# e-impact full - k1 k2 k3 k4 k5 k6 k7 k8 k9 k10 k13 k14 k15 k16 k17 k18 k19 k20 k25 k26 k27 k28 k29 k30 k31 k32 k33 k38 k39 k40

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Electron-impact reaction rates')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-19, 1e-12)
plt.yscale('log')
plt.plot(temps, k1 , ':' , label='R01 - T1', linewidth=1)
plt.plot(temps, k2 , ':' , label='R02 - T2', linewidth=1)
plt.plot(temps, k3 , ':' , label='R03 - T2', linewidth=1)
plt.plot(temps, k4 , '--', label='R04 - T2', linewidth=1)
plt.plot(temps, k5 , '--', label='R05 - T2', linewidth=1)
plt.plot(temps, k6 , '--', label='R06 - T2', linewidth=1)
plt.plot(temps, k15, '--', label='R15 - T2', linewidth=1)
plt.plot(temps, k18, '--', label='R18 - T2', linewidth=1)
plt.plot(temps, k25, '--', label='R25 - T2', linewidth=1)
plt.plot(temps, k27, '--', label='R27 - T2', linewidth=1)
plt.plot(temps, k29, '--', label='R29 - T2', linewidth=1)
plt.plot(temps, k31, '--', label='R31 - T2', linewidth=1)
plt.plot(temps, k39, '--', label='R39 - T2', linewidth=1)
plt.plot(temps, k7 , '-.', label='R07 - T3', linewidth=1)
plt.plot(temps, k16, '-.', label='R16 - T3', linewidth=1)
plt.plot(temps, k17, '-.', label='R17 - T3', linewidth=1)
plt.plot(temps, k19, '-.', label='R19 - T3', linewidth=1)
plt.plot(temps, k20, '-.', label='R20 - T3', linewidth=1)
plt.plot(temps, k33, '-.', label='R33 - T3', linewidth=1)
plt.plot(temps, k8 , '-.', label='R08 - T4', linewidth=1)
plt.plot(temps, k9 , '-.', label='R09 - T4', linewidth=1)
plt.plot(temps, k10, '-.', label='R10 - T4', linewidth=1)
plt.plot(temps, k13, '-' , label='R13 - T6', linewidth=1)
plt.plot(temps, k14, '-' , label='R14 - T6', linewidth=1)
plt.plot(temps, k40, '-' , label='R40 - T6', linewidth=1)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1), ncol=2)
plt.savefig('rxn_e.pdf', bbox_inches='tight', dpi=300)

# e-impact elastic, dissociation, attachment, dissociative recombination - k1 k7 k8 k9 k10 k13 k14 k16 k17 k19 k20 k33 k40

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Electron-impact reaction rates')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-19, 1e-12)
plt.yscale('log')
plt.plot(temps, k1 , '-' , label='R01 - T1', linewidth=1)
plt.plot(temps, k7 , '-', label='R07 - T3', linewidth=1)
plt.plot(temps, k16, '-', label='R16 - T3', linewidth=1)
plt.plot(temps, k17, '-', label='R17 - T3', linewidth=1)
plt.plot(temps, k19, '-', label='R19 - T3', linewidth=1)
plt.plot(temps, k20, '-', label='R20 - T3', linewidth=1)
plt.plot(temps, k33, '-', label='R33 - T3', linewidth=1)
plt.plot(temps, k8 , '-.', label='R08 - T4', linewidth=1)
plt.plot(temps, k9 , '-.', label='R09 - T4', linewidth=1)
plt.plot(temps, k10, '-.', label='R10 - T4', linewidth=1)
plt.plot(temps, k13, ':' , label='R13 - T6', linewidth=1)
plt.plot(temps, k14, ':' , label='R14 - T6', linewidth=1)
plt.plot(temps, k40, ':' , label='R40 - T6', linewidth=1)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('rxn_e_edadr.pdf', bbox_inches='tight', dpi=300)

# e-impact ionization - k2 k3 k4 k5 k6 k15 k18 k25 k27 k29 k31 k39

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Electron-impact ionization reaction rates')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-20, 1e-13)
plt.yscale('log')
plt.plot(temps, k2 , '-' , label='R02 - T2', linewidth=1)
plt.plot(temps, k3 , '-' , label='R03 - T2', linewidth=1)
plt.plot(temps, k4 , '-' , label='R04 - T2', linewidth=1)
plt.plot(temps, k5 , '-' , label='R05 - T2', linewidth=1)
plt.plot(temps, k6 , '-' , label='R06 - T2', linewidth=1)
plt.plot(temps, k15, '-.', label='R15 - T2', linewidth=1)
plt.plot(temps, k18, '-.', label='R18 - T2', linewidth=1)
plt.plot(temps, k25, '-.', label='R25 - T2', linewidth=1)
plt.plot(temps, k27, ':' , label='R27 - T2', linewidth=1)
plt.plot(temps, k29, ':' , label='R29 - T2', linewidth=1)
plt.plot(temps, k31, ':' , label='R31 - T2', linewidth=1)
plt.plot(temps, k39, ':' , label='R39 - T2', linewidth=1)

plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('rxn_e_i.pdf', bbox_inches='tight', dpi=300)

# e-impact recombination - k26 k28 k30 k32 k38

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Electron-impact recombination reaction rates')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-48, 1e-41)
plt.xscale('log')
plt.yscale('log')
plt.plot(temps, k26, '-' , label='R26 - T5', linewidth=1)
plt.plot(temps, k28, '-' , label='R28 - T5', linewidth=1)
plt.plot(temps, k30, '-' , label='R30 - T5', linewidth=1)
plt.plot(temps, k32, '-' , label='R32 - T5', linewidth=1)
plt.plot(temps, k38, '-' , label='R38 - T5', linewidth=1)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('rxn_e_r.pdf', bbox_inches='tight', dpi=300)

# Non e-impact - k11 k12 k21 k22 k23 k24 k34 k35 k36 k37 k41 k42

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Ion and neutral species-impact reaction rates')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-49, 1e-13)
plt.xscale('log')
plt.yscale('log')
plt.plot(temps, k11, '-' , label='R11', linewidth=1)
plt.plot(temps, k12, '-' , label='R12', linewidth=1)
plt.plot(temps, k21, ':' , label='R21', linewidth=1)
plt.plot(temps, k22, ':', label='R22', linewidth=1)
plt.plot(temps, k23, '-.', label='R23', linewidth=1)
plt.plot(temps, k24, '-.', label='R24', linewidth=1)
plt.plot(temps, k34, ':', label='R34', linewidth=1)
plt.plot(temps, k35, ':', label='R35', linewidth=1)
plt.plot(temps, k36, ':', label='R36', linewidth=1)
plt.plot(temps, k37, ':' , label='R37', linewidth=1)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
plt.savefig('rxn_non_e.pdf', bbox_inches='tight', dpi=300)

# Paper - k1 k11 k12 k13 k14 k15 k16 k17 k18 k19 k20 k23 k25 k27 k29 k31 k33 k34 k35 k39 k40

plt.figure()
plt.xlabel(r'Temperature $[K]$')
plt.ylabel(r'Reaction Rate $[m^3 s^{-1}]$')
plt.title('Reaction Rate vs Temperature')
plt.grid(True)
plt.xlim(6e2, 1e5)
plt.ylim(1e-20, 1e-12)
plt.xscale('log')
plt.yscale('log')
plt.plot(temps, k1 , '-', label='R01', linewidth=1)
plt.plot(temps, k11, '-', label='R11', linewidth=1)
plt.plot(temps, k12, '-', label='R12', linewidth=1)
plt.plot(temps, k13, '-', label='R13', linewidth=1)
plt.plot(temps, k14, '-', label='R14', linewidth=1)
plt.plot(temps, k15, '-', label='R15', linewidth=1)
plt.plot(temps, k16, '--', label='R16', linewidth=1)
plt.plot(temps, k17, '--', label='R17', linewidth=1)
plt.plot(temps, k18, '--', label='R18', linewidth=1)
plt.plot(temps, k19, '--', label='R19', linewidth=1)
plt.plot(temps, k20, '--', label='R20', linewidth=1)
plt.plot(temps, k23, '-.', label='R23', linewidth=1)
plt.plot(temps, k25, '-.', label='R25', linewidth=1)
plt.plot(temps, k27, '-.', label='R27', linewidth=1)
plt.plot(temps, k29, '-.', label='R29', linewidth=1)
plt.plot(temps, k31, '-.', label='R31', linewidth=1)
plt.plot(temps, k33, ':', label='R33', linewidth=1)
plt.plot(temps, k34, ':', label='R34', linewidth=1)
plt.plot(temps, k35, ':', label='R35', linewidth=1)
plt.plot(temps, k39, ':', label='R39', linewidth=1)
plt.plot(temps, k40, ':', label='R40', linewidth=1)
plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1), ncol=2)
plt.savefig('rxn_paper.pdf', bbox_inches='tight', dpi=300)

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

# time,H,H+,H-,H2,H2+,H2O,H2O+,H3O+,O,O+,O++,O+++,O-,O2,O2+,OH,OH+,OH-,TeV,Tg,e,rate_constant0,rate_constant1,rate_constant10,rate_constant11,rate_constant12,rate_constant13,rate_constant14,rate_constant15,rate_constant16,rate_constant17,rate_constant18,rate_constant19,rate_constant2,rate_constant20,rate_constant21,rate_constant22,rate_constant23,rate_constant24,rate_constant25,rate_constant26,rate_constant27,rate_constant28,rate_constant29,rate_constant3,rate_constant30,rate_constant31,rate_constant32,rate_constant33,rate_constant34,rate_constant35,rate_constant36,rate_constant37,rate_constant38,rate_constant39,rate_constant4,rate_constant5,rate_constant6,rate_constant7,rate_constant8,rate_constant9

# time,H,H+,H-,H2,H2+,H2O,H2O+,H3O+,O,O+,O++,O+++,O-,O2,O2+,OH,OH+,OH-,TeV,Tg,e,rate_constant0,rate_constant1,rate_constant10,rate_constant11,rate_constant12,rate_constant13,rate_constant14,rate_constant15,rate_constant16,rate_constant17,rate_constant18,rate_constant19,rate_constant2,rate_constant20,rate_constant21,rate_constant22,rate_constant23,rate_constant24,rate_constant25,rate_constant26,rate_constant27,rate_constant28,rate_constant29,rate_constant3,rate_constant30,rate_constant31,rate_constant32,rate_constant33,rate_constant34,rate_constant35,rate_constant36,rate_constant37,rate_constant38,rate_constant39,rate_constant4,rate_constant40,rate_constant41,rate_constant5,rate_constant6,rate_constant7,rate_constant8,rate_constant9

# Elastic electron-impact
# e + AB -> e + AB
# R1

# Electron-impact dissociation
# e + AB -> e + A + B
# R7 R16 R17 R19 R20 R33

# Electron-impact attachment
# e + AB -> AB-
# R8 R9 R10

# Electron-impact dissociative recombination
# e + AB+ -> A + B
# R13 R14 R40

# Electron-impact ionization
# e + AB -> e + e + AB+
# R2 R3 R4 R5 R6 R15 R18 R25 R27 R29 R31 R39

# Electron-impact recombination
# e + AB+ -> AB
# R26 R28 R30 R32 R38
