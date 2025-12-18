##import tkinter as tk
##
##root = tk.Tk()
##root.mainloop()



##import tkinter as tk
##
##root = tk.Tk()
##
##root.title("Day 1 - My First Tkinter Window")
##root.geometry("400x300")  # width x height in pixels
##
##root.mainloop()

##import tkinter as tk
##
##root = tk.Tk()
##
##root.title("Fixed Window Demo")
##root.geometry("400x300+200+100")  # width x height + x_offset + y_offset
##root.resizable(False, False)      # disable horizontal and vertical resize
##
##root.mainloop()

import tkinter as tk

root = tk.Tk()

root.title("Styled Window")
root.geometry("500x350+300+150")
root.resizable(True, True)

root.configure(bg="#1e1e1e")          # dark background
root.attributes("-alpha", 0.9)        # 0.0 fully transparent, 1.0 opaque

root.mainloop()





