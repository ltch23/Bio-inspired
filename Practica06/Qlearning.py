import numpy as np

class Qlearning:
    def __init__(self, alpha=0.25, gamma=0.6,):
        self.Q = {}
        self.alpha = alpha
        self.gamma = gamma

    def predecir(self, estado):
        if (estado not in self.Q.keys()):
            self.Q[estado] = np.random.rand(4)
        self.estado_prev = estado
        self.accion = np.argmax(self.Q[estado])
        return np.argmax(self.Q[estado])

    def actualizar(self, reward, estado):
        if (estado not in self.Q.keys()):
            self.Q[estado] = np.random.rand(4)
        self.Q[self.estado_prev][self.accion] += self.alpha * \
            (reward + self.gamma * np.max(self.Q[estado]) - self.Q[self.estado_prev][self.accion])
