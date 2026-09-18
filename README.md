# DevPy Canvas 🚀

O **DevPy Canvas** é um ecossistema corporativo Full Stack desenvolvido em **Python** e **FastAPI**. O projeto reúne, em uma única arquitetura modular e escalável, as três maiores vertentes exigidas pelo mercado de tecnologia atual: **Aplicações de Inteligência Artificial (SaaS)**, **Sistemas Transacionais (E-commerce)** e **Engenharia de Dados (Automação/Analytics)**.

---

## 🛠️ Arquitetura e Tecnologias Utilizadas

O projeto foi construído seguindo boas práticas de desenvolvimento, separação de conceitos (Módulos/Roteadores) e persistência de dados relacional.

| Camada | Tecnologias Principais | Descrição e Funcionalidade |
| :--- | :--- | :--- |
| **Back-End** | Python 3.10, FastAPI, SQLModel | Criação de APIs assíncronas de alta performance e rotas modulares. |
| **Front-End** | HTML5, CSS3, JavaScript (ES6+), Tailwind CSS | Interfaces responsivas, dinâmicas e consumo assíncrono de APIs. |
| **Banco de Dados**| SQLite (Local) / PostgreSQL | Mapeamento relacional de entidades (Usuários, Relatórios, Produtos, Pedidos, Mensagens). |
| **Segurança** | JWT (JSON Web Tokens), Bcrypt | Criptografia de senhas e proteção de rotas privadas via Middleware. |
| **IA & Documentos**| OpenAI API (GPT-4o-mini), ReportLab | Engenharia de prompts para geração de relatórios e exportação nativa de PDFs. |
| **DevOps** | Docker, Docker Compose | Conteinerização estruturada da aplicação para deploy simplificado em nuvem. |

---

## 📦 Projetos Integrados no Ecossistema

### 1. 🧠 SaaS de Produtividade com Inteligência Artificial
Uma plataforma de inteligência de negócios protegida por segurança máxima JWT.
* **Autenticação Segura:** Sistema de cadastro e login com senhas criptografadas via algoritmo *bcrypt* e geração de tokens JWT.
* **Motor de IA:** Endpoint integrado aos modelos LLM da OpenAI para processamento de dados de negócios brutos e geração de insights estratégicos.
* **Geração de Documentos:** Microsserviço que transforma o relatório da IA em um arquivo **PDF oficial e formatado** em tempo real para download do usuário.

### 2. 🛒 Marketplace Tech Shop (E-commerce Transacional)
Loja virtual completa com fluxo de compra ativo integrado ao banco de dados relacional.
* **Catálogo Dinâmico:** Produtos (Cursos e Mentorias) puxados diretamente do banco de dados e populados via *scripts de seed*.
* **Carrinho Ativo:** Manipulação de estado no Front-End para adição de itens e cálculo de valor total de forma reativa.
* **Checkout Simulado:** Rota transacional que valida a compra, abate o estoque e registra o histórico de pedidos vinculados ao ID do usuário.

### 3. 📊 Automated Scraper & Analytics (Engenharia de Dados)
Painel analítico alimentado por automação e coleta de dados de mercado.
* **Web Scraper:** Robô em Python que simula a raspagem de preços de hardware e tecnologia flutuantes em tempo real.
* **Dashboard Nativo:** Plotagem gráfica de métricas e comparativos de preços construída em HTML5 e CSS puros, livre de bloqueios de rede.

### 4. 💼 Página de Contato & CV Oficial
Módulo voltado para empregabilidade e atração de talentos.
* **Formulário de Mensagens:** Recebimento de propostas de contratação salvas diretamente na tabela do banco de dados.
* **Download de Currículo:** Geração dinâmica do currículo oficial do desenvolvedor no formato PDF padronizado de coluna única (otimizado para ATS/Robôs de triagem) contendo as certificações da EBAC.

---

## 🔧 Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Docker instalado (opcional, para rodar via container).

### Passo a Passo (Modo Tradicional)
1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd devpy-canvas
   ```
2. **Crie e ative o ambiente virtual (venv):**
   ```bash
   python -m venv venv
   # No Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   ```
3. **Instale as dependências atualizadas:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Inicie o servidor de desenvolvimento:**
   ```bash
   uvicorn backend.main:app --reload
   ```
5. **Acesse no seu navegador:**
   * Aplicação: `http://127.0.0.1:8000`
   * Documentação Swagger da API: `http://127.0.0`

---

## 🎓 Certificações Oficiais (EBAC)
* **Profissão: Desenvolvedor Full Stack Python** (77 módulos | 21 meses) — Código: *79274-40500-32013-36115*
* **Desenvolvedor Back-End Python** (40 módulos | 12 meses) — Código: *62429-40500-90129-22054*
* **Desenvolvedor Front-End** (37 módulos | 8 meses) — Código: *09969-40500-82267-45142*
* **TI do Zero ao Pro** (10 horas) — Código: *33266-40500-44611-22408*

---
Criado com orgulho por **Jonas Eduardo Fontela Machado** 🚀
