# 🌟 AUTOMATIZAÇÃO DE LINKEDIN COM PYTHON E SELENIUM

** Este projeto é um bot que automatiza conexões e interações no LinkedIn, facilitando a construção de um network profissionais. O objetivo é automatizar tarefas repetitivas, como percorrer listas de perfis filtrados e interagir com estes perfis, como visualizar perfis e enviar solicitações de conexão com mensagens personalizadas.

## Objetivos do Projeto 🎯

- 🤖 Automatizar visualizações de perfis e o envio de convites de conexão com mensagens personalizadas.
- - 📈 Aumentar o número de conexões relevantes no LinkedIn, focando em recrutadores e profissionais da área de tecnologia.
- 🚀 Maximizar a eficiência e personalização da interação no LinkedIn.
- 🛠️ Simular havegação humana com o uso de intervalos aleatórios e manipulação inteligente de abas para evitar bloqueios de conta.
- 🛠️ Modularidade do código para facilitar futuras manutenções e evoluções.

## Tecnologias Utilizadas 🖥 

- **Python**: Linguagem de programação da arquitetura do projeto.
- **Selenium WebDriver**: Automação da interação com o navegador.
- **Web Scraping**: Extração e interação de dados de páginas da web.
- **Anaconda (Jupyter Notebook)**: Ambiente de desenvolvimento modular e gerenciamento de dependências.
- **Chrome/Firefox WebDriver**: Controle dos navegadores Chrome e Firefox.

## Arquitetura do Código 🏛️

A aplicação segue uma abordagem modular, dividida em funções específicas para realizar ações distintas, como fechar abas, acessar perfis, enviar convites e gerenciar o fluxo da interação. 

A modularidade foi fundamental para garantir a manutenção e escalabilidade do código, possibilitando o isolamento de funcionalidades e a reutilização de código. A divisão de responsabilidade é clara, com cada função focada em uma única tarefa.

**Destaques Arquitetônicos**:
- **Fechar Abas**: Gerencia todas as abas abertas durante a execução, garantindo que o foco permaneça na aba ativa correta.
- **Acessar Perfil**: Automatiza a navegação pelos perfis de usuários do LinkedIn.
- **Enviar Conexões**: Envia convites de conexão personalizados e controla o fluxo de mensagens.

Essa separação é importante para facilitar a manutenção e possibilitar melhorias futuras com baixo acoplamento entre as funcionalidades.

## Conceitos Avançados Utilizados ⚙️

### Controle de Fluxo Avançado
- **Uso de Randomização**: A aplicação utiliza a biblioteca `random` para variar os tempos de espera e simular interações humanas, evitando que o LinkedIn detecte o comportamento como automatizado.
  
### Networking Diferenciado
- **Multi-threading (futuro)**: Planeja-se a implementação de multi-threading para lidar com múltiplas janelas de perfis simultaneamente, melhorando o desempenho e a eficiência da automação.
  
- **Gerenciamento de Sessões**: A aplicação gerencia múltiplas sessões e guias abertas, mantendo o controle sobre a janela correta para evitar inconsistências durante a navegação.

- **Manuseio Dinâmico de Páginas**: A utilização do Selenium permite que a aplicação se adapte ao conteúdo dinâmico carregado pelo LinkedIn, como janelas modais e elementos interativos.

## Como Executar o Projeto 🚀

### Pré-requisitos

- 🐍 **Python 3.8+**
- 🌐 **Anaconda**
- 🌐 **Google Chrome** ou **Firefox**
- 🕸 **WebDriver** compatível com a versão do navegador

### Passos

1. 📂 Clone este repositório:
   ```
   git clone https://github.com/leonardobarral/linkedin-automation.git
   </código>
   ```

2. 📦 Crie um ambiente virtual no Anaconda:
   ```
   conda create -n linkedin-automation python=3.8
   ```
   ```
   conda activate linkedin-automation
   ```

3. 🛠️ Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

4. 🌐 Baixe e configure o WebDriver:
   - Verifique a versão do navegador em:
     <chrome://settings/help> ou <about:firefox>
   - Baixe o WebDriver compatível:
     <https://chromedriver.chromium.org/downloads> ou <https://github.com/mozilla/geckodriver/releases>
   - Coloque o WebDriver na pasta do Anaconda:
     <C:\Users\user\Anaconda3>
   
5. ▶️ Execute a automação:
   ```
   python main.py
   ```

6. 🌐 A automação será executada no LinkedIn e enviará convites conforme configurado.

## 📋 Observações

- Certifique-se de que a versão do navegador e do WebDriver sejam compatíveis.
- Verifique as credenciais de login no arquivo de configuração antes de executar a automação.

## 🔜 Próximos Passos

- ✨ Implementar o envio de mensagens de follow-up.
- 🛠️ Incluir suporte a multi-threading para maximizar a eficiência.
- ☁️ Integrar com serviços de cloud para armazenamento de logs e análise de desempenho.

## Muito obrigado por esta visita! 😊
