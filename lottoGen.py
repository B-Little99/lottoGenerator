import tkinter as tk

# This creates the window object for the application
window = tk.Tk()

window.title('Lotto Generator')

label1 = tk.Label(window, text = '...', relief='groove', width = 2)
label2 = tk.Label(window, text = '...', relief='groove', width = 2)
label3 = tk.Label(window, text = '...', relief='groove', width = 2)
label4 = tk.Label(window, text = '...', relief='groove', width = 2)
label5 = tk.Label(window, text = '...', relief='groove', width = 2)
label6 = tk.Label(window, text = '...', relief='groove', width = 2)
getNumbers = tk.Button(window, text = 'Get your lotto numbers', relief='groove')
resetNumbers = tk.Button(window, text = 'Reset the numbers', relief='groove')

label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getNumbers.grid()
resetNumbers.grid()

window.geometry("500x500")

# The mainloop syntax sustains the window being open for the application
window.mainloop()