from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from .database import get_session
from .models import Produto, Pedido
from typing import List

router = APIRouter(prefix="/api/loja", tags=["E-commerce / Loja"])

# 1. Rota para Listar todos os produtos do catálogo
@router.get("/produtos", response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_session)):
    produtos = db.exec(select(Produto)).all()
    return list(produtos)

# 2. Rota para Popular o banco com alguns produtos de teste (executada uma vez)
@router.post("/seed", status_code=status.HTTP_201_CREATED)
def criar_produtos_teste(db: Session = Depends(get_session)):
    # Verifica se já existem produtos para não duplicar
    existe = db.exec(select(Produto)).first()
    if existe:
        return {"mensagem": "O catálogo já possui produtos."}
        
    produtos_teste = [
        Produto(nome="Curso Python Pro", descricao="Do zero ao primeiro emprego como desenvolvedor Python Full Stack.", preco=199.90, imagem_url="https://unsplash.com", estoque=100),
        Produto(nome="Mentoria Tech Co.", descricao="Acompanhamento individual para alavancar sua carreira de dev.", preco=450.00, imagem_url="https://unsplash.com", estoque=10),
        Produto(nome="E-book FastAPI Masters", descricao="Aprenda a criar APIs robustas e escaláveis com padrão de mercado.", preco=49.90, imagem_url="https://unsplash.com", estoque=50)
    ]
    
    for prod in produtos_teste:
        db.add(prod)
    db.commit()
    return {"mensagem": "Catálogo de teste criado com sucesso!"}

# 3. Rota para Simular o Checkout/Finalização de Compra
@router.post("/checkout")
def finalizar_compra(dados: dict, db: Session = Depends(get_session)):
    usuario_id = dados.get("usuario_id")
    total = dados.get("total")
    
    if not usuario_id or not total:
        raise HTTPException(status_code=400, detail="Informações de checkout inválidas.")
        
    # Salva o pedido feito no banco de dados relacional
    novo_pedido = Pedido(total=float(total), usuario_id=int(usuario_id), status="Pago")
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    
    return {
        "mensagem": "Pagamento aprovado e pedido finalizado com sucesso!",
        "pedido_id": novo_pedido.id,
        "status": novo_pedido.status
    }

# 4. Nova rota: Listar pedidos de um usuário específico
@router.get("/pedidos/{usuario_id}", response_model=List[Pedido])
def listar_pedidos_usuario(usuario_id: int, db: Session = Depends(get_session)):
    # Busca todas as compras correspondentes ao ID fornecido, ordenando pelas mais recentes
    pedidos = db.exec(select(Pedido).where(Pedido.usuario_id == usuario_id).order_by(Pedido.criado_em.desc())).all()
    return list(pedidos)
