import pandas as pd
import numpy as np

# Exemplo de criação de um DataFrame
data = {
    'Nome': ['Carlos', 'Maria', 'Pedro', 'Ana', 'João', 'Luiza'],
    'deparmento': ['TI', 'RH', 'TI', 'Marketing', 'RH', 'Marketing'],
    'salario': [2000, 3000, 2500, 3500, 2800, 3200]
}

df = pd.DataFrame(data)

# Filtragem dos funcionarios de TI

funcionarios_ti = df[df['deparmento'] == 'TI']
print(funcionarios_ti)
# Media do salario dos funcionarios de TI
Media_salarial_ti = funcionarios_ti['salario'].mean()
print(f'Media salarial dos funcionarios de TI: {Media_salarial_ti}')