import random
import sys
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def fuzzing(vel, dis, flag = 0):
    # Fuzzificacao
    velocidade = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidade')
    distancia = ctrl.Antecedent(np.arange(0, 101, 1), 'distancia')
    pressao = ctrl.Consequent(np.arange(0, 101, 1), 'pressao')

    velocidade.automf(5)
    distancia.automf(5)

    # pressao['low'] = fuzz.trimf(pressao.universe, [0, 0, 50])
    # pressao['medium'] = fuzz.trimf(pressao.universe, [0, 50, 100])
    # pressao['high'] = fuzz.trimf(pressao.universe, [50, 100, 100])

    pressao['poor'] = fuzz.gaussmf(pressao.universe, 0, 10)
    pressao['mediocre'] = fuzz.gaussmf(pressao.universe, 25, 10)
    pressao['average'] = fuzz.gaussmf(pressao.universe, 50, 10)
    pressao['decent'] = fuzz.gaussmf(pressao.universe, 75, 10)
    pressao['good'] = fuzz.gaussmf(pressao.universe, 100, 10)

    # Regras
    regras = []

    regras.append(ctrl.Rule(velocidade['mediocre'] & distancia['average'], pressao['poor']))
    regras.append(ctrl.Rule(velocidade['mediocre'] & distancia['mediocre'], pressao['mediocre']))
    regras.append(ctrl.Rule(velocidade['mediocre'] & distancia['poor'], pressao['average']))
    regras.append(ctrl.Rule(velocidade['average']  & distancia['average'], pressao['average']))
    regras.append(ctrl.Rule(velocidade['average']  & distancia['mediocre'], pressao['decent']))
    regras.append(ctrl.Rule(velocidade['average']  & distancia['poor'], pressao['good']))
    regras.append(ctrl.Rule(velocidade['decent'] & distancia['good'], pressao['average']))
    regras.append(ctrl.Rule(velocidade['decent'] & distancia['decent'], pressao['decent']))

    regras.append(ctrl.Rule(velocidade['poor'], pressao['poor']))
    # regras.append(ctrl.Rule(velocidade['mediocre'] | distancia['good'], pressao['decent']))
    regras.append(ctrl.Rule(velocidade['good'], pressao['good']))

    pressao_ctrl = ctrl.ControlSystem(regras)
    pressao_sim = ctrl.ControlSystemSimulation(pressao_ctrl)

    pressao_sim.input['velocidade'] = vel
    pressao_sim.input['distancia'] = dis

    pressao_sim.compute()
    print(pressao_sim.output['pressao'])

    # distancia.view()
    # velocidade.view()
    pressao.view(sim=pressao_sim)
    plt.show()

if __name__ == '__main__':
    fuzzing(float(sys.argv[1]), float(sys.argv[2]))