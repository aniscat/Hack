import pandas as pd
from transformers import BertTokenizer, BertModel
import torch
import torch.nn as nn
import torch.optim as optim

data = {
    'Pregunta': [
        '¿Que es la fotosintesis?',
        '¿Cua}l es la ley de la gravitaciaon universal?',
        '¿Que es un ecosistema?',
        '¿Cua}l es la estructura ba}sica de un a}tomo?',
        '¿Como se clasifican los seres vivos?'
    ],
    'Respuesta_Correcta': [
        'La fotosintesis es el proceso por el cual las plantas convierten la luz solar en energia quimica.',
        'La ley de la gravitacion universal es una ley fisica que describe la atraccion gravitatoria entre dos objetos.',
        'Un ecosistema es una comunidad de seres vivos y su entorno no vivo que interactúan entre si.',
        'Un a}tomo esta} compuesto por protones, neutrones y electrones.',
        'Los seres vivos se clasifican en diferentes categorias como dominio, reino, filo, clase, orden, familia, genero y especie.'
    ],
    'areas_Conocimiento': [
        'Biologia, Bota}nica',
        'Fisica',
        'Ecologia, Biologia',
        'Quimica, Fisica',
        'Taxonomia, Biologia'
    ]
}

df = pd.DataFrame(data)
df.to_csv('cuestionario_ciencias_naturales.csv', index=False)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def tokenize_and_encode(data):
    return tokenizer(data, padding=True, truncation=True, return_tensors='pt')

df = pd.read_csv('cuestionario_ciencias_naturales.csv')
questions_encoded = tokenize_and_encode(df['Pregunta'].tolist())
answers_encoded = tokenize_and_encode(df['Respuesta_Correcta'].tolist())

class BertClassifier(nn.Module):
    def __init__(self, bert_model_name='bert-base-uncased', num_classes=1):
        super(BertClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(bert_model_name)
        self.fc = nn.Linear(self.bert.config.hidden_size, num_classes)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs[1]
        out = self.fc(cls_output)
        return out

model = BertClassifier()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-5)

def train(model, questions_encoded, answers_encoded, criterion, optimizer, epochs=3):
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(questions_encoded['input_ids'], questions_encoded['attention_mask'])
        loss = criterion(outputs, answers_encoded['input_ids'].float())
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

train(model, questions_encoded, answers_encoded, criterion, optimizer)

def evaluate_and_recommend(model, tokenizer, question, user_answer, correct_answer, areas_conocimiento):
    model.eval()
    inputs = tokenizer(question, return_tensors='pt', padding=True, truncation=True)
    user_inputs = tokenizer(user_answer, return_tensors='pt', padding=True, truncation=True)
    correct_inputs = tokenizer(correct_answer, return_tensors='pt', padding=True, truncation=True)
    
    with torch.no_grad():
        output = model(inputs['input_ids'], inputs['attention_mask'])
        user_output = model(user_inputs['input_ids'], user_inputs['attention_mask'])
        correct_output = model(correct_inputs['input_ids'], correct_inputs['attention_mask'])
    
    user_score = torch.nn.functional.cosine_similarity(user_output, correct_output).item()
    
    if user_score < 0.8:
        recommendation = f"a}reas para mejorar: {areas_conocimiento}"
    else:
        recommendation = "¡Buen trabajo! Sigue asi."

    return user_score, recommendation

question = df['Pregunta'].iloc[0]
correct_answer = df['Respuesta_Correcta'].iloc[0]
user_answer = "Es el proceso en el cual las plantas usan la luz del sol para producir energia."

score, recommendation = evaluate_and_recommend(model, tokenizer, question, user_answer, correct_answer, df['a}reas_Conocimiento'].iloc[0])
print(f"Score: {score}, Recommendation: {recommendation}")
