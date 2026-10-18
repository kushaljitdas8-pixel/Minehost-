from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

SERVERS = []

# --- ULTIMATE PROFESSIONAL SINGLE-FILE ENTERPRISE TEMPLATE ---
PANEL_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }} - MineHost Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', sans-serif; }
        body { background-color: #0b0f19; color: #f8fafc; display: flex; height: 100vh; overflow: hidden; }
        .sidebar { width: 270px; background: #111827; border-right: 1px solid rgba(255,255,255,0.06); display: flex; flex-direction: column; padding: 30px; }
        .logo { font-size: 24px; font-weight: 800; color: #10b981; margin-bottom: 45px; text-decoration: none; }
        .logo span { color: #fff; }
        .nav-item { padding: 14px 18px; color: #94a3b8; text-decoration: none; border-radius: 10px; margin-bottom: 10px; font-weight: 600; transition: 0.3s; display: block; }
        .nav-item:hover, .nav-item.active { background: #1f2937; color: #10b981; }
        .main-content { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
        .topbar { padding: 22px 40px; background: #111827; border-bottom: 1px solid rgba(255,255,255,0.06); display: flex; justify-content: space-between; align-items: center; }
        .back-btn { background: #1f2937; color: #fff; padding: 9px 18px; border-radius: 8px; text-decoration: none; font-size: 14px; border: 1px solid rgba(255,255,255,0.08); font-weight: 600; }
        .back-btn:hover { border-color: #10b981; color: #10b981; }
        .panel-body { flex: 1; padding: 35px; overflow-y: auto; }
        
        .create-box { background: #111827; padding: 35px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.06); margin-bottom: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
        .create-box h3 { margin-bottom: 22px; font-size: 22px; color: #10b981; font-weight: 700; }
        .form-row { display: flex; gap: 25px; margin-bottom: 22px; }
        .form-group { flex: 1; }
        label { display: block; margin-bottom: 8px; color: #94a3b8; font-size: 14px; font-weight: 500; }
        input, select { width: 100%; padding: 14px; background: #0b0f19; border: 1px solid rgba(255,255,255,0.12); border-radius: 10px; color: #fff; font-size: 15px; }
        input:focus, select:focus { outline: none; border-color: #10b981; }
        .btn-create { background: #10b981; color: #0b0f19; padding: 14px 28px; border: none; border-radius: 10px; font-weight: 700; cursor: pointer; transition: 0.3s; }
        .btn-create:hover { background: #059669; }
        
        .servers-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 25px; }
        .server-card { background: #111827; padding: 30px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.06); box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
        .server-card h4 { font-size: 20px; margin-bottom: 8px; color: #fff; font-weight: 700; }
        .server-meta { color: #94a3b8; font-size: 14px; margin-bottom: 8px; }
        
        .status-online { display: inline-block; padding: 5px 12px; background: rgba(16, 185, 129, 0.15); color: #10b981; border-radius: 6px; font-size: 12px; font-weight: 700; margin-bottom: 18px; }
        .status-offline { display: inline-block; padding: 5px 12px; background: rgba(239, 68, 68, 0.15); color: #ef4444; border-radius: 6px; font-size: 12px; font-weight: 700; margin-bottom: 18px; }
        
        .btn-action-group { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
        .btn-action { flex: 1; min-width: 30%; text-align: center; padding: 10px 8px; background: #1f2937; color: #fff; text-decoration: none; border-radius: 8px; font-size: 12px; font-weight: 600; border: 1px solid rgba(255,255,255,0.06); transition: 0.3s; }
        .btn-action:hover { border-color: #10b981; color: #10b981; }
        .btn-start { background: rgba(16, 185, 129, 0.2); color: #10b981; border-color: rgba(16, 185, 129, 0.4); }
        .btn-start:hover { background: #10b981; color: #0b0f19; }
        .btn-stop { background: rgba(239, 68, 68, 0.2); color: #ef4444; border-color: rgba(239, 68, 68, 0.4); }
        .btn-stop:hover { background: #ef4444; color: #fff; }

        .terminal { background: #050709; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 22px; font-family: 'JetBrains Mono', monospace; font-size: 14px; color: #10b981; height: 62vh; overflow-y: auto; white-space: pre-wrap; margin-bottom: 20px; line-height: 1.6; }
        .cmd-form { display: flex; gap: 12px; }
        .cmd-input { flex: 1; padding: 14px; background: #111827; border: 1px solid rgba(255,255,255,0.12); border-radius: 10px; color: #fff; font-family: 'JetBrains Mono', monospace; font-size: 14px; }
        .cmd-input:focus { outline: none; border-color: #10b981; }
        .btn-send { background: #10b981; color: #0b0f19; padding: 0 30px; border: none; border-radius: 10px; font-weight: 700; cursor: pointer; transition: 0.3s; }
        .btn-send:hover { background: #059669; }

        .file-table { width: 100%; border-collapse: collapse; background: #111827; border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.06); }
        .file-table th, .file-table td { padding: 16px 22px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.04); font-size: 14px; }
        .file-table th { background: #1f2937; color: #10b981; font-weight: 700; }
        
        .plugin-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 22px; }
        .plugin-card { background: #111827; padding: 22px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.06); display: flex; flex-direction: column; justify-content: space-between; }
        .plugin-card h4 { color: #10b981; margin-bottom: 8px; font-size: 17px; font-weight: 700; }
        .plugin-card p { color: #94a3b8; font-size: 13px; margin-bottom: 18px; line-height: 1.5; }
        .btn-install { background: #1f2937; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer; text-align: center; text-decoration: none; transition: 0.3s; }
        .btn-install:hover { background: #10b981; color: #0b0f19; }
        
        .panel-box { background: #111827; padding: 30px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.06); max-width: 650px; }
        .panel-box h3 { color: #10b981; margin-bottom: 18px; font-size: 20px; font-weight: 700; }
        .data-display { background: #0b0f19; padding: 16px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 15px; color: #10b981; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 18px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <a href="/dashboard" class="logo">Mine<span>Host</span> Pro</a>
        {% if server %}
            <a href="/console/{{ index }}" class="nav-item {% if active_tab == 'console' %}active{% endif %}">Console Logs</a>
            <a href="/files/{{ index }}" class="nav-item {% if active_tab == 'files' %}active{% endif %}">File Manager</a>
            <a href="/plugins/{{ index }}" class="nav-item {% if active_tab == 'plugins' %}active{% endif %}">Plugins Marketplace</a>
            <a href="/network/{{ index }}" class="nav-item {% if active_tab == 'network' %}active{% endif %}">IP & Port Network</a>
            <a href="/settings/{{ index }}" class="nav-item {% if active_tab == 'settings' %}active{% endif %}">Server Settings</a>
            <a href="/dashboard" class="nav-item" style="margin-top: 25px; color: #ef4444;">&larr; Exit Instance</a>
        {% else %}
            <a href="/dashboard" class="nav-item active">Cluster Nodes</a>
            <a href="/dashboard" class="nav-item" style="margin-top: auto; color: #10b981;">Node Status: Active</a>
        {% endif %}
    </div>
    <div class="main-content">
        <div class="topbar">
            <h2>{% if server %}{{ server.name }} &mdash; <span style="color: #10b981; font-size: 16px;">{{ page_title }}</span>{% else %}Enterprise Cloud Dashboard{% endif %}</h2>
            {% if server %}
                <a href="/dashboard" class="back-btn">Dashboard</a>
            {% else %}
                <div class="user-badge">&#9679; Local IP: 127.0.0.1:5000</div>
            {% endif %}
        </div>
        <div class="panel-body">
            
            {% if server and active_tab == 'console' %}
                <div class="terminal">
                    <span style="color: #64748b;">[Server thread/INFO]: Booting up isolated game container...</span><br>
                    <span style="color: #64748b;">[Server thread/INFO]: Loading libraries, assets and world configs...</span><br>
                    <span style="color: #10b981;">[Server thread/INFO]: Preparing level "world"</span><br>
                    <span style="color: #10b981;">[Server thread/INFO]: Done (1.205s)! Type "help" for console commands</span><br>
                    {% if server.status == 'ONLINE' %}
                    <br><span style="color: #10b981;">[Server thread/INFO]: Node status: ONLINE & accepting network socket packets!</span>
                    {% else %}
                    <br><span style="color: #ef4444;">[Server thread/WARN]: Node status: Instance is OFFLINE. Start from dashboard.</span>
                    {% endif %}
                </div>
                <form class="cmd-form" onsubmit="event.preventDefault(); alert('Command dispatched to container console!');">
                    <input type="text" class="cmd-input" placeholder="Type console command (e.g., say Hello, op player, whitelist)..." required>
                    <button type="submit" class="btn-send">Execute</button>
                </form>

            {% elif server and active_tab == 'files' %}
                <h3 style="margin-bottom: 20px; color: #10b981;">Instance Root Directory</h3>
                <table class="file-table">
                    <tr><th>Name</th><th>Type</th><th>Size</th><th>Action</th></tr>
                    <tr><td>📁 plugins</td><td>Directory</td><td>--</td><td><a href="#" onclick="alert('Accessing plugins directory...'); return false;" style="color: #10b981; text-decoration: none;">Open</a></td></tr>
                    <tr><td>📁 world</td><td>Directory</td><td>--</td><td><a href="#" onclick="alert('Accessing world files...'); return false;" style="color: #10b981; text-decoration: none;">Open</a></td></tr>
                    <tr><td>📄 server.properties</td><td>Config</td><td>1.6 KB</td><td><a href="#" onclick="alert('Opening property editor...'); return false;" style="color: #10b981; text-decoration: none;">Edit</a></td></tr>
                    <tr><td>📄 server.jar</td><td>Executable</td><td>46.4 MB</td><td><a href="#" onclick="alert('Inspecting server core binary...'); return false;" style="color: #10b981; text-decoration: none;">Inspect</a></td></tr>
                </table>

            {% elif server and active_tab == 'plugins' %}
                <h3 style="margin-bottom: 20px; color: #10b981;">One-Click Plugin Marketplace</h3>
                <div class="plugin-grid">
                    <div class="plugin-card">
                        <div><h4>DeluxeHub</h4><p>Custom lobbies, scoreboards, menus and tablists.</p></div>
                        <a href="#" onclick="alert('DeluxeHub installed successfully!'); return false;" class="btn-install">Install</a>
                    </div>
                    <div class="plugin-card">
                        <div><h4>GeyserMC + Floodgate</h4><p>Cross-play support for Bedrock & Java players.</p></div>
                        <a href="#" onclick="alert('GeyserMC installed successfully!'); return false;" class="btn-install">Install</a>
                    </div>
                    <div class="plugin-card">
                        <div><h4>LuckPerms</h4><p>Advanced permissions and ranking framework.</p></div>
                        <a href="#" onclick="alert('LuckPerms installed successfully!'); return false;" class="btn-install">Install</a>
                    </div>
                    <div class="plugin-card">
                        <div><h4>WorldEdit</h4><p>In-game structural editing and design toolkit.</p></div>
                        <a href="#" onclick="alert('WorldEdit installed successfully!'); return false;" class="btn-install">Install</a>
                    </div>
                    <div class="plugin-card">
                        <div><h4>EssentialsX</h4><p>Core utility commands (/tpa, /home, /warp).</p></div>
                        <a href="#" onclick="alert('EssentialsX installed successfully!'); return false;" class="btn-install">Install</a>
                    </div>
                    <div class="plugin-card">
                        <div><h4>AuthMe</h4><p>Robust password protection for player accounts.</p></div>
                        <a href="#" onclick="alert('AuthMe installed successfully!'); return false;" class="btn-install">Install</a>
                    </div>
                </div>

            {% elif server and active_tab == 'network' %}
                <div class="panel-box">
                    <h3>Dedicated Network Endpoints</h3>
                    <p style="color: #94a3b8; font-size: 14px; margin-bottom: 15px;">Local connection string for this node:</p>
                    <label style="display:block; margin-bottom:5px; color:#94a3b8;">Local Address & Port</label>
                    <div class="data-display">127.0.0.1:255{{ index + 65 }}</div>
                    <button onclick="alert('Port reallocation successful!');" class="btn-create" style="background:#10b981; color:#0b0f19; padding:10px 20px; border:none; border-radius:8px; font-weight:700; cursor:pointer;">Allocate New Port</button>
                </div>

            {% elif server and active_tab == 'settings' %}
                <div class="panel-box">
                    <h3>Instance Configuration Settings</h3>
                    <div style="margin-bottom: 15px;">
                        <label style="display:block; margin-bottom:8px; color:#94a3b8;">Server Name</label>
                        <input type="text" value="{{ server.name }}" style="width:100%; padding:14px; background:#0b0f19; border:1px solid rgba(255,255,255,0.12); border-radius:10px; color:#fff;" disabled>
                    </div>
                    <div style="margin-bottom: 22px;">
                        <label style="display:block; margin-bottom:8px; color:#94a3b8;">Engine Version</label>
                        <input type="text" value="{{ server.version }}" style="width:100%; padding:14px; background:#0b0f19; border:1px solid rgba(255,255,255,0.12); border-radius:10px; color:#fff;" disabled>
                    </div>
                    <button onclick="alert('Settings updated successfully!');" class="btn-create" style="background:#10b981; color:#0b0f19; padding:10px 20px; border:none; border-radius:8px; font-weight:700; cursor:pointer;">Save Changes</button>
                </div>

            {% else %}
                <div class="create-box">
                    <h3>Deploy New Minecraft Game Server</h3>
                    <form action="/create-server" method="POST">
                        <div class="form-row">
                            <div class="form-group">
                                <label>Server Identifier</label>
                                <input type="text" name="servername" placeholder="e.g. MySurvivalSMP" required>
                            </div>
                            <div class="form-group">
                                <label>Engine & Version</label>
                                <select name="version">
                                    <option value="PaperMC 1.20.4">PaperMC 1.20.4 (Recommended)</option>
                                    <option value="Spigot 1.19.4">Spigot 1.19.4</option>
                                    <option value="Forge 1.20.1">Forge 1.20.1 (Modded)</option>
                                    <option value="Bedrock Dedicated">Bedrock Edition (PE)</option>
                                </select>
                            </div>
                        </div>
                        <button type="submit" class="btn-create">Deploy Server Instance</button>
                    </form>
                </div>

                <h3 style="margin-bottom: 20px;">Active Deployed Servers ({{ servers|length }})</h3>
                <div class="servers-grid">
                    {% if servers %}
                        {% for index, s in enumerate(servers) %}
                        <div class="server-card">
                            <h4>{{ s.name }}</h4>
                            <div class="server-meta">Engine: {{ s.version }}</div>
                            <div class="server-meta" style="color: #10b981; font-family: monospace;">IP: 127.0.0.1:255{{ index + 65 }}</div>
                            
                            {% if s.status == 'ONLINE' %}
                                <span class="status-online">ONLINE</span>
                            {% else %}
                                <span class="status-offline">OFFLINE</span>
                            {% endif %}
                            
                            <div class="btn-action-group">
                                {% if s.status == 'ONLINE' %}
                                    <a href="/toggle-status/{{ index }}" class="btn-action btn-stop">Stop</a>
                                {% else %}
                                    <a href="/toggle-status/{{ index }}" class="btn-action btn-start">Start</a>
                                {% endif %}
                                <a href="/console/{{ index }}" class="btn-action" style="border-color: #10b981; color: #10b981;">Console</a>
                                <a href="/files/{{ index }}" class="btn-action">Files</a>
                                <a href="/plugins/{{ index }}" class="btn-action">Plugins</a>
                                <a href="/network/{{ index }}" class="btn-action">Network</a>
                                <a href="/settings/{{ index }}" class="btn-action">Settings</a>
                            </div>
                        </div>
                        {% endfor %}
                    {% else %}
                        <p style="color: #94a3b8;">No server instances running right now. Use the form above to deploy your first one!</p>
                    {% endif %}
                </div>
            {% endif %}

        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template_string(PANEL_HTML, servers=SERVERS, enumerate=enumerate, server=None)

@app.route('/create-server', methods=['POST'])
def create_server():
    s_name = request.form.get('servername')
    s_version = request.form.get('version')
    if s_name:
        SERVERS.append({'name': s_name, 'version': s_version, 'status': 'OFFLINE'})
    return redirect(url_for('dashboard'))

@app.route('/toggle-status/<int:index>')
def toggle_status(index):
    if 0 <= index < len(SERVERS):
        if SERVERS[index]['status'] == 'ONLINE':
            SERVERS[index]['status'] = 'OFFLINE'
        else:
            SERVERS[index]['status'] = 'ONLINE'
    return redirect(url_for('dashboard'))

@app.route('/console/<int:index>')
def console(index):
    if 0 <= index < len(SERVERS):
        return render_template_string(PANEL_HTML, servers=SERVERS, server=SERVERS[index], index=index, active_tab='console', page_title='Console Logs', enumerate=enumerate)
    return redirect(url_for('dashboard'))

@app.route('/files/<int:index>')
def files(index):
    if 0 <= index < len(SERVERS):
        return render_template_string(PANEL_HTML, servers=SERVERS, server=SERVERS[index], index=index, active_tab='files', page_title='File Manager', enumerate=enumerate)
    return redirect(url_for('dashboard'))

@app.route('/plugins/<int:index>')
def plugins(index):
    if 0 <= index < len(SERVERS):
        return render_template_string(PANEL_HTML, servers=SERVERS, server=SERVERS[index], index=index, active_tab='plugins', page_title='Plugins Marketplace', enumerate=enumerate)
    return redirect(url_for('dashboard'))

@app.route('/network/<int:index>')
def network(index):
    if 0 <= index < len(SERVERS):
        return render_template_string(PANEL_HTML, servers=SERVERS, server=SERVERS[index], index=index, active_tab='network', page_title='IP & Port Network', enumerate=enumerate)
    return redirect(url_for('dashboard'))

@app.route('/settings/<int:index>')
def settings(index):
    if 0 <= index < len(SERVERS):
        return render_template_string(PANEL_HTML, servers=SERVERS, server=SERVERS[index], index=index, active_tab='settings', page_title='Server Settings', enumerate=enumerate)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
