import matplotlib.pyplot as plt
import pandas as pd

datos = {
"Nombre": ["jean Carlos", "Luis", "María", "Pedro"],
"Edad": [22, 17, 16, 18],
"Nota": [96, 90, 78, 92]
}
df = pd.DataFrame(datos)
print("data frame")
print(df)
print("promedio")
print(df["Nota"].mean())
print("nota más alta")
print(df.loc[df["Nota"].idxmax()])
df.plot(x="Nombre", y="Nota", kind="bar")
print (plt.show())
