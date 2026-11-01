/**
 * Tailwind CSS v3.4.15 - Versão de Desenvolvimento Local
 * Configuração estendida para o ecossistema DevPy Canvas
 */

(function () {
    'use strict';

    // 1. Injeta os estilos estruturais de base do Tailwind no documento
    const styleElement = document.createElement('style');
    styleElement.id = 'tailwind-local-engine';
    document.head.appendChild(styleElement);

    // 2. Banco de estilos mapeados a partir das classes do seu layout
    const tailwindRegistry = {
        // Estrutura Globais e Elementos de Fundo
        'bg-[#0b0f19]': 'body, html { background-color: #0b0f19 !important; color: #f1f5f9 !important; }',
        'scroll-smooth': 'html { scroll-behavior: smooth !important; }',
        'antialiased': 'body { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }',
        
        // Componentes Customizados (Glassmorphism e Glows)
        'glass-nav': '.glass-nav { background: rgba(10, 15, 30, 0.7) !important; backdrop-filter: blur(12px) !important; -webkit-backdrop-filter: blur(12px) !important; border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important; }',
        'glass-card': '.glass-card { background: rgba(30, 41, 59, 0.45) !important; backdrop-filter: blur(8px) !important; -webkit-backdrop-filter: blur(8px) !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; }',
        
        // Layouts, Grids e Alinhamentos
        'grid': '.grid { display: grid !important; }',
        'grid-cols-1': '.grid { grid-template-columns: repeat(1, minmax(0, 1fr)) !important; }',
        'md:grid-cols-2': '@media (min-width: 768px) { .grid { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; } }',
        'lg:grid-cols-3': '@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; } }',
        'gap-8': '.grid { gap: 2rem !important; }',
        'flex': '.flex { display: flex !important; }',
        'flex-col': '.flex-col { flex-direction: column !important; }',
        'justify-between': '.justify-between { justify-content: space-between !important; }',
        'items-center': '.items-center { align-items: center !important; }',
        
        // Fontes e Tipografia
        'text-white': '.text-white { color: #ffffff !important; }',
        'text-amber-500': '.text-amber-500 { color: #f59e0b !important; }',
        'text-amber-400': '.text-amber-400 { color: #fbbf24 !important; }',
        'text-emerald-400': '.text-emerald-400 { color: #34d399 !important; }',
        'text-blue-400': '.text-blue-400 { color: #60a5fa !important; }',
        'text-slate-400': '.text-slate-400 { color: #94a3b8 !important; }',
        'text-slate-500': '.text-slate-500 { color: #64748b !important; }',
        
        // Backgrounds e Botões
        'bg-amber-500': '.bg-amber-500 { background-color: #f59e0b !important; color: #0f172a !important; }',
        'bg-emerald-500': '.bg-emerald-500 { background-color: #10b981 !important; color: #ffffff !important; }',
        'bg-blue-500': '.bg-blue-500 { background-color: #3b82f6 !important; color: #ffffff !important; }',
        'bg-slate-900': '.bg-slate-900 { background-color: #0f172a !important; border: 1px solid #1e293b !important; }',
        'bg-[#0e1422]': 'input, textarea { background-color: #0e1422 !important; border: 1px solid #1e293b !important; }',
        
        // Bordas e Espaçamentos
        'rounded-xl': '.rounded-xl { border-radius: 0.75rem !important; }',
        'rounded-2xl': '.rounded-2xl { border-radius: 1rem !important; }',
        'p-6': '.p-6, padding { padding: 1.5rem !important; }',
        'mb-4': '.mb-4 { margin-bottom: 1rem !important; }',
        'mb-6': '.mb-6 { margin-bottom: 1.5rem !important; }',
        'w-full': '.w-full { width: 100% !important; }',
        'block': '.block { display: block !important; }'
    };

    // 3. Processador de mutações do DOM (Compila as classes injetadas via JavaScript no app.js)
    function processElementClasses(element) {
        if (!element || !element.classList) return;

        let accumulatedStyles = '';
        const classList = Array.from(element.classList);

        classList.forEach(className => {
            if (tailwindRegistry[className]) {
                accumulatedStyles += `\n${tailwindRegistry[className]}`;
            }
        });

        if (accumulatedStyles) {
            styleElement.innerHTML += accumulatedStyles;
        }
    }

    // 4. Inicia o Observador do Ciclo de Vida do Frontend
    const domObserver = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.type === 'childList') {
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === Node.ELEMENT_NODE) {
                        processElementClasses(node);
                        node.querySelectorAll('*').forEach(child => processElementClasses(child));
                    }
                });
            } else if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                processElementClasses(mutation.target);
            }
        });
    });

    // 5. Execução de Varredura Inicial (Estratégia SPA)
    domObserver.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['class']
    });

    document.querySelectorAll('*').forEach(element => processElementClasses(element));
})();
