import pandas as pd
data = {
    'Pregunta': [
        '¿Que es la fotosintesis?',
        '¿Cual es la ley de la gravitacion universal?',
        '¿Que es un ecosistema?',
        '¿Cual es la estructura basica de un atomo?',
        '¿Como se clasifican los seres vivos?'
    ],
    'Respuesta_Correcta': [
        'La fotosintesis es el proceso por el cual las plantas convierten la luz solar en energia quimica.',
        'La ley de la gravitacion universal es una ley fisica que describe la atraccion gravitatoria entre dos objetos.',
        'Un ecosistema es una comunidad de seres vivos y su entorno no vivo que interactuan entre si.',
        'Un atomo esta compuesto por protones, neutrones y electrones.',
        'Los seres vivos se clasifican en diferentes categorias como dominio, reino, filo, clase, orden, familia, genero y especie.'
    ],
    'areas_Conocimiento': [
        'Biologia, Botanica',
        'Fisica',
        'Ecologia, Biologia',
        'Quimica, Fisica',
        'Taxonomia, Biologia'
    ]
}

df = pd.DataFrame(data)

df.to_csv('cuestionario_ciencias_naturales.csv', index=False)

print("Archivo CSV guardado exitosamente.")
