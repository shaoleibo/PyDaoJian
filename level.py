import Tkinter
root = Tkinter.Tk()

lblExp = Tkinter.Label( root, text="Exp(“经验”)")
lblExp.pack()
txtExp = Tkinter.Entry( root )
txtExp.pack()

lblStrength = Tkinter.Label( root, text="Strength")
lblStrength.pack()
txtStrength = Tkinter.Entry( root )
txtStrength.pack()

lblDexerity = Tkinter.Label( root, text="Dexerity")
lblDexerity.pack()
txtDexerity = Tkinter.Entry( root )
txtDexerity.pack()

lblIntellect = Tkinter.Label( root, text="Intellect")
lblIntellect.pack()
txtIntellect = Tkinter.Entry( root )
txtIntellect.pack()



root.mainloop()