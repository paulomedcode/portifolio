"""Gera as artes das redes sociais da MedCode (foto de perfil, capas de destaque e banner).

Uso (na raiz do repositório): python3 _redes/gerar_imagens.py
Monta cada arte em HTML (cores e fontes do site) e exporta em PNG com o Chrome headless.
"""
import base64
import subprocess
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "_redes/imagens"
SAIDA.mkdir(parents=True, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

FONTES = '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Manrope:wght@500;700;800&display=block" rel="stylesheet">'
BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden}
body{font-family:'Manrope',sans-serif;-webkit-font-smoothing:antialiased}
.grad{background:linear-gradient(135deg,#3b2bb8 0%,#6d4aff 55%,#3b82f6 100%)}
"""
# Símbolo </> do logo (mesmo traço do favicon)
CODIGO = '<path d="M8.5 8L4.5 12l4 4M15.5 8l4 4-4 4M13.2 6.5l-2.4 11"/>'


def foto(nome):
    return "data:image/png;base64," + base64.b64encode((RAIZ / "public" / nome).read_bytes()).decode()


def svg(paths, tamanho, cor="#fff", traco=2):
    return (f'<svg width="{tamanho}" height="{tamanho}" viewBox="0 0 24 24" fill="none" stroke="{cor}" '
            f'stroke-width="{traco}" stroke-linecap="round" stroke-linejoin="round">{paths}</svg>')


def render(nome, largura, altura, corpo, css=""):
    html = f"<!doctype html><html><head><meta charset='utf-8'>{FONTES}<style>{BASE_CSS}{css}</style></head><body>{corpo}</body></html>"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        caminho = f.name
    destino = SAIDA / f"{nome}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={largura},{altura}", "--virtual-time-budget=6000",
                    f"--screenshot={destino}", f"file://{caminho}"], check=True, capture_output=True)
    print("ok", destino.name)


# ---------- Foto de perfil (1080x1080; o Instagram corta em círculo) ----------
render("perfil-a-simbolo", 1080, 1080, f"""
<div class="grad" style="width:1080px;height:1080px;display:flex;align-items:center;justify-content:center">
  <div style="width:560px;height:560px;border-radius:150px;background:rgba(255,255,255,.14);border:6px solid rgba(255,255,255,.35);display:flex;align-items:center;justify-content:center">
    {svg(CODIGO, 400, traco=2.2)}
  </div>
</div>""")

render("perfil-b-nome", 1080, 1080, f"""
<div style="width:1080px;height:1080px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;padding-bottom:10px">
  <div class="grad" style="width:400px;height:400px;border-radius:112px;display:flex;align-items:center;justify-content:center;box-shadow:0 40px 80px -40px rgba(81,54,217,.7)">
    {svg(CODIGO, 290, traco=2.5)}
  </div>
  <div style="font-family:'Bricolage Grotesque';font-weight:800;font-size:200px;letter-spacing:-7px;line-height:.9;color:#14112e">Med<span style="background:linear-gradient(90deg,#6d4aff,#3b82f6);-webkit-background-clip:text;color:transparent">Code</span></div>
</div>""")

render("perfil-c-ana", 1080, 1080, f"""
<div class="grad" style="width:1080px;height:1080px;display:flex;align-items:center;justify-content:center;position:relative">
  <div style="width:900px;height:900px;border-radius:50%;overflow:hidden;border:16px solid #fff">
    <img src="{foto('perfil_assistente.png')}" style="width:100%;height:100%;object-fit:cover;object-position:50% 22%">
  </div>
  <div class="grad" style="position:absolute;right:150px;bottom:150px;width:200px;height:200px;border-radius:56px;border:12px solid #fff;display:flex;align-items:center;justify-content:center">
    {svg(CODIGO, 130, traco=2.6)}
  </div>
</div>""")

# ---------- Capas dos destaques (1080x1920; o Instagram mostra o círculo do meio) ----------
ICONES = {
    "teste-a-ia": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/><path d="M8 12h.01M12 12h.01M16 12h.01"/>',
    "clinicas": '<path d="M12 21s-7-4.35-7-10a4 4 0 0 1 7-2.65A4 4 0 0 1 19 11c0 5.65-7 10-7 10z"/><path d="M12 9v4M10 11h4"/>',
    "comercio": '<path d="M3 9l1.5-5h15L21 9"/><path d="M3 9h18v2a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0z"/><path d="M5 13v7h14v-7M10 20v-4h4v4"/>',
    "sites": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>' + '<path d="M9.5 8.5L8 10l1.5 1.5M14.5 8.5L16 10l-1.5 1.5"/>',
    "quem-sou": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "fale-com-a-gente": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
}
for nome, paths in ICONES.items():
    render(f"destaque-{nome}", 1080, 1920, f"""
<div class="grad" style="width:1080px;height:1920px;display:flex;align-items:center;justify-content:center">
  {svg(paths, 520 if nome == "clinicas" else 420, traco=1.5 if nome == "clinicas" else 1.7)}
</div>""")

# ---------- Banner do LinkedIn (1584x396) ----------
render("banner-linkedin", 1584, 396, f"""
<div class="grad" style="width:1584px;height:396px;position:relative;overflow:hidden;color:#fff">
  <div style="position:absolute;right:-120px;top:-160px;width:620px;height:620px;border-radius:50%;background:rgba(255,255,255,.07)"></div>
  <div style="position:absolute;left:520px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;width:640px">
    <div style="font-size:19px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#d9d2ff">MedCode Assessoria</div>
    <div style="font-family:'Bricolage Grotesque';font-weight:800;font-size:46px;line-height:1.08;letter-spacing:-1.2px;margin-top:10px">Agentes de IA no WhatsApp, sites e sistemas para empresas</div>
    <div style="font-size:21px;font-weight:700;margin-top:16px;color:#e6e0ff">Especialistas em clínicas e consultórios · medcodedev.com</div>
  </div>
  <div style="position:absolute;right:70px;top:70px;display:flex;flex-direction:column;gap:12px;width:300px;font-size:17px;font-weight:700">
    <div style="align-self:flex-end;background:#00a884;padding:12px 16px;border-radius:16px 16px 4px 16px">Tem horário amanhã? 🎤</div>
    <div style="background:#fff;color:#14112e;padding:12px 16px;border-radius:16px 16px 16px 4px">Tenho sim! 9h ou 15h, qual prefere? 😊</div>
    <div style="align-self:flex-end;background:#00a884;padding:12px 16px;border-radius:16px 16px 4px 16px">9h 👍</div>
  </div>
</div>""")
