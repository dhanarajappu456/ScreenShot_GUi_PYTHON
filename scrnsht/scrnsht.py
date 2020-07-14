import time
import pyautogui
import tkinter as tk
def scrn():
    name_var=round(time.time())
    name_in_string='{}.png'.format(name_var)
    time.sleep(5)
    img=pyautogui.screenshot(name_in_string)
    img.show()


root=tk.Tk()
frame=tk.Frame(
    root
    
)
frame.pack()
scr=tk.Button(
    frame,
    text="snap me!!!",
    command=scrn
)
scr.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text="quit",
    command=quit
    
    
    
)
close.pack(side=tk.LEFT)
owner=tk.Label(root,
               text="created by Dhanaraj\n-------------copyright issued",
            
               anchor="se"
               
               
               
               
                
               )
owner.pack(side=tk.BOTTOM)


root.mainloop()
