from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from .database import criar_banco_e_tabelas, get_session
from .models import Usuario, Produto  # Importamos o modelo Produto aqui
from .auth import criptografar_senha, verificar_senha, criar_token_acesso
from .routes_ia import router as router_ia  
from .routes_loja import router as router_loja 
from .routes_scraper import router as router_scraper  
from .routes_contato import router as router_contato  
import os

app = FastAPI(title="DevPy Canvas API")

# Registra os roteadores acoplados do sistema
app.include_router(router_ia)
app.include_router(router_loja)  
app.include_router(router_scraper)  
app.include_router(router_contato)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- INICIALIZAÇÃO E SEED AUTOMÁTICO ---
# --- SUBISTITUA O BLOCO ON_STARTUP POR ESTE NO SEU MAIN.PY ---
@app.on_event("startup")
def on_startup():
    # 1. Executa a criação das tabelas do banco de dados
    criar_banco_e_tabelas()
    
    # 2. Abre a sessão e roda o seed profissional com os campos exatos
    db: Session = next(get_session())
    try:
        # Busca se já existe algum produto cadastrado usando o modelo correto
        produto_existente = db.exec(select(Produto)).first()
        
        if not produto_existente:
            print("[SEED AUTOMÁTICO] Catálogo vazio detectado. Injetando dados compatíveis...")
            
            # Criamos os objetos usando EXATAMENTE as colunas que a sua rota /seed usa
            produtos_teste = [
                Produto(
                    nome="Curso Python Pro", 
                    descricao="Do zero ao primeiro emprego como desenvolvedor Python Full Stack.", 
                    preco=199.90, 
                    imagem_url="https://unsplash.com", 
                    estoque=100
                ),
                Produto(
                    nome="Mentoria Tech Co.", 
                    descricao="Acompanhamento individual para alavancar sua carreira de dev.", 
                    preco=450.00, 
                    imagem_url="https://unsplash.com", 
                    estoque=10
                ),
                Produto(
                    nome="E-book FastAPI Masters", 
                    descricao="Aprenda a criar APIs robustas e escaláveis com padrão de mercado.", 
                    preco=49.90, 
                    imagem_url="https://unsplash.com", 
                    estoque=50
                )
            ]
            
            # Adiciona a lista completa de uma só vez
            db.add_all(produtos_teste)
            db.commit()
            print("[SEED AUTOMÁTICO] Produtos gravados com sucesso no banco relacional!")
        else:
            print("[SEED AUTOMÁTICO] O catálogo já possui produtos cadastrados. Pulando.")
    except Exception as e:
        print(f"[SEED ERRO] Falha crítica na gravação do banco: {e}")
        db.rollback()
    finally:
        db.close()


# --- DIRETÓRIOS E COMPONENTES ESTÁTICOS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")
app.mount("/img", StaticFiles(directory=os.path.join(FRONTEND_DIR, "img")), name="img")

# --- ROTAS DE AUTENTICAÇÃO ---

@app.post("/api/auth/cadastro", status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: Usuario, db: Session = Depends(get_session)):
    usuario_existente = db.exec(select(Usuario).where(Usuario.email == usuario.email)).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado no sistema.")
    
    usuario.senha_criptografada = criptografar_senha(usuario.senha_criptografada)
    
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"mensagem": "Usuário criado com sucesso!", "usuario_id": usuario.id}

@app.post("/api/auth/login")
def login_usuario(usuario_dados: dict, db: Session = Depends(get_session)):
    email = usuario_dados.get("email")
    senha = usuario_dados.get("senha")
    
    usuario = db.exec(select(Usuario).where(Usuario.email == email)).first()
    if not usuario or not verificar_senha(senha, usuario.senha_criptografada):
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos.")
    
    token = criar_token_acesso(data={"sub": usuario.email, "usuario_id": usuario.id})
    return {"access_token": token, "token_type": "bearer", "nome": usuario.nome}

# --- ROTAS DE RENDERIZAÇÃO DE PÁGINAS HTML ---

@app.get("/", response_class=HTMLResponse)
def ler_index():
    with open(os.path.join(FRONTEND_DIR, "index.html"), "r", encoding="utf-8") as file:
        return file.read()

@app.get("/dashboard", response_class=HTMLResponse)
def ler_dashboard():
    with open(os.path.join(FRONTEND_DIR, "dashboard.html"), "r", encoding="utf-8") as file:
        return file.read()

@app.get("/login", response_class=HTMLResponse)
def ler_login():
    with open(os.path.join(FRONTEND_DIR, "login.html"), "r", encoding="utf-8") as file:
        return file.read()

@app.get("/loja", response_class=HTMLResponse)
def ler_loja():
    with open(os.path.join(FRONTEND_DIR, "loja.html"), "r", encoding="utf-8") as file:
        return file.read()

@app.get("/analytics", response_class=HTMLResponse)
def ler_analytics():
    with open(os.path.join(FRONTEND_DIR, "analytics.html"), "r", encoding="utf-8") as file:
        return file.read()

@app.get("/contato", response_class=HTMLResponse)
def ler_contato():
    with open(os.path.join(FRONTEND_DIR, "contato.html"), "r", encoding="utf-8") as file:
        return file.read()

# --- API DE PROJETOS ---
@app.get("/api/projetos")
def listar_projetos():
    return [
        {
            "id": 1,
            "titulo": "SaaS de Produtividade com IA",
            "descricao": "Aplicação web que consome modelos LLMs para automatizar fluxos de trabalho e gerar relatórios corporativos inteligentes.",
            "tags": ["FastAPI", "SQLModel", "PostgreSQL", "OpenAI"],
            "status": "Disponível"
        }
    ]
