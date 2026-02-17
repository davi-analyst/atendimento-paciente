import csv

patient_calls = 0
calls_per_day = {}
key_words = ['agendamento', 'exame', 'convênio']
# Cria o dicionário de contagem 
words_count = {word: 0 for word in key_words} 

# Abertura e processamento do arquivo
with open(r'C:\Users\eletr\Documents\T.I Estudos\Programinhas e Exercícios\lista-atendimento-paciente', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',', skipinitialspace=True)
    
    for line in reader:
        if not line:
            continue
            
        date_atend = line[0]
        subject = line[2].lower() 
        patient_calls += 1
        calls_per_day[date_atend] = calls_per_day.get(date_atend, 0) + 1
        
        for word in key_words:
            if word in subject:
                words_count[word] += 1

# Exibição dos Resultados
print(f"{'--- Relatório de Atendimento ---':^40}")
print(f"Total de Ligações: {patient_calls}")

print(f"\nLigações por Dia: ")
# Ordenação por data 
for day in sorted(calls_per_day.keys()):
    print(f"  {day}: {calls_per_day[day]} ligações")

print(f"\nPalavras-chave: ")
for word, count in words_count.items():

    print(f"  {word.capitalize()}: {count}")
