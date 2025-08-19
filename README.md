# Esteganografia em Python

Um script simples em Python que permite ocultar e extrair mensagens de arquivos de imagem usando a técnica de esteganografia. O programa utiliza o bit menos significativo (LSB) dos pixels para armazenar dados de forma discreta.

### 🌟 Funcionalidades

* **Ocultar Mensagem:** Criptografa uma mensagem de texto dentro dos pixels de uma imagem de saída, criando um novo arquivo de imagem.
* **Extrair Mensagem:** Lê os dados ocultos de uma imagem para decodificar e exibir a mensagem original.
* **Interface de Linha de Comando:** Oferece um menu interativo e fácil de usar para codificar e decodificar mensagens.

### 💻 Tecnologias

* **Python:** Linguagem de programação principal.
* **Pillow (`PIL`):** Biblioteca para manipulação de imagens, utilizada para abrir, editar e salvar arquivos de imagem.
* **`os`:** Módulo do Python para interagir com o sistema operacional, usado para listar os arquivos de imagem na pasta.

### ⚙️ Pré-requisitos

Para executar o script, você precisa instalar a biblioteca `Pillow`. Abra seu terminal e execute o seguinte comando:

```bash
pip install Pillow
```

### 🛠️ Como Usar

Para colocar o projeto em funcionamento, siga estes passos:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Gugzz21/Esteganografia.git](https://github.com/Gugzz21/Esteganografia.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Esteganografia
    ```
3.  **Adicione sua imagem:**
    * Coloque a imagem (`.png`, `.jpg`, ou `.bmp`) que você deseja usar para ocultar a mensagem na mesma pasta do script.

4.  **Execute o script:**
    ```bash
    python seu_script.py
    ```
    *(O script irá apresentar um menu interativo. Siga as instruções para escolher uma opção e fornecer os dados necessários.)*

---

### ✍️ Autor

**Gugzz21** - [Link para o perfil do GitHub](https://github.com/Gugzz21)
