from main import predict_data as pd
import numpy as np

def user_interface():
    a, b, c, d, e = float(input("Rain Possibility (0-1): ")), float(input("Important Festival (0/1):")), float(input("Weekend (0/1): ")), float(input("Traffic Last Year (0-1): ")), float(input("Government Holiday (0/1): "))
    return  pd(np.array([[a, b, c, d, e]]))

print(f"Possibility of traffic - {float(user_interface()[0][0]) * 100:.2f}%")