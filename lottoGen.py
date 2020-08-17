import tkinter as tk

# This creates the window object for the application
window = tk.Tk()

img = tk.PhotoImage(file = 'logo.gif')

window.title('Lotto Generator')
window.resizable(0, 0)

# Creating the widgets
imageLabel = tk.Label(window, image = img)
label1 = tk.Label(window, text = '...', relief='groove', width = 2)
label2 = tk.Label(window, text = '...', relief='groove', width = 2)
label3 = tk.Label(window, text = '...', relief='groove', width = 2)
label4 = tk.Label(window, text = '...', relief='groove', width = 2)
label5 = tk.Label(window, text = '...', relief='groove', width = 2)
label6 = tk.Label(window, text = '...', relief='groove', width = 2)
getNumbers = tk.Button(window, text = 'Get Your Lotto Numbers')
resetNumbers = tk.Button(window, text = 'Reset Numbers')

# Designing the layout of the widgets
imageLabel.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = (10, 20))
getNumbers.grid(row = 2, column = 2, columnspan = 4)
resetNumbers.grid(row = 2, column = 6, columnspan = 2)





# The mainloop syntax sustains the window being open for the application
window.mainloop()