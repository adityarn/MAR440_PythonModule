def plot_one_var(var, depth, ax, xlabel="", ylabel="Depth (m)"):
    ax.plot(var, depth)
    

def plot_multiple_variables(depth, temp, sal, oxy, sigma0, wd = 190/25.4, ht=230/25.4):
    plt.rcParams.update({'font.size': 10})
    plt.figure(figsize=(wd, ht))
    ax = plt.subplot()
    
    ax.plot(temp, -depth, color="r")
    
    ax2 = ax.twiny()
    ax2.plot(sal, -depth, color="b")
    
    ax3 = ax.twiny()
    ax3.spines.top.set_position(("axes", 1.1))
    ax3.plot(oxy, -depth, color="k")
    
    ax4 = ax.twiny()
    ax4.xaxis.set_ticks_position("bottom")
    ax4.xaxis.set_label_position("bottom")

    ax4.spines["bottom"].set_position(("axes", -0.1))
    ax4.plot(sigma0, -depth, color="g")
    
    ax.set_xlabel("Temperature ($^\circ$C)", color="r")
    ax2.set_xlabel("Salinity (PSU)", color="b")
    ax3.set_xlabel("Oxygen (ml/l)", color="k")
    ax4.set_xlabel("sigma$_0$ (kg/m$^3$)", color="g")
    
    
    
    ax.set_ylabel("Depth (m)")
    
    ax.grid(color="0.5", linewidth=1)
    #ax2.grid(color="b", linewidth=0.1)
    #ax3.grid(color="k", linewidth=0.1)
    
    
plot_multiple_variables(stn6_binned["Depth"], stn6_binned["TempAvg"], stn6_binned["SalAvg"], stn6_binned["Oxy1"], stn6_binned["sigma0"])