


# Create the root window
root = Tk()
root.title('Image Window')  # Set the title of the window
root.geometry('400x400')  # Set the size of the window

# Open and identify the image
image_file = Image.open("images.jpeg")  # Ensure the file path is correct
upload = ImageTk.PhotoImage(image_file)  # Convert the image to a format compatible with Tkinter

# Add the image to a label
label = Label(root, image=upload, height=350, width=300)
label.place(x=50, y=0)  # Place the image label in the window

# Add a text label below the image
label2 = Label(root, text="This is how you add an image in Tkinter Window")
label2.place(x=40, y=360)  # Position the text label

# Run the application
root.mainloop()
