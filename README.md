# Projeto: Roteiro de Viagem Automatizado com OpenAI

## Descrição

Este projeto utiliza a API da OpenAI para gerar um roteiro de viagem personalizado. Ele integra ferramentas de busca e consultas em tempo real para criar um itinerário detalhado, incluindo eventos locais e preços de passagens aéreas. Através de uma combinação de agentes e modelos de linguagem avançados, o projeto oferece uma experiência rica e informativa para planejamentos de viagem.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **OpenAI API**: Para gerar respostas inteligentes e personalizadas.
- **LangChain**: Framework para criar e gerenciar agentes baseados em modelos de linguagem.
- **Dotenv**: Para carregar variáveis de ambiente de forma segura.
- **Ferramentas de Busca**: Integração com DuckDuckGo e Wikipedia para consultas em tempo real.

## Configuração do Ambiente

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie um ambiente virtual e ative-o:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Execução do Projeto

1. **Carregar as variáveis de ambiente:**
    ```python
    from dotenv import load_dotenv
    load_dotenv()
    ```

2. **Inicializar o agente e ferramentas:**
    ```python
    from langchain_openai import ChatOpenAI
    from langchain.agents import initialize_agent
    from langchain_community.agent_toolkits.load_tools import load_tools
    import os

    open_api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=open_api_key)
    tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    ```

3. **Executar a consulta de roteiro de viagem:**
    ```python
    query = """
    Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com os eventos que irão ocorrer na data da viagem e com o preço da passagem de São Paulo para Londres.
    """
    agent.run(query)
    ```

4. **Exibir a resposta gerada pela API:**
    ```python
    import openai
    import os

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim."}
        ]
    )

    print(response.choices[0].message['content'].strip())
    ```

## Exemplo de Saída

O agente fornecerá um roteiro detalhado, incluindo eventos locais em Londres durante o período da viagem, bem como o preço estimado da passagem aérea de São Paulo para Londres.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Para isso, siga os passos abaixo:

1. **Fork o projeto**
2. **Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)**
3. **Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)**
4. **Faça o push para a branch (`git push origin feature/nova-feature`)**
5. **Abra um Pull Request**

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.
