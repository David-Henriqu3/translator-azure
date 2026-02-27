# Tradutor de Artigos Técnicos com AzureAI

Projeto criado para o DIO Bootcamp AI 102: "Tradutor de Artigos Técnicos com AzureAI".

Este repositório contém um pequeno utilitário em Python que extrai conteúdo de um seletor CSS em uma página web, traduz os trechos usando o serviço Azure Translator (Cognitive Services) e exporta o resultado em Markdown.

### Funcionalidades
- Extrai títulos, parágrafos, itens de lista e blockquotes de um seletor CSS.
- Tradução automática usando a API do Azure Translator.
- Exporta conteúdo traduzido em formato Markdown.

### Pré-requisitos
- Python 3.8+
- Conta/Chave do Azure Translator (Cognitive Services)

### Instalação
Recomenda-se criar um virtualenv e instalar dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Configuração
Crie um arquivo `.env` na raiz do projeto com as variáveis:

```
TRANSLATOR_KEY=seu_valor_aqui
TRANSLATOR_LOCATION=brazilsouth
# Opcional: TRANSLATOR_ENDPOINT se você usar um endpoint personalizado
```

Observação: o `.env` já está listado em `.gitignore` para evitar comitar chaves acidentalmente.

### Uso
Edite `main.py` para ajustar a `url` e o `seletor` do conteúdo que deseja traduzir. Em seguida, execute:

```powershell
python .\main.py
```

O script vai gerar um arquivo `conteudo_traduzido.md` com o conteúdo traduzido.

### Boas práticas / Produção
- Para produção, prefira usar um gerenciador de segredos (ex.: Azure Key Vault) em vez de `.env`.
- Não exponha a chave em commits públicos; se já tiver sido comitada, remova-a do histórico do Git.

### Contribuição
Issue, PRs e sugestões são bem-vindas — especialmente exemplos de seletores para sites técnicos.

### Autor
Projeto do DIO Bootcamp — Tradutor de Artigos Técnicos com AzureAI.
