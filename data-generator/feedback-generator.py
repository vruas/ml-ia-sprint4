import pandas as pd
import random
from sklearn.model_selection import train_test_split  # pip install scikit-learn


# Listas de palavras e frases para gerar comentários
comentarios_positivos = [
    "Produto excelente, chegou antes do prazo!",
    "O atendimento foi ótimo, recomendo.",
    "Completamente satisfeito, voltarei a comprar.",
    "Gostei bastante, compraria novamente.",
    "Superou minhas expectativas!",
    "Excelente custo-benefício, recomendo!",
    "Muito feliz com a compra, recomendo!",
    "Produto excelente, recomendo sem dúvidas.",
    "Altamente recomendável, qualidade excepcional.",
    "Ótimo acabamento e qualidade.",
]

comentarios_neutros = [
    "Bom custo-benefício.",
    "Demorou para chegar, mas é bom.",
    "Recebi o que foi prometido, nada além disso.",
    "Entrega rápida, mas o produto é mediano.",
    "O produto é razoável, cumpre o que promete.",
    "Preço justo para a qualidade.",
    "Atendeu bem ao propósito.",
    "Produto funcional, atende bem.",
    "Produto veio como descrito, qualidade ok.",
    "Recebi o que foi anunciado, sem surpresas.",
]

comentarios_negativos = [
    "A qualidade é muito ruim, não recomendo.",
    "Produto chegou com defeito, muito frustrado.",
    "Muito ruim, devolvi o produto.",
    "Serviço péssimo, atendimento horrível.",
    "Esperava mais, não correspondeu às expectativas.",
    "Produto de baixa qualidade, não recomendo.",
    "Completamente insatisfeito, não volto a comprar.",
    "Produto danificado, atendimento ruim.",
    "Não valeu o preço pago.",
    "Entrega muito lenta.",
]

# Função para gerar dados aleatórios
def gerar_dados_aleatorios(num_dados):
    dados = []
    for _ in range(num_dados):
        sentimento = random.choice(["Positivo", "Neutro", "Negativo"])
        if sentimento == "Positivo":
            comentario = random.choice(comentarios_positivos)
            avaliacao = random.randint(4, 5)  # Avaliação alta
        elif sentimento == "Neutro":
            comentario = random.choice(comentarios_neutros)
            avaliacao = 3  # Avaliação média
        else:
            comentario = random.choice(comentarios_negativos)
            avaliacao = random.randint(1, 2)  # Avaliação baixa
        dados.append((comentario, avaliacao, sentimento))
    return dados

# Gerar 100 dados aleatórios
num_dados = 100
dados_aleatorios = gerar_dados_aleatorios(num_dados)

# Criar DataFrame a partir dos dados gerados
df = pd.DataFrame(dados_aleatorios, columns=["Comentario", "Avaliacao", "Sentimento"])

# Dividir em 80% para treino e 20% para teste
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Salvar em arquivos CSV
train_df.to_csv("feeling-train.csv", index=False)
test_df.to_csv("feeling-test.csv", index=False)

print("Arquivos train_data.csv e test_data.csv foram gerados com sucesso!")
