from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Simple App Dashboard</title>
  <style>
    :root { --ink:#172033; --muted:#687386; --line:#e6eaf0; --blue:#4169e1; --bg:#f4f7fb; }
    * { box-sizing: border-box; }
    body { margin:0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; background:var(--bg); color:var(--ink); }
    header { background:#fff; border-bottom:1px solid var(--line); padding:18px 6%; display:flex; align-items:center; justify-content:space-between; }
    .brand { display:flex; gap:12px; align-items:center; font-weight:750; font-size:18px; }
    .logo { width:38px; height:38px; border-radius:12px; display:grid; place-items:center; color:white; background:linear-gradient(135deg,#4169e1,#8a5cf6); font-size:19px; }
    .pill { font-size:12px; padding:7px 11px; background:#e9f9ef; color:#187344; border-radius:999px; font-weight:700; }
    main { max-width:1040px; margin:46px auto; padding:0 22px; }
    .eyebrow { color:var(--blue); text-transform:uppercase; letter-spacing:1.7px; font-size:12px; font-weight:800; }
    h1 { font-size:clamp(30px,5vw,44px); letter-spacing:-1.3px; margin:12px 0; }
    .intro { color:var(--muted); font-size:16px; line-height:1.7; max-width:650px; }
    .cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:18px; margin-top:32px; }
    .card { background:#fff; border:1px solid var(--line); border-radius:18px; padding:23px; box-shadow:0 8px 24px rgba(25,40,70,.04); }
    .icon { width:42px; height:42px; border-radius:13px; background:#edf1ff; display:grid; place-items:center; font-size:21px; }
    .card h2 { font-size:16px; margin:18px 0 7px; }
    .value { font-size:22px; font-weight:800; }
    .hint { color:var(--muted); font-size:13px; line-height:1.6; margin-top:8px; }
    .panel { margin-top:22px; padding:26px; border-radius:18px; color:white; background:linear-gradient(115deg,#202e55,#3e4e91); display:flex; gap:24px; align-items:center; justify-content:space-between; flex-wrap:wrap; }
    .panel h2 { margin:0 0 8px; font-size:20px; }
    .panel p { margin:0; color:#dce4ff; line-height:1.6; font-size:14px; }
    a.button { display:inline-block; text-decoration:none; background:white; color:#24366e; padding:12px 17px; border-radius:11px; font-weight:750; white-space:nowrap; }
    footer { text-align:center; padding:24px; color:var(--muted); font-size:12px; }
    @media (max-width:560px) { header { padding:14px 5%; } main { margin:32px auto; } .panel { align-items:flex-start; } }
  </style>
</head>
<body>
  <header>
    <div class="brand"><div class="logo">✦</div> Sample Dashboard</div>
    <div class="pill">● App is running</div>
  </header>
  <main>
    <div class="eyebrow">Flask starter app</div>
    <h1>Welcome back 👋</h1>
    <p class="intro">Your Python web application is up and running. This is a simple dashboard you can extend with database data, APIs, or your own features.</p>
    <section class="cards">
      <article class="card">
        <div class="icon">🐍</div>
        <h2>Application</h2>
        <div class="value">Flask</div>
        <div class="hint">Python web framework serving this page.</div>
      </article>
      <article class="card">
        <div class="icon">🌐</div>
        <h2>Web server</h2>
        <div class="value">Online</div>
        <div class="hint">Your browser is receiving a response from the app.</div>
      </article>
      <article class="card">
        <div class="icon">🗄️</div>
        <h2>Database</h2>
        <div class="value">{{ db_label }}</div>
        <div class="hint">This starter page does not require MySQL to load.</div>
      </article>
    </section>
    <section class="panel">
      <div>
        <h2>Your dashboard is ready</h2>
        <p>Start with this interface, then connect a database when you're ready.</p>
      </div>
      <a class="button" href="/health">Check app health →</a>
    </section>
  </main>
  <footer>Built with Python + Flask · Simple starter dashboard</footer>
</body>
</html>
"""

@app.route("/")
def home():
    # The page intentionally loads without requiring a database connection.
    return render_template_string(HTML, db_label="Not connected")

@app.route("/health")
def health():
    return {"status": "ok", "application": "simple-flask-dashboard"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
