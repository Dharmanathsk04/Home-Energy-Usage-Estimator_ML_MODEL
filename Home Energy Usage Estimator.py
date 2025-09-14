import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression

X=[[2,5],[3,6],[4,7],[5,8],[6,9]]

y=[10,12,14,16,18]

model=LinearRegression()

model.fit(X,y)

def predict_energy():
    appliances=int(app_entry.get())
    hours=int(hour_entry.get())
    prediction=model.predict([[appliances,hours]])[0]
    messagebox.showinfo("Prediction",f"Estimated energy usage: {prediction:.2f} kWh")

root=tk.Tk()

root.title("Home Energy Usage Estimator")

tk.Label(root,text="Number of Appliances:").pack()
app_entry=tk.Entry(root); app_entry.pack()

tk.Label(root,text="Hours of Usage:").pack()
hour_entry=tk.Entry(root); hour_entry.pack()

tk.Button(root,text="Predict",command=predict_energy).pack()
root.mainloop()
