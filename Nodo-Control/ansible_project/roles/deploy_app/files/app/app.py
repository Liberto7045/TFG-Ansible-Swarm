from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host='db', port=6379)

@app.route('/')
def index():
    count = r.incr('visitas')
    hostname = os.environ.get("HOSTNAME", "desconocido")
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TFG — Docker Swarm + Ansible</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; background: #f5f5f5; color: #1a1a2e; padding: 1.5rem 1rem; }}
    .container {{ max-width: 860px; margin: 0 auto; }}
    .header {{ border-bottom: 1px solid #e0e0e0; padding-bottom: 1.25rem; margin-bottom: 1.5rem; }}
    .status {{ display: flex; align-items: center; gap: 10px; margin-bottom: 6px; }}
    .dot {{ width: 10px; height: 10px; border-radius: 50%; background: #1D9E75; }}
    .status-text {{ font-size: 13px; color: #666; }}
    h1 {{ font-size: 22px; font-weight: 500; margin-bottom: 4px; }}
    .subtitle {{ font-size: 14px; color: #666; }}
    .metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 1.5rem; }}
    .metric {{ background: #ebebeb; border-radius: 8px; padding: 1rem; }}
    .metric-label {{ font-size: 13px; color: #666; margin-bottom: 4px; }}
    .metric-value {{ font-size: 28px; font-weight: 500; }}
    .metric-mono {{ font-size: 14px; font-weight: 500; font-family: monospace; margin-top: 6px; }}
    .cards {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 1.5rem; }}
    .card {{ background: #fff; border: 0.5px solid #ddd; border-radius: 12px; padding: 1rem 1.25rem; }}
    .card-title {{ font-size: 13px; font-weight: 500; color: #888; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.04em; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    td {{ padding: 6px 0; }}
    tr {{ border-bottom: 0.5px solid #eee; }}
    tr:last-child {{ border-bottom: none; }}
    .td-right {{ text-align: right; font-family: monospace; font-size: 12px; color: #444; }}
    .td-label {{ color: #666; }}
    .stack-row {{ display: flex; justify-content: space-between; align-items: center; font-size: 13px; margin-bottom: 8px; }}
    .badge {{ font-size: 11px; padding: 2px 8px; border-radius: 6px; }}
    .badge-blue {{ background: #e6f1fb; color: #185FA5; }}
    .badge-green {{ background: #eaf3de; color: #3B6D11; }}
    .badge-amber {{ background: #faeeda; color: #854F0B; }}
    .stack-mono {{ font-family: monospace; font-size: 11px; color: #888; }}
    .tech-card {{ background: #fff; border: 0.5px solid #ddd; border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: 1.5rem; }}
    .tags {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }}
    .tag {{ font-size: 12px; padding: 4px 10px; border: 0.5px solid #ccc; border-radius: 6px; color: #333; }}
    .footer {{ margin-top: 1.25rem; padding-top: 1rem; border-top: 0.5px solid #e0e0e0; font-size: 12px; color: #888; display: flex; justify-content: space-between; }}
  </style>
</head>
<body>
<div class="container">

  <div class="header">
    <div class="status">
      <div class="dot"></div>
      <span class="status-text">Clúster operativo</span>
    </div>
    <h1>TFG — Docker Swarm + Ansible</h1>
    <p class="subtitle">Despliegue automatizado de infraestructura de contenedores</p>
  </div>

  <div class="metrics">
    <div class="metric">
      <div class="metric-label">Visitas totales</div>
      <div class="metric-value">{count}</div>
    </div>
    <div class="metric">
      <div class="metric-label">Nodos activos</div>
      <div class="metric-value">3</div>
    </div>
    <div class="metric">
      <div class="metric-label">Réplicas web</div>
      <div class="metric-value">3</div>
    </div>
    <div class="metric">
      <div class="metric-label">Contenedor actual</div>
      <div class="metric-mono">{hostname[:8]}</div>
    </div>
  </div>

  <div class="cards">
    <div class="card">
      <div class="card-title">Infraestructura</div>
      <table>
        <tr><td class="td-label">Nodo Control</td><td class="td-right">192.168.56.10</td></tr>
        <tr><td class="td-label">Swarm Manager</td><td class="td-right">192.168.56.11</td></tr>
        <tr><td class="td-label">Worker 1</td><td class="td-right">192.168.56.12</td></tr>
        <tr><td class="td-label">Worker 2</td><td class="td-right">192.168.56.13</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">Stack desplegado</div>
      <div class="stack-row"><span class="td-label">Servicio web</span><span class="badge badge-blue">Flask · 3 réplicas</span></div>
      <div class="stack-row"><span class="td-label">Base de datos</span><span class="badge badge-green">Redis · 1 réplica</span></div>
      <div class="stack-row"><span class="td-label">Monitoring</span><span class="badge badge-amber">Visualizer · 1 réplica</span></div>
      <div class="stack-row"><span class="td-label">Red overlay</span><span class="stack-mono">mi_proyecto_red_proyecto</span></div>
    </div>
  </div>

  <div class="tech-card">
    <div class="card-title">Tecnologías</div>
    <div class="tags">
      <span class="tag">Docker Swarm</span>
      <span class="tag">Ansible 2.16</span>
      <span class="tag">Python Flask</span>
      <span class="tag">Redis</span>
      <span class="tag">Ubuntu 24.04</span>
      <span class="tag">VMware Workstation</span>
      <span class="tag">community.docker</span>
    </div>
  </div>

  <div class="footer">
    <span>Curso 2024–2025</span>
    <span>libertoTFG.swarm</span>
  </div>

</div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
