import cv2
import numpy as np

def ordenarpuntos(puntos):
    n_puntos= np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3])
