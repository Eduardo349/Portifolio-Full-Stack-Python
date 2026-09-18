from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# Tabela de Usuários (Mantida e Atualizada)
class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True, index=True)
    senha_criptografada: str
    criado_em: str = Field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Relacionamentos
    relatorios: List["Relatorio"] = Relationship(back_populates="usuario")
    pedidos: List["Pedido"] = Relationship(back_populates="usuario")

# Tabela de Relatórios de IA (Mantida)
class Relatorio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    dados_entrada: str
    insight_ia: str
    criado_em: str = Field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    
    usuario_id: int = Field(foreign_key="usuario.id")
    usuario: Usuario = Relationship(back_populates="relatorios")


# --- NOVAS TABELAS DO PROJETO 2: E-COMMERCE ---

# Tabela de Produtos do Catálogo
class Produto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    preco: float
    imagem_url: str  # Link para a foto do produto
    estoque: int

# Tabela de Pedidos/Carrinho Finalizado
class Pedido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: float
    status: str = Field(default="Pendente")  # Pendente, Pago, Cancelado
    criado_em: str = Field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    
    usuario_id: int = Field(foreign_key="usuario.id")
    usuario: Usuario = Relationship(back_populates="pedidos")

# --- NOVA TABELA DO PROJETO 3: WEB SCRAPER & METRICAS ---
class DadoColetado(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    categoria: str        # Ex: "Placa de Vídeo", "Vaga Python"
    nome_item: str        # Ex: "RTX 4060 Ti" ou "Dev Python Júnior"
    valor_identificado: float  # Preço ou salário encontrado
    fonte_origem: str     # Ex: "Kabum", "LinkedIn"
    coletado_em: str = Field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

