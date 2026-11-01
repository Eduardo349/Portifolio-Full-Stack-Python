const API_URL = "/api";

async function carregarProjetos() {
    const gridProjetos = document.querySelector("#projetos .grid");
    
    if (!gridProjetos) return;

    try {
        const response = await fetch(`${API_URL}/projetos`);
        const projetos = await response.json();
        gridProjetos.innerHTML = "";

        // Card 1: SaaS de Produtividade com IA (Consumido dinamicamente do seu Backend Python)
        projetos.forEach(projeto => {
            gridProjetos.innerHTML += `
                <div class="glass-card rounded-2xl p-6 flex flex-col justify-between transition-all duration-300 hover:scale-[1.02] hover:border-amber-500/30 hover:shadow-xl hover:shadow-amber-500/5 group">
                    <div>
                        <div class="flex justify-between items-start mb-4">
                            <span class="text-[11px] font-bold tracking-wider uppercase px-2.5 py-1 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                                Disponível
                            </span>
                            <span class="text-xs font-mono text-slate-500 group-hover:text-slate-400 transition-colors">
                                💻 Full Stack
                            </span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-2 group-hover:text-amber-400 transition-colors">
                            ${projeto.titulo}
                        </h3>
                        <p class="text-sm text-slate-400 leading-relaxed mb-6">
                            ${projeto.descricao}
                        </p>
                    </div>
                    <div>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">FastAPI</span>
                            <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">SQLModel</span>
                            <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">PostgreSQL</span>
                            <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">OpenAI</span>
                        </div>
                        <a href="/login" class="block w-full text-center py-2.5 bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs rounded-xl tracking-wider uppercase transition-all shadow-md shadow-amber-500/10">
                            Acessar Sistema
                        </a>
                    </div>
                </div>
            `;
        });

        // Card 2: Marketplace E-commerce
        gridProjetos.innerHTML += `
            <div class="glass-card rounded-2xl p-6 flex flex-col justify-between transition-all duration-300 hover:scale-[1.02] hover:border-emerald-500/30 hover:shadow-xl hover:shadow-emerald-500/5 group">
                <div>
                    <div class="flex justify-between items-start mb-4">
                        <span class="text-[11px] font-bold tracking-wider uppercase px-2.5 py-1 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            Disponível
                        </span>
                        <span class="text-xs font-mono text-slate-500 group-hover:text-slate-400 transition-colors">
                            🛒 E-commerce
                        </span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2 group-hover:text-emerald-400 transition-colors">
                        Marketplace Tech Shop
                    </h3>
                    <p class="text-sm text-slate-400 leading-relaxed mb-6">
                        Loja virtual completa com catálogo dinâmico, gerenciamento de estoque integrado ao banco e simulação de checkout transacional.
                    </p>
                </div>
                <div>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">FastAPI</span>
                        <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">SQLModel</span>
                        <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">PostgreSQL</span>
                    </div>
                    <a href="/loja" class="block w-full text-center py-2.5 bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold text-xs rounded-xl tracking-wider uppercase transition-all shadow-md shadow-emerald-500/10">
                        Entrar na Loja
                    </a>
                </div>
            </div>
        `;

        // Card 3: Automated Scraper & Analytics Dashboard
        gridProjetos.innerHTML += `
            <div class="glass-card rounded-2xl p-6 flex flex-col justify-between transition-all duration-300 hover:scale-[1.02] hover:border-blue-500/30 hover:shadow-xl hover:shadow-blue-500/5 group">
                <div>
                    <div class="flex justify-between items-start mb-4">
                        <span class="text-[11px] font-bold tracking-wider uppercase px-2.5 py-1 rounded-md bg-blue-500/10 text-blue-400 border border-blue-500/20">
                            Disponível
                        </span>
                        <span class="text-xs font-mono text-slate-500 group-hover:text-slate-400 transition-colors">
                            📊 Analytics
                        </span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2 group-hover:text-blue-400 transition-colors">
                        Automated Scraper & Analytics
                    </h3>
                    <p class="text-sm text-slate-400 leading-relaxed mb-6">
                        Robô de automação que realiza raspagem de dados (Web Scraping) em tempo real, trata os registros e exibe métricas completas em um painel interativo.
                    </p>
                </div>
                <div>
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">FastAPI</span>
                        <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">Web Scraping</span>
                        <span class="text-[11px] font-mono font-medium px-2 py-0.5 rounded-md bg-slate-900 text-slate-300 border border-slate-800">Automation</span>
                    </div>
                    <a href="/analytics" class="block w-full text-center py-2.5 bg-blue-500 hover:bg-blue-600 text-white font-bold text-xs rounded-xl tracking-wider uppercase transition-all shadow-md shadow-blue-500/10">
                        Ver Analytics
                    </a>
                </div>
            </div>
        `;

    } catch (error) {
        console.error("Erro na aplicação:", error);
        gridProjetos.innerHTML = `<p class="text-red-400 text-center font-medium col-span-full py-8">Erro ao conectar com o backend.</p>`;
    }
}

document.addEventListener("DOMContentLoaded", carregarProjetos);



