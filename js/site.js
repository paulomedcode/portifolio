/* MedCode: comportamento da landing page.
   Fica em arquivo próprio porque a CSP do vercel.json só libera JS inline por hash. */
(function () {
  // Vercel Web Analytics: fila de eventos customizados (o script /_vercel/insights a consome)
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
  function track(name, data) {
    try { window.va('event', { name: name, data: data }); } catch (e) { /* sem analytics, segue a vida */ }
  }

  // Todo clique em link de WhatsApp vira evento, com a origem vinda do data-origem
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="wa.me/"]');
    if (a) track('whatsapp_click', { origem: a.getAttribute('data-origem') || 'outro' });
  });

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Entrada suave das seções ao rolar
  var items = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('on'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  // FAQ: 8 perguntas à mostra, o resto atrás do botão (sem JS aparece tudo)
  var faqToggle = document.querySelector('.faq-toggle');
  var faqMore = document.getElementById('faq-mais');
  if (faqToggle && faqMore) {
    faqMore.hidden = true;
    faqToggle.hidden = false;
    faqToggle.addEventListener('click', function () {
      var open = faqToggle.getAttribute('aria-expanded') !== 'true';
      faqToggle.setAttribute('aria-expanded', open);
      faqMore.hidden = !open;
      faqToggle.textContent = open ? 'Mostrar menos dúvidas' : 'Ver todas as dúvidas';
    });
  }

  // Botão flutuante da Ana: fica escondido na primeira tela e quando já há um botão da Ana (ou o chat da demonstração) à vista
  var float = document.querySelector('.wa-float');
  var watch = document.querySelectorAll('.hero, section.ana, #contato, .iphone');
  if (float && watch.length && 'IntersectionObserver' in window) {
    var visible = new Set();
    var fo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) visible.add(e.target); else visible.delete(e.target); });
      float.classList.toggle('is-hidden', visible.size > 0);
    });
    watch.forEach(function (el) { fo.observe(el); });
  }

  // Botão do topo some enquanto o botão principal do hero está na tela (evita dois botões iguais)
  var topBtn = document.querySelector('.nav .btn-wa-sm');
  var heroCta = document.querySelector('.hero .ctas');
  if (topBtn && heroCta && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      topBtn.classList.toggle('is-hidden', entries[0].isIntersecting);
    }).observe(heroCta);
  }

  // Telefone: máscara e validação (formulário de contato e chat da Ana)
  function maskPhone(v) {
    var d = v.replace(/\D/g, '').slice(0, 11);
    if (d.length <= 2) return d.length ? '(' + d : '';
    if (d.length <= 6) return '(' + d.slice(0, 2) + ') ' + d.slice(2);
    if (d.length <= 10) return '(' + d.slice(0, 2) + ') ' + d.slice(2, 6) + '-' + d.slice(6);
    return '(' + d.slice(0, 2) + ') ' + d.slice(2, 7) + '-' + d.slice(7);
  }
  function validPhone(v) {
    var d = v.replace(/\D/g, '');
    // DDD válido (11 a 99) e celular com 9 na frente (11 dígitos) ou fixo (10 dígitos)
    return /^[1-9][1-9]/.test(d) && (d.length === 11 ? d[2] === '9' : d.length === 10);
  }
  function setErr(input, errId, bad) {
    input.setAttribute('aria-invalid', bad ? 'true' : 'false');
    document.getElementById(errId).hidden = !bad;
  }

  // ---------- Formulário "Prefere que a gente te chame?" ----------
  var form = document.getElementById('leadForm');
  if (form) {
    var phone = form.elements.whatsapp;
    var status = document.getElementById('formStatus');
    var submit = form.querySelector('.btn-submit');


    phone.addEventListener('input', function () { phone.value = maskPhone(phone.value); });
    phone.addEventListener('blur', function () { if (phone.value) setErr(phone, 'lf-whats-err', !validPhone(phone.value)); });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var nome = form.elements.nome, ok = form.elements.consentimento;
      var badNome = !nome.value.trim(), badPhone = !validPhone(phone.value), badOk = !ok.checked;
      setErr(nome, 'lf-nome-err', badNome);
      setErr(phone, 'lf-whats-err', badPhone);
      setErr(ok, 'lf-ok-err', badOk);
      if (badNome || badPhone || badOk) {
        (badNome ? nome : badPhone ? phone : ok).focus();
        return;
      }

      var interesse = form.elements.interesse.value;
      var payload = {
        nome: nome.value.trim(),
        whatsapp: phone.value,
        negocio: form.elements.negocio.value.trim(),
        interesse: interesse,
        consentimento: true,
        site: form.elements.site.value // honeypot: gente de verdade deixa vazio
      };

      submit.disabled = true;
      submit.textContent = 'Enviando...';
      status.className = 'form-status';
      status.textContent = '';

      fetch('/api/lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        track('lead_form_submit', { interesse: interesse });
        form.innerHTML = '<div class="form-done" tabindex="-1"><b>Recebemos! Vamos te chamar em breve.</b>' +
          '<p>Se preferir, você também pode falar com a gente agora pelo WhatsApp.</p></div>';
        form.querySelector('.form-done').focus();
      }).catch(function () {
        submit.disabled = false;
        submit.textContent = 'Quero que me chamem';
        status.className = 'form-status err';
        status.innerHTML = 'Não conseguimos enviar agora. Tente de novo ou fale direto com a gente:<br>' +
          '<a class="btn-wa-sm" data-origem="form-erro" target="_blank" rel="noopener" ' +
          'href="https://wa.me/5515991153174?text=' + encodeURIComponent('Oi! Tentei deixar meu contato no site, mas não foi.') + '">WhatsApp</a>';
      });
    });
  }

  // ---------- Teste rápido "Seu WhatsApp está perdendo clientes?" ----------
  var quiz = document.getElementById('quiz');
  if (quiz) {
    var respostas = {};
    var itens = quiz.querySelectorAll('.quiz-list li');
    var out = document.getElementById('quiz-out'), hint = document.getElementById('quiz-hint');
    var RESULT = [
      { k: 'Resultado', t: 'Seu WhatsApp está em dia 👏', x: 'Parabéns, pouca gente consegue. Se um dia o volume crescer, um agente de IA segura o atendimento sem você precisar contratar.', ok: true },
      { k: 'Resultado', t: 'Tem cliente escapando de vez em quando', x: 'Não é um problema grande, mas cada mensagem sem resposta rápida é uma venda em risco. Um agente de IA cobre exatamente esses buracos.' },
      { k: 'Resultado', t: 'Tem cliente escapando de vez em quando', x: 'Não é um problema grande, mas cada mensagem sem resposta rápida é uma venda em risco. Um agente de IA cobre exatamente esses buracos.' },
      { k: 'Atenção', t: 'Seu WhatsApp está perdendo clientes', x: 'Quem não recebe resposta rápida costuma chamar o concorrente. Um agente de IA responde em segundos, a qualquer hora, e passa pra você só o que precisa de você.' },
      { k: 'Atenção', t: 'Seu WhatsApp está perdendo clientes', x: 'Quem não recebe resposta rápida costuma chamar o concorrente. Um agente de IA responde em segundos, a qualquer hora, e passa pra você só o que precisa de você.' }
    ];
    var atualizar = function () {
      var n = Object.keys(respostas).length;
      if (n < itens.length) { hint.textContent = 'Faltam ' + (itens.length - n) + (itens.length - n === 1 ? ' pergunta.' : ' perguntas.'); return; }
      var sim = 0; for (var k in respostas) sim += respostas[k];
      var r = RESULT[sim];
      document.getElementById('quiz-kicker').textContent = r.k + ' · ' + sim + ' de ' + itens.length + ' sinais';
      document.getElementById('quiz-title').textContent = r.t;
      document.getElementById('quiz-text').textContent = r.x;
      out.classList.toggle('ok', !!r.ok);
      out.hidden = false;
      hint.hidden = true;
      track('teste_whatsapp', { sinais: sim });
    };
    itens.forEach(function (li, i) {
      li.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', 'false');
        b.addEventListener('click', function () {
          li.querySelectorAll('button').forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); });
          li.classList.add('answered');
          respostas[i] = Number(b.getAttribute('data-v'));
          atualizar();
        });
      });
    });
  }

  // ---------- Chat em tela cheia no celular (padrão da Ana e da Mariana) ----------
  // Até 760px o chat ocupa a tela toda: sem moldura, sem barras, só o X em cima pra sair.
  var CHAT_CELULAR = 760;
  var chatNoCelular = function () { return window.innerWidth <= CHAT_CELULAR; };
  // iPhone ignora overflow:hidden no body; prender o body no lugar é o que realmente trava a rolagem
  var travaY = 0;
  var travarPagina = function (classe) {
    travaY = window.scrollY;
    document.documentElement.classList.add(classe);
    document.body.style.position = 'fixed';
    document.body.style.top = -travaY + 'px';
    document.body.style.width = '100%';
  };
  var destravarPagina = function (classe) {
    document.documentElement.classList.remove(classe);
    document.body.style.position = document.body.style.top = document.body.style.width = '';
    window.scrollTo({ top: travaY, behavior: 'instant' });
  };
  // Quando o teclado abre, o chat encolhe pro espaço visível e o topo (com o X) não some
  var vv = window.visualViewport;
  var encaixarNaTela = function (el, ativo) {
    if (!vv || !ativo || !chatNoCelular()) { el.style.height = el.style.top = ''; return; }
    el.style.top = vv.offsetTop + 'px';
    el.style.height = vv.height + 'px';
  };

  // ---------- Chat com a Ana (Web Chat do GPT Maker num popup) ----------
  // A conversa abre direto, sem formulário: a própria Ana pede nome e WhatsApp quando a conversa
  // engata (instrução no additionalContext e no treinamento A14). O contexto segue pelo mesmo
  // protocolo de postMessage do float.js oficial do GPT Maker.
  var ANA_TOKEN = '3FA66368059223AF10886EB5C8FCB84B';
  var ANA_ORIGIN = 'https://app.gptmaker.ai';
  var anaDialog = document.getElementById('anaChat');
  if (anaDialog && typeof anaDialog.showModal === 'function') {
    var anaFrameBox = document.getElementById('anaFrame');
    var anaUser = null, anaIframe = null, anaLoaded = false, anaVisitante = null;
    try { anaUser = JSON.parse(sessionStorage.getItem('anaUser')); } catch (e) { /* sem storage */ }
    // id anônimo pra conversa continuar a mesma se a pessoa fechar e abrir de novo
    try { anaVisitante = sessionStorage.getItem('anaVisitante'); } catch (e) { /* sem storage */ }
    if (!anaVisitante) {
      anaVisitante = 'site-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
      try { sessionStorage.setItem('anaVisitante', anaVisitante); } catch (e) { /* segue */ }
    }

    var anaPost = function (msg) {
      if (anaIframe && anaIframe.contentWindow) anaIframe.contentWindow.postMessage(msg, ANA_ORIGIN);
    };
    var startChat = function () {
      anaFrameBox.hidden = false;
      anaDialog.classList.add('is-chatting');
      fitAna();
      if (!anaIframe) {
        anaIframe = document.createElement('iframe');
        anaIframe.src = ANA_ORIGIN + '/widget/' + ANA_TOKEN + '/iframe?floating=true';
        anaIframe.title = 'Conversa com a Ana, agente de IA da MedCode';
        anaIframe.allow = 'microphone';
        anaFrameBox.appendChild(anaIframe);
      } else if (anaLoaded) {
        anaPost({ type: 'gpt-maker-toogle', token: ANA_TOKEN });
      }
    };
    var lockPage = function () { travarPagina('ana-open'); };
    var unlockPage = function () { destravarPagina('ana-open'); };
    var openAna = function (e) {
      anaDialog.showModal();
      lockPage();
      var origem = e && e.currentTarget && e.currentTarget.getAttribute('data-origem');
      track('ana_chat_open', origem ? { origem: origem } : {});
      startChat();
    };
    var closeAna = function () {
      if (anaLoaded && !anaFrameBox.hidden) anaPost({ type: 'gpt-maker-toogle', token: ANA_TOKEN });
      anaDialog.close();
      anaDialog.style.height = anaDialog.style.top = '';
      unlockPage();
    };

    document.querySelectorAll('[data-open-ana]').forEach(function (b) { b.addEventListener('click', openAna); });
    anaDialog.querySelectorAll('[data-close-ana]').forEach(function (b) { b.addEventListener('click', closeAna); });

    var fitAna = function () {
      encaixarNaTela(anaDialog, anaDialog.open && anaDialog.classList.contains('is-chatting'));
    };
    if (vv) { vv.addEventListener('resize', fitAna); vv.addEventListener('scroll', fitAna); }
    anaDialog.addEventListener('cancel', function (e) { e.preventDefault(); closeAna(); });
    anaDialog.addEventListener('click', function (e) { if (e.target === anaDialog) closeAna(); });


    window.addEventListener('message', function (e) {
      if (e.origin !== ANA_ORIGIN || !e.data || !anaIframe || e.source !== anaIframe.contentWindow) return;
      var t = e.data.type;
      if (t === 'gpt-maker-on-load') {
        anaLoaded = true;
        if (anaDialog.open) anaPost({ type: 'gpt-maker-toogle', token: ANA_TOKEN });
      } else if (t === 'gpt-maker-button-close') {
        closeAna();
      } else if (t === 'gpt-maker-request-context') {
        if (anaUser && anaUser.whatsapp) {
          var d = anaUser.whatsapp.replace(/\D/g, '');
          anaPost({
            type: 'gpt-maker-context-response',
            userMetadata: { id: '55' + d, name: anaUser.nome, phone: '55' + d },
            additionalContext: 'Visitante do site da MedCode, conversando pelo chat do site. Nome e WhatsApp já informados; não peça de novo.'
          });
        } else {
          anaPost({
            type: 'gpt-maker-context-response',
            userMetadata: { id: anaVisitante, name: 'Visitante do site' },
            additionalContext: 'Visitante do site da MedCode, conversando pelo chat do site. Ainda não informou nome nem WhatsApp. Converse primeiro; depois de 2 ou 3 trocas, quando a conversa engatar ou quando a pessoa pedir proposta, valores detalhados ou diagnóstico, peça o nome e o WhatsApp de forma natural, numa mensagem só, explicando que é pra equipe continuar com ela se a conversa cair.'
          });
        }
      }
    });
  }

  // ---------- Demonstração ao vivo (página da saúde) ----------
  // O chat da clínica fictícia só carrega quando a pessoa toca no celular.
  // No celular, o chat abre em tela cheia (mesmo padrão da Ana) e o X volta pro iPhone.
  var demoCel = document.querySelector('.iphone');
  var fitDemo = function () {
    if (demoCel) encaixarNaTela(demoCel, document.documentElement.classList.contains('demo-aberta'));
  };
  var fecharDemo = function () {
    if (!document.documentElement.classList.contains('demo-aberta')) return;
    destravarPagina('demo-aberta');
    fitDemo();
  };
  document.querySelectorAll('[data-demo-iniciar]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.iphone-chat');
      var frame = box && box.querySelector('iframe[data-demo-src]');
      if (!frame) return;
      if (!frame.src) frame.src = frame.getAttribute('data-demo-src');
      if (box.classList.contains('ligado')) {
        track('demo_clinica_voltar', {});
      } else {
        box.classList.add('ligado');
        track('demo_clinica_abrir', {});
      }
      var aviso = btn.querySelector('em');
      if (aviso) aviso.textContent = 'Continuar conversa';
      if (chatNoCelular()) {
        travarPagina('demo-aberta');
        fitDemo();
      }
    });
  });
  document.querySelectorAll('[data-demo-fechar]').forEach(function (b) { b.addEventListener('click', fecharDemo); });
  if (vv) { vv.addEventListener('resize', fitDemo); vv.addEventListener('scroll', fitDemo); }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fecharDemo(); });
  // O Web Chat do GPT Maker só aparece depois de receber o contexto do visitante
  // (mesmo protocolo de postMessage do chat da Ana, mais abaixo).
  var demoFrame = document.querySelector('iframe[data-demo-src]');
  if (demoFrame) {
    var demoId = null;
    try { demoId = sessionStorage.getItem('demoVisitante'); } catch (e) { /* sem storage */ }
    if (!demoId) {
      demoId = 'demo-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
      try { sessionStorage.setItem('demoVisitante', demoId); } catch (e) { /* segue */ }
    }
    window.addEventListener('message', function (e) {
      if (e.origin !== 'https://app.gptmaker.ai' || e.source !== demoFrame.contentWindow || !e.data) return;
      if (e.data.type === 'gpt-maker-on-load') {
        // modo "floating": a janela só abre depois do toggle, como no chat da Ana.
        // Se o toggle chega antes do widget processar o contexto, ele não abre; repetir é
        // seguro (o widget ignora o toggle quando a conversa já carregou).
        [0, 700, 1600, 3000, 5000].forEach(function (ms) {
          setTimeout(function () {
            if (demoFrame.contentWindow) demoFrame.contentWindow.postMessage({ type: 'gpt-maker-toogle', token: demoFrame.getAttribute('data-demo-token') }, 'https://app.gptmaker.ai');
          }, ms);
        });
      } else if (e.data.type === 'gpt-maker-request-context') {
        demoFrame.contentWindow.postMessage({
          type: 'gpt-maker-context-response',
          userMetadata: { id: demoId, name: 'Visitante da demonstração' },
          additionalContext: 'Visitante testando a demonstração da Center Clínica (clínica fictícia) no site da MedCode. Atenda como paciente normal.'
        }, 'https://app.gptmaker.ai');
      }
    });
  }

  // ---------- Animações do hero ----------
  if (reduce) return;

  // Palavra que se digita e apaga (a frase fixa para leitores de tela fica no .sr-only)
  // Cada página pode trocar as palavras e as mensagens pelos atributos data-* (separadas por |)
  function list(node, attr, fallback) {
    var v = node && node.getAttribute(attr);
    return v ? v.split('|') : fallback;
  }
  var el = document.getElementById('typed');
  var words = list(el, 'data-words', ['velocidade', 'folga', 'resposta 24h', 'mais vendas']);
  if (el) {
    var w = 0, i = words[0].length, deleting = true;

    // Reserva a altura da maior palavra pra a digitação não empurrar a foto e o resto da página
    var sub = el.closest('[data-typed-box]') || el.closest('.hero-sub');
    var reserveHeight = function () {
      var current = el.textContent, max = 0;
      sub.style.minHeight = '';
      words.forEach(function (wd) { el.textContent = wd; max = Math.max(max, sub.offsetHeight); });
      el.textContent = current;
      sub.style.minHeight = max + 'px';
    };
    reserveHeight();
    if (document.fonts) document.fonts.ready.then(reserveHeight);
    window.addEventListener('resize', reserveHeight);

    setTimeout(function tick() {
      var word = words[w];
      i += deleting ? -1 : 1;
      el.textContent = word.slice(0, i);
      var delay = deleting ? 55 : 95;
      if (deleting && i === 0) { deleting = false; w = (w + 1) % words.length; delay = 300; }
      else if (!deleting && i === word.length) { deleting = true; delay = 1800; }
      setTimeout(tick, delay);
    }, 1800);
  }

  // Mensagens do agente alternando, com "digitando..."
  var chat = document.getElementById('chatMsg'), m = 0;
  var msgs = list(chat, 'data-msgs', [
    'Oi! Antes de seguirmos, pode me dizer seu nome? Assim personalizo seu atendimento 😊',
    'Temos horário amanhã às 9h ou às 15h. Qual fica melhor pra você?',
    'Prontinho! Te mando um lembrete 1h antes. Posso ajudar em algo mais?'
  ]);
  if (chat) setInterval(function () {
    m = (m + 1) % msgs.length;
    chat.innerHTML = '<span class="dots"><i></i><i></i><i></i></span>';
    setTimeout(function () { chat.textContent = msgs[m]; }, 1100);
  }, 4200);

  // Pílula de ação alternando
  var pill = document.getElementById('pill'), pillText = document.getElementById('pillText'), p = 0;
  var pills = list(pill, 'data-pills', ['Horário agendado para 15h', 'Orçamento enviado', 'Transferido para humano', 'Lembrete enviado']);
  if (pill) setInterval(function () {
    pill.style.opacity = 0;
    setTimeout(function () { p = (p + 1) % pills.length; pillText.textContent = pills[p]; pill.style.opacity = 1; }, 350);
  }, 3000);
})();
