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

  // Botão flutuante de WhatsApp some quando já há um botão de WhatsApp na tela
  var float = document.querySelector('.wa-float');
  var watch = document.querySelectorAll('.hero .ctas, #contato');
  if (float && watch.length && 'IntersectionObserver' in window) {
    var visible = new Set();
    var fo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) visible.add(e.target); else visible.delete(e.target); });
      float.classList.toggle('is-hidden', visible.size > 0);
    });
    watch.forEach(function (el) { fo.observe(el); });
  }

  // ---------- Formulário "Prefere que a gente te chame?" ----------
  var form = document.getElementById('leadForm');
  if (form) {
    var phone = form.elements.whatsapp;
    var status = document.getElementById('formStatus');
    var submit = form.querySelector('.btn-submit');

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
          'href="https://wa.me/5511991649612?text=' + encodeURIComponent('Oi! Tentei deixar meu contato no site, mas não foi.') + '">WhatsApp</a>';
      });
    });
  }

  // ---------- Animações do hero ----------
  if (reduce) return;

  // Palavra que se digita e apaga (a frase fixa para leitores de tela fica no .sr-only)
  var words = ['velocidade', 'folga', 'resposta 24h', 'mais vendas'];
  var el = document.getElementById('typed');
  if (el) {
    var w = 0, i = words[0].length, deleting = true;

    // Reserva a altura da maior palavra pra a digitação não empurrar a foto e o resto da página
    var sub = el.closest('.hero-sub');
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
  var msgs = [
    'Oi! Antes de seguirmos, pode me dizer seu nome? Assim personalizo seu atendimento 😊',
    'Temos horário amanhã às 9h ou às 15h. Qual fica melhor pra você?',
    'Prontinho! Te mando um lembrete 1h antes. Posso ajudar em algo mais?'
  ];
  var chat = document.getElementById('chatMsg'), m = 0;
  if (chat) setInterval(function () {
    m = (m + 1) % msgs.length;
    chat.innerHTML = '<span class="dots"><i></i><i></i><i></i></span>';
    setTimeout(function () { chat.textContent = msgs[m]; }, 1100);
  }, 4200);

  // Pílula de ação alternando
  var pills = ['Horário agendado para 15h', 'Orçamento enviado', 'Transferido para humano', 'Lembrete enviado'];
  var pill = document.getElementById('pill'), pillText = document.getElementById('pillText'), p = 0;
  if (pill) setInterval(function () {
    pill.style.opacity = 0;
    setTimeout(function () { p = (p + 1) % pills.length; pillText.textContent = pills[p]; pill.style.opacity = 1; }, 350);
  }, 3000);
})();
