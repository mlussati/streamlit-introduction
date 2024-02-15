1. **Instalação**:
    - Primeiramente, você precisa instalar o Streamlit. Você pode fazer isso executando o seguinte comando no seu terminal ou prompt de comando:
      ```
      pip install streamlit
      ```
    - Este comando instala o Streamlit, que é uma biblioteca Python para criar aplicativos web interativos a partir de scripts de dados.

2. **Criando um Aplicativo Streamlit**:
    - Em seguida, crie um arquivo Python (vamos chamá-lo de `ola_mundo.py`).
    - Dentro de `ola_mundo.py`, você escreverá seu aplicativo Streamlit.

3. **Fundamentos do Streamlit**:
    - O código que você forneceu é um exemplo de um aplicativo Streamlit simples.
    - Vamos revisar cada parte:

    ```python
    import streamlit as st

    st.title("Olá Mundo")
    ```
    - `st.title("Olá Mundo")`: Esta linha define o título do seu aplicativo para "Olá Mundo". Quando você executar seu aplicativo Streamlit, verá este título sendo exibido.

    ```python
    st.write("Este é o Palanca Code")
    ```
    - `st.write("Este é o Palanca code")`: Esta linha exibe o texto "Este é o Manilson" no seu aplicativo. Você pode usar `st.write()` para mostrar qualquer texto ou dados.

    ```python
    st.markdown("# Conteúdo Markdown")
    ```
    - `st.markdown("# Conteúdo Markdown")`: Esta linha renderiza um cabeçalho Markdown (nível 1) com o texto "Conteúdo Markdown". Você pode usar `st.markdown()` para exibir texto formatado usando a sintaxe Markdown.

    ```python
    st.code("""
        if legal == "bom":
            print("Aceito")
        """)
    ```
    - `st.code("""
        if legal == "bom":
            print("Aceito")
        """)`: Esta linha exibe código em um bloco de código. O trecho de código verifica se a variável `post` é igual a "bom" e imprime "Curtir" se a condição for verdadeira.
    - Note que `post` não está definido no trecho de código fornecido, então você precisaria defini-lo em outro lugar no seu aplicativo.

4. **Executando o Aplicativo**:
    - Após criar `hello.py`, execute-o usando o seguinte comando:
      ```
      streamlit run hello.py
      ```
    - Este comando inicia um servidor web local e abre seu aplicativo em um navegador da web em `http://localhost:8501/`.

5. **Interagindo com Seu Aplicativo**:
    - Ao visitar a URL local, você verá seu aplicativo Streamlit com o título, texto, markdown e trecho de código sendo exibidos.
    - Você pode modificar o código em `hello.py` e ver as alterações refletidas em tempo real conforme você salva o arquivo.

O Streamlit facilita a criação de aplicativos web interativos diretamente do seu código Python, sem a necessidade de escrever HTML, CSS ou JavaScript. É uma ótima ferramenta para projetos de ciência de dados e aprendizado de máquina,
atualmente foi incluído a parte de LLM (GenAI).
