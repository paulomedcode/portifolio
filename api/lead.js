// POST /api/lead: recebe o formulário "Prefere que a gente te chame?" e o cadastro antes do
// chat com a Ana (origem "chat-ana") e manda por e-mail.
// Envio pelo Resend (https://resend.com), só com fetch, sem dependências.
// Variáveis de ambiente na Vercel (Settings > Environment Variables):
//   RESEND_API_KEY  chave da API do Resend (obrigatória, nunca vai pro front-end)
//   LEAD_TO         destino (padrão: contato@medcodedev.com)
//   LEAD_FROM       remetente; precisa ser de um domínio verificado no Resend
//                   (padrão: "Site MedCode <onboarding@resend.dev>", que só entrega pro e-mail da conta Resend)

const INTERESSES = ['Agente de IA', 'Site/Landing page', 'Site + Agente', 'Sistema sob medida', 'Consultoria', 'Ainda não sei'];

function clean(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u001f\u007f]/g, ' ').trim().slice(0, max);
}
function esc(s) {
  return s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = null; }
  }
  if (!body || typeof body !== 'object') return res.status(400).json({ ok: false, error: 'invalid' });

  // Honeypot preenchido: é robô. Responde "ok" pra ele não insistir, mas não envia nada.
  if (clean(body.site, 200)) return res.status(200).json({ ok: true });

  const nome = clean(body.nome, 80);
  const whatsapp = clean(body.whatsapp, 20);
  const digits = whatsapp.replace(/\D/g, '');
  const negocio = clean(body.negocio, 80);
  const interesse = INTERESSES.includes(body.interesse) ? body.interesse : 'Ainda não sei';
  const chatAna = body.origem === 'chat-ana';

  if (!nome || !/^[1-9][1-9]\d{8,9}$/.test(digits) || body.consentimento !== true) {
    return res.status(400).json({ ok: false, error: 'invalid' });
  }

  const key = process.env.RESEND_API_KEY;
  if (!key) {
    console.error('lead: RESEND_API_KEY não configurada');
    return res.status(500).json({ ok: false, error: 'config' });
  }

  const to = process.env.LEAD_TO || 'contato@medcodedev.com';
  const from = process.env.LEAD_FROM || 'Site MedCode <onboarding@resend.dev>';
  const quando = new Date().toLocaleString('pt-BR', { timeZone: 'America/Sao_Paulo' });
  const waLink = 'https://wa.me/55' + digits;

  const linhas = chatAna
    ? [
        ['Nome', nome],
        ['WhatsApp', whatsapp],
        ['Onde', 'Chat com a Ana no site (a conversa fica no GPT Maker, canal "Site MedCode")'],
        ['Consentimento LGPD', 'Sim, aceitou a Política de Privacidade'],
        ['Recebido em', quando],
      ]
    : [
        ['Nome', nome],
        ['WhatsApp', whatsapp],
        ['Tipo de negócio', negocio || '(não informado)'],
        ['Interesse', interesse],
        ['Consentimento LGPD', 'Sim, aceitou a Política de Privacidade'],
        ['Recebido em', quando],
      ];
  const titulo = chatAna ? 'Uma pessoa começou a conversar com a Ana no site' : 'Novo contato pelo site';
  const assunto = chatAna ? `Chat com a Ana no site: ${nome}` : `Novo contato pelo site: ${nome} (${interesse})`;

  const html =
    `<h2 style="font-family:sans-serif">${titulo}</h2>` +
    '<table style="font-family:sans-serif;font-size:15px;border-collapse:collapse">' +
    linhas.map(([k, v]) => `<tr><td style="padding:4px 12px 4px 0;color:#666">${k}</td><td style="padding:4px 0"><b>${esc(v)}</b></td></tr>`).join('') +
    '</table>' +
    `<p style="font-family:sans-serif"><a href="${waLink}">Chamar no WhatsApp</a></p>`;
  const text = linhas.map(([k, v]) => `${k}: ${v}`).join('\n') + `\n\nChamar: ${waLink}`;

  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from, to: [to], subject: assunto, html, text }),
    });
    if (!r.ok) {
      console.error('lead: Resend respondeu', r.status, await r.text());
      return res.status(502).json({ ok: false, error: 'send' });
    }
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('lead: falha ao enviar', err);
    return res.status(502).json({ ok: false, error: 'send' });
  }
};
