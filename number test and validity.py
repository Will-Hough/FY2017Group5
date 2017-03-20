import Tkinter

main = Tkinter.Tk()

#assuming the panel is on the equator and sunlight hits at the normal to the panel constantly 

def paneltoenergy():
    panellength=raw_input("Panel Length:")
    panelwidth=raw_input("Panel Width:")

    if panellength.isdigit() != True:
         print "Invalid Length Input"

    if panelwidth.isdigit() != True:
        print "Invalid Width Input"
        

    #Total energy from sun is 1850 watts per square meter
        length=float(panellength)
        width=float(panelwidth)
        size = length*width

    raw_energy = size*1850

    #assuming that half of the energy is lost into the atmosphere

    energy_output = raw_energy/2

    def calor_input_e(c=4.19, t=20):
        Q = energy_output
        t = float(raw_input("Please enter the temperature of the water. "))

        m = Q/(c*(100-t))

        return m

    print "You will be able to boil " + str(calor_input_e()) + " litres of water."




def energytopanel():

    def calor_output_e(m=1.57,c=4.19,t=20):
        m = float(raw_input("Please enter how many litres of water there are. "))
        t = float(raw_input("Please enter the temperature. "))
        global q
        q=m*c*(100-t)  

    calor_output_e()
    
    energyinput = q

    raw_energy=energyinput*2

    size = (raw_energy / 1850)

    squares = str(size)

    print "You will need " + str(squares) + " metres squared of solar panels."


ptoe  = Tkinter.Button(main, text="Panel To Energy", command = paneltoenergy)
etop = Tkinter.Button(main, text="Energy to Panel", command = energytopanel)

ptoe.pack()
etop.pack()

main.mainloop()







print "You will need the following amount of energy (in Joules) " + str(calor_output_e()) + " to boil the water."

