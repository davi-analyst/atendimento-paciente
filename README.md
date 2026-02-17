📊 Analisador de Atendimentos (CSV)
Este script em Python automatiza a leitura e análise de logs de atendimento de pacientes, transformando dados brutos de um arquivo CSV em um relatório organizado.

# O que ele faz?
O sistema processa um arquivo de registros e gera três estatísticas principais:

Contagem Geral: Calcula o volume total de ligações processadas.

Frequência Diária: Agrupa e ordena quantas ligações ocorreram em cada data específica.

Análise de Assunto: Identifica a recorrência de palavras-chave estratégicas (agendamento, exame, convênio) para entender a demanda da clínica.

# Como usar
Certifique-se de que o arquivo CSV está no caminho especificado:
C:\Users\onde-você-colocou-o-arquivo-"lista-de-atendimento.csv"

O arquivo deve seguir o formato: Data, Paciente, Assunto (separados por vírgula).

Execute o script:

Bash
python atendimento-paciente.py

#. Aprendizados Técnicos (Lógica de Programação)
Manipulação de Arquivos (I/O): Uso do with open para leitura segura de arquivos externos.

Biblioteca csv: Tratamento de delimitadores e espaços em branco estruturados.

Dicionários Dinâmicos: Uso do método .get() para criar contadores de dias de forma eficiente (sem erros de chave inexistente).

Análise de Strings: Normalização de texto com .lower() e busca de padrões com if word in subject.

Formatação de Saída: Uso de f-strings com alinhamento (^40) para criar um relatório visualmente limpo no terminal.
