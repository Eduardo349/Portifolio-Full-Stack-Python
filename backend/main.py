from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from .database import criar_banco_e_tabelas, get_session
from .models import Usuario
from .auth import criptografar_senha, verificar_senha, criar_token_acesso
from .routes_ia import router as router_ia  # 1. Importa a nova rota de IA
from .routes_loja import router as router_loja # 2. Importa a nova rota da loja
from .routes_scraper import router as router_scraper  # 3. Importa a nova rota do scraper
from .routes_contato import router as router_contato  # 4. Importa o módulo de contato
import os

app = FastAPI(title="DevPy Canvas API")


app.include_router(router_ia)# 5. Registra as rotas de IA no servidor do FastAPI
app.include_router(router_loja)  # 6. Registra a loja no servidor
app.include_router(router_scraper)  # 7. Registra o scraper no servidor
app.include_router(router_contato)  # 8. Registra o contato no servidor

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    criar_banco_e_tabelas()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")

# --- ROTAS DE AUTENTICAÇÃO ---

@app.post("/api/auth/cadastro", status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: Usuario, db: Session = Depends(get_session)):
    # Verifica se o e-mail já está cadastrado no banco
    usuario_existente = db.exec(select(Usuario).where(Usuario.email == usuario.email)).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado no sistema.")
    
    # Criptografa a senha antes de salvar por segurança
    usuario.senha_criptografada = criptografar_senha(usuario.senha_criptografada)
    
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"mensagem": "Usuário criado com sucesso!", "usuario_id": usuario.id}

@app.post("/api/auth/login")
def login_usuario(usuario_dados: dict, db: Session = Depends(get_session)):
    email = usuario_dados.get("email")
    senha = usuario_dados.get("senha")
    
    # Busca o usuário no banco
    usuario = db.exec(select(Usuario).where(Usuario.email == email)).first()
    if not usuario or not verificar_senha(senha, usuario.senha_criptografada):
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos.")
    
    # Gera o token de acesso (crachá) do usuário válido por 60 minutos
    token = criar_token_acesso(data={"sub": usuario.email, "usuario_id": usuario.id})
    return {"access_token": token, "token_type": "bearer", "nome": usuario.nome}

# -----------------------------

@app.get("/", response_class=HTMLResponse)
def ler_index():
    with open(os.path.join(FRONTEND_DIR, "index.html"), "r", encoding="utf-8") as file:
        return file.read()

# -------------------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def ler_dashboard():
    with open(os.path.join(FRONTEND_DIR, "dashboard.html"), "r", encoding="utf-8") as file:
        return file.read()
# --------------------------------------

# --- ROTA DO LOGIN AQUI ---
@app.get("/login", response_class=HTMLResponse)
def ler_login():
    with open(os.path.join(FRONTEND_DIR, "login.html"), "r", encoding="utf-8") as file:
        return file.read()
# --------------------------------------

# --- ROTA DA LOJA AQUI ---
@app.get("/loja", response_class=HTMLResponse)
def ler_loja():
    with open(os.path.join(FRONTEND_DIR, "loja.html"), "r", encoding="utf-8") as file:
        return file.read()
# --------------------------------------

# --- ROTA DO WEB SCRAPER & METRICAS AQUI ---
@app.get("/analytics", response_class=HTMLResponse)
def ler_analytics():
    with open(os.path.join(FRONTEND_DIR, "analytics.html"), "r", encoding="utf-8") as file:
        return file.read()
# -------------------------------------------------

# --- ROTA HTML DO CONTATO ---
@app.get("/contato", response_class=HTMLResponse)
def ler_contato():
    with open(os.path.join(FRONTEND_DIR, "contato.html"), "r", encoding="utf-8") as file:
        return file.read()

# ---------------------------------------------


@app.get("/api/projetos")
def listar_projetos():
    return [
        {
            "id": 1,
            "titulo": "SaaS de Produtividade com IA",
            "descricao": "Aplicação web que consome modelos LLMs para automatizar fluxos de trabalho e gerar relatórios corporativos inteligentes.",
            "tags": ["FastAPI", "SQLModel", "PostgreSQL", "OpenAI"],
            "status": "Disponível"  # Mudei para Disponível para liberar o clique!
        }
    ]

