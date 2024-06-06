"""
  F27SQ - Coursework 3 - Task 2

  @author: [Basil Rehan Siddiqui]
  @userid: [H00435828]
  @campus: Dubai
      
  This is GUI program to display a progress bar that updates the progress 
  when the user presses the enter key in response to an input.
 
"""
import tkinter as tk #Importing library to use in this code

class ProgressBarGUI: #Creating new class
    def __init__(self, main):
        self.main = main
        self.main.title("Progress Bar") #Giving it a title

        self.progress_labels = []

        for i in range(10, 101, 10): #Making it start from 10, skip every 10 & end with 100
            label = tk.Label(main, text=f"{i}%", fg="red") #Making the format in percentage & starting with color red
            label.pack()
            self.progress_labels.append(label)

        self.progress_label = tk.Label(main, text="0%", fg="black", font=(28)) #Made the progress label bigger to make it stand out from the rest
        self.progress_label.pack()

        self.progress_value = 0 #The loading bar starts from 0

        self.main.bind("<Return>", self.update_progress) #Pressing enter key will update the progress bar

    def update_progress(self, event=None):
        if self.progress_value < 100:                                        #If progress value is less than 100,
            self.progress_labels[self.progress_value // 10]["fg"] = "green"  #changes the next label to green
            self.progress_value += 10                                        #Add 10% after every enter key press
            self.progress_label.config(text=f"{self.progress_value}%", fg="black")
        else:
            self.main.destroy() #Or else, end the application

if __name__ == "__main__": #To start the progress bar
    main = tk.Tk()
    app = ProgressBarGUI(main)
    main.mainloop()