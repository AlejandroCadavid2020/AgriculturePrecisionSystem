import tkinter as tk
from tkinter import messagebox
import random

# Función para generar datos de sensores
def get_sensor_data():
    data = {
        "Humedad del Suelo": round(random.uniform(10, 80), 2),
        "Temperatura": round(random.uniform(20, 40), 2),
        "Detección de Plagas": random.choice(["Sí", "No"]),
        "Calidad del Aire": round(random.uniform(50, 150), 2)
    }
    return data

# Función para generar datos de drones
def get_drone_data():
    area_coverage = random.randint(50, 200)  # metros cuadrados
    return f"Capturando datos de {area_coverage} m²"

# Función para mostrar alertas según los datos de sensores
def check_alerts(data):
    alerts = []
    if data["Humedad del Suelo"] < 30:
        alerts.append("⚠️ Alerta: Humedad baja en el suelo, considerar riego.")
    if data["Temperatura"] > 35:
        alerts.append("⚠️ Alerta: Temperatura alta, posible estrés térmico en cultivos.")
    if data["Detección de Plagas"] == "Sí":
        alerts.append("⚠️ Alerta: Plagas detectadas, verificar cultivos.")
    if data["Calidad del Aire"] > 100:
        alerts.append("⚠️ Alerta: Calidad del aire desfavorable, verificar efectos en los cultivos.")
    return alerts

# Función para actualizar los datos en la interfaz
def update_data():
    sensor_data = get_sensor_data()
    drone_data = get_drone_data()

    # Actualizar los datos de sensores en la interfaz
    humidity_label.config(text=f"Humedad del Suelo: {sensor_data['Humedad del Suelo']}%")
    temperature_label.config(text=f"Temperatura: {sensor_data['Temperatura']} °C")
    pest_label.config(text=f"Detección de Plagas: {sensor_data['Detección de Plagas']}")
    air_quality_label.config(text=f"Calidad del Aire: {sensor_data['Calidad del Aire']} ICAI")

    # Actualizar el reporte de drones
    drone_label.config(text=f"Reporte de Drones: {drone_data}")

    # Verificar y mostrar alertas
    alerts = check_alerts(sensor_data)
    if alerts:
        alert_message = "\n".join(alerts)
        messagebox.showwarning("Alertas del Sistema", alert_message)

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador de Agricultura de Precisión")
root.geometry("400x300")

# Etiquetas para mostrar los datos de sensores
humidity_label = tk.Label(root, text="Humedad del Suelo:", font=("Arial", 12))
humidity_label.pack(pady=5)

temperature_label = tk.Label(root, text="Temperatura:", font=("Arial", 12))
temperature_label.pack(pady=5)

pest_label = tk.Label(root, text="Detección de Plagas:", font=("Arial", 12))
pest_label.pack(pady=5)

air_quality_label = tk.Label(root, text="Calidad del Aire:", font=("Arial", 12))
air_quality_label.pack(pady=5)

# Etiqueta para mostrar el reporte de drones
drone_label = tk.Label(root, text="Reporte de Drones:", font=("Arial", 12))
drone_label.pack(pady=10)

# Botón para actualizar los datos
update_button = tk.Button(root, text="Actualizar Datos", command=update_data, font=("Arial", 12), bg="lightblue")
update_button.pack(pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
