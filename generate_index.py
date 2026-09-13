import re

# Load SVG paths
with open('svg_paths.html', 'r', encoding='utf-8') as f:
    svg_paths = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VANS Electroengineerings — Global Railway Electrification & Leadership</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #0D287A;
      --primary-dark: #07174A;
      --accent: #F0821E;
      --accent-hover: #D96F11;
      --bg: #F4F7FC;
      --card-bg: #FFFFFF;
      --text: #1E293B;
      --text-muted: #5A6B8C;
      --border: #C9E1F5;
      --shadow-sm: 0 2px 6px rgba(13,40,122,0.06);
      --shadow-md: 0 10px 25px -5px rgba(13,40,122,0.12);
      --shadow-lg: 0 20px 35px -10px rgba(13,40,122,0.25);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 100%;
      height: 100%;
      font-family: 'Segoe UI', 'Inter', Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.4;
      overflow-x: hidden;
    }}

    /* Top instruction bar */
    .top-bar {{
      background: #EBF3FA;
      color: #5A6B8C;
      padding: 12px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 15px;
      border-bottom: 1px solid var(--border);
      width: 100%;
    }}
    .top-bar b {{ color: var(--primary); font-weight: 700; }}
    .btn-toggle {{
      background: var(--primary);
      color: #fff;
      border: 0;
      padding: 7px 16px;
      border-radius: 8px;
      font-weight: 600;
      cursor: pointer;
      font-size: 13.5px;
      transition: all 0.2s ease;
    }}
    .btn-toggle:hover {{ background: var(--primary-dark); transform: translateY(-1px); }}

    /* Main Full-Width Dashboard Layout */
    .dashboard {{
      width: 100%;
      margin: 0;
      padding: 24px 32px;
      display: grid;
      grid-template-columns: 1fr 680px;
      gap: 32px;
      position: relative;
    }}

    @media (max-width: 1400px) {{
      .dashboard {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Left Side: Logo, Title & Map */
    .map-section {{
      background: transparent;
      border: 0;
      border-radius: 0;
      padding: 0;
      box-shadow: none;
      position: relative;
      display: flex;
      flex-direction: column;
    }}

    .map-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      gap: 20px;
    }}

    .map-header .logo-box {{
      display: flex;
      align-items: center;
      gap: 16px;
      text-decoration: none;
    }}

    .map-header .logo-box img {{
      height: 162px;
      width: auto;
      object-fit: contain;
    }}

    .main-title {{
      text-align: center;
      flex: 1;
    }}

    .main-title h1 {{
      font-family: Arial, Helvetica, sans-serif;
      font-size: 42px;
      font-weight: 800;
      color: #0D2478;
      letter-spacing: -0.5px;
      line-height: 1.1;
    }}

    .main-title h1 span {{
      color: #F26522;
    }}

    .main-title small {{
      display: block;
      text-align: center;
      font-size: 16px;
      color: #333;
      font-weight: 600;
      margin-top: 4px;
    }}

    /* SVG Map Canvas */
    .map-container {{
      position: relative;
      width: 100%;
      background: #F0F5FA;
      border-radius: 18px;
      overflow: hidden;
      border: 1px solid var(--border);
      background-image:
        linear-gradient(30deg, transparent 49.5%, rgba(0,180,220,.05) 50%, transparent 50.5%),
        linear-gradient(150deg, transparent 49.5%, rgba(0,180,220,.05) 50%, transparent 50.5%);
      background-size: 50px 50px;
    }}

    .map-container svg {{
      width: 100%;
      height: auto;
      display: block;
    }}

    .country-path {{
      stroke: #111111;
      stroke-width: 0.4;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .country-path:hover {{
      fill: #FF7A00 !important;
      stroke: #000;
      stroke-width: 1;
    }}

    .country-path.active-country {{
      fill: #FF7A00 !important;
      stroke: #0D287A;
      stroke-width: 1.5;
    }}

    .show-highlight-all .country-path {{
      stroke: #FF7A00;
      stroke-width: 1;
    }}

    /* SVG Text Labels inside Country Shapes */
    .country-label {{
      font-family: 'Segoe UI', Arial, sans-serif;
      font-size: 7px;
      font-weight: 700;
      fill: #FFFFFF;
      text-anchor: middle;
      dominant-baseline: central;
      pointer-events: none;
      paint-order: stroke fill;
      stroke: #000000;
      stroke-width: 2px;
      stroke-linejoin: round;
      letter-spacing: -0.1px;
    }}

    /* Side info panel overlay on Map */
    #info-panel {{
      position: absolute;
      top: 24px;
      right: 24px;
      width: 320px;
      background: #FFFFFF;
      border: 2px solid var(--border);
      border-radius: 18px;
      padding: 22px;
      display: none;
      box-shadow: var(--shadow-lg);
      z-index: 10;
      animation: slideIn 0.25s ease;
    }}

    @keyframes slideIn {{
      from {{ opacity: 0; transform: translateX(15px); }}
      to {{ opacity: 1; transform: translateX(0); }}
    }}

    #info-panel h2 {{ font-family: 'Outfit', sans-serif; font-size: 24px; color: var(--primary); margin-bottom: 4px; }}
    #info-panel .pct {{ font-size: 15px; color: var(--text); font-weight: 600; margin-bottom: 18px; }}

    .panel-btn {{
      display: block;
      text-decoration: none;
      background: var(--primary);
      color: #fff;
      padding: 11px 14px;
      border-radius: 9px;
      font-size: 13.5px;
      margin-bottom: 10px;
      transition: all 0.2s ease;
    }}
    .panel-btn:hover {{ background: var(--primary-dark); transform: translateY(-1px); }}
    .panel-btn.alt {{ background: var(--accent); }}
    .panel-btn.alt:hover {{ background: var(--accent-hover); }}
    .panel-btn b {{ display: block; font-size: 14.5px; margin-bottom: 2px; }}
    .panel-btn span {{ display: block; font-size: 11.5px; opacity: 0.9; line-height: 1.35; }}

    .panel-close {{
      position: absolute;
      right: 14px;
      top: 10px;
      font-size: 22px;
      color: var(--text-muted);
      cursor: pointer;
      line-height: 1;
    }}
    .panel-close:hover {{ color: var(--text); }}

    /* Right Side 2x2 Grid Sidebar */
    .sidebar {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      align-content: start;
    }}

    .panel-card {{
      background: rgba(255,255,255,0.95);
      border: 2px solid var(--border);
      border-radius: 22px;
      padding: 20px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
    }}

    .panel-card h2 {{
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: var(--primary);
      text-align: center;
      margin-bottom: 16px;
      letter-spacing: 0.5px;
      border-bottom: 2px solid #EBF3FA;
      padding-bottom: 8px;
    }}

    /* 2x2 Inner Grid for Products & Directors */
    .inner-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      flex: 1;
    }}

    /* Cards Inside Panels */
    .item-card {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 10px;
      text-decoration: none;
    }}

    .item-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--primary);
    }}

    .item-card img {{
      width: 100%;
      height: 95px;
      object-fit: cover;
      border-radius: 10px;
      margin-bottom: 8px;
    }}

    .item-card.director img {{
      width: 90px;
      height: 90px;
      border-radius: 50%;
      object-fit: cover;
      border: 2.5px solid var(--primary);
    }}

    .item-card .card-title {{
      font-family: 'Outfit', sans-serif;
      color: var(--primary);
      font-weight: 700;
      font-size: 12.5px;
      line-height: 1.25;
      text-transform: uppercase;
    }}

    .item-card .card-subtitle {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 3px;
    }}

    /* Large Banner Cards for Secured Market & Opportunity */
    .full-card {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 8px;
      text-decoration: none;
      flex: 1;
    }}

    .full-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--accent);
    }}

    .full-card img {{
      width: 100%;
      height: 170px;
      object-fit: cover;
      border-radius: 10px;
    }}

    /* Modals & Backdrop */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(13,40,122,0.45);
      backdrop-filter: blur(4px);
      display: none;
      z-index: 100;
    }}

    .modal-dialog {{
      position: fixed;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      width: min(880px, 94vw);
      max-height: 92vh;
      overflow-y: auto;
      background: #FFFFFF;
      border-radius: 20px;
      padding: 36px 40px;
      display: none;
      z-index: 101;
      box-shadow: var(--shadow-lg);
      animation: modalFade 0.25s ease;
    }}

    @keyframes modalFade {{
      from {{ opacity: 0; transform: translate(-50%, -46%); }}
      to {{ opacity: 1; transform: translate(-50%, -50%); }}
    }}

    .modal-dialog .close-modal {{
      position: absolute;
      right: 20px;
      top: 16px;
      font-size: 28px;
      color: var(--text-muted);
      cursor: pointer;
    }}
    .modal-dialog .close-modal:hover {{ color: var(--primary); }}

    .modal-dialog img.profile-pic {{
      width: 130px;
      height: 130px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid var(--primary);
      display: block;
      margin: 0 auto 16px auto;
    }}

    .modal-dialog h2 {{ font-family: 'Outfit', sans-serif; font-size: 28px; color: var(--primary); margin-bottom: 6px; }}
    .modal-dialog .role {{ color: var(--accent); font-weight: 700; font-size: 16px; margin-bottom: 6px; }}
    .modal-dialog .meta {{ color: var(--text-muted); font-size: 14px; margin-bottom: 20px; }}

    .modal-dialog h3 {{
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      color: var(--primary);
      margin: 22px 0 10px;
      border-bottom: 2px solid #E2E8F0;
      padding-bottom: 6px;
    }}

    .modal-dialog p, .modal-dialog li {{ font-size: 14.5px; line-height: 1.6; color: var(--text); }}
    .modal-dialog ul {{ padding-left: 20px; margin-bottom: 12px; }}
    .modal-dialog .cols {{ display: flex; gap: 24px; flex-wrap: wrap; }}
    .modal-dialog .cols > div {{ flex: 1 1 300px; }}

    .modal-dialog .pdf-link {{
      display: inline-block;
      margin-top: 24px;
      background: var(--primary);
      color: #fff;
      text-decoration: none;
      padding: 12px 20px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 600;
      transition: all 0.2s ease;
    }}
    .modal-dialog .pdf-link:hover {{ background: var(--primary-dark); }}

    /* Footer */
    footer {{
      background: var(--primary);
      color: #fff;
      text-align: center;
      padding: 20px;
      font-size: 14px;
      border-top: 3px solid var(--accent);
      margin-top: 30px;
    }}
    footer a {{ color: #FFA34D; text-decoration: none; font-weight: 600; }}
    footer a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>

  <!-- Top Announcement / Instruction Bar -->
  <header class="top-bar">
    <div>
      <b>Click any country on the map...</b> Two options open: railway information, and electricity generation by primary energy source.
    </div>
    <button class="btn-toggle" onclick="toggleHighlights()">Show Clickable Areas</button>
  </header>

  <!-- Main Dashboard Container -->
  <div class="dashboard">

    <!-- Left Main Section: Logo, Title & Real Interactive SVG Map -->
    <main class="map-section">
      <div class="map-header">
        <a href="https://vanselectroengineerings.com/" target="_blank" rel="noopener" class="logo-box">
          <img src="img/vans-logo.png" alt="VANS Electro Logo">
        </a>

        <div class="main-title">
          <h1>Electrification of <span>Railway Network</span></h1>
          <small>(% of total route)</small>
        </div>
      </div>

      <!-- SVG Map Canvas -->
      <div class="map-container" id="mapContainer">
        <svg viewBox="0 0 1000 500" id="worldMap">
{svg_paths}
        </svg>

        <!-- Side Info Panel Overlay -->
        <div id="info-panel">
          <span class="panel-close" onclick="hidePanel()">&times;</span>
          <div id="panel-body"></div>
        </div>
      </div>
    </main>

    <!-- Right Sidebar 2x2 Panel Grid -->
    <aside class="sidebar">

      <!-- Panel 1: PRODUCTS -->
      <section class="panel-card">
        <h2>PRODUCTS</h2>
        <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
          <img src="img/prods.png" alt="Products" style="width: 100%; height: auto; max-height: 280px; object-fit: contain; border-radius: 12px;">
        </div>
      </section>

      <!-- Panel 2: DIRECTORS -->
      <section class="panel-card">
        <h2>DIRECTORS</h2>
        <div class="inner-grid">
          <div class="item-card director" onclick="openProfile(0)">
            <img src="img/abhishek saraf.jpg" alt="Abhishek Saraff">
            <div class="card-title">ABHISHEK SARAFF</div>
            <div class="card-subtitle">MD - Avadh Rail</div>
          </div>
          <div class="item-card director" onclick="openProfile(1)">
            <img src="img/srinivas (1).jpg" alt="B. Srinivasan">
            <div class="card-title">B. SRINIVASAN</div>
            <div class="card-subtitle">MD - VANS Electro</div>
          </div>
          <div class="item-card director" onclick="openProfile(2)">
            <img src="img/images.jpg" alt="Nitin Jain">
            <div class="card-title">NITIN JAIN</div>
            <div class="card-subtitle">JMD - Concord</div>
          </div>
          <div class="item-card director" onclick="openProfile(3)">
            <img src="img/VIRAJ.jpg" alt="Viraj Bansal">
            <div class="card-title">VIRAJ BANSAL</div>
            <div class="card-subtitle">JMD - VANS Electro</div>
          </div>
        </div>
      </section>

      <!-- Panel 3: SECURED VANS MARKET -->
      <section class="panel-card" onclick="openOppModal()" style="cursor: pointer;">
        <h2>SECURED VANS MARKET</h2>
        <img src="img/vansopp.jpg" alt="VANS Opportunity Plan" style="width: 100%; height: 175px; object-fit: cover; border-radius: 12px; margin-bottom: 8px;">
        <div class="card-title" style="text-align: center;">VANS OPPORTUNITY PLAN</div>
      </section>

      <!-- Panel 4: UPCOMING PRODUCTS -->
      <section class="panel-card">
        <h2>UPCOMING PRODUCTS</h2>
        <div style="display: flex; gap: 12px; height: 100%;">
          <a href="https://pdf.ac/0ZBhKy-Qy0" target="_blank" rel="noopener" class="item-card" style="flex: 1;">
            <img src="img/prod_rmu.png" alt="Ring Main Unit Market Report">
            <div class="card-title">RING MAIN<br>UNIT (RMU)</div>
          </a>
          <a href="https://pdf.ac/vtUxD0t9D" target="_blank" rel="noopener" class="item-card" style="flex: 1;">
            <img src="img/prod_vaccuminterpreter.png" alt="Vacuum Interrupter Market Report">
            <div class="card-title">VACUUM<br>INTERRUPTER</div>
          </a>
        </div>
      </section>

    </aside>

  </div>

  <!-- Footer -->
  <footer>
    <p>&copy; 2026 VANS Electroengineerings Limited. All rights reserved. Visit <a href="https://vanselectroengineerings.com/" target="_blank">vanselectroengineerings.com</a></p>
  </footer>

  <!-- Modal Backdrop & Dialogs -->
  <div class="modal-overlay" id="modal-overlay"></div>

  <!-- Opportunity Plan Modal -->
  <div class="modal-dialog" id="opp-modal" style="text-align: center;">
    <span class="close-modal" onclick="closeModal()">&times;</span>
    <h2 style="margin-bottom: 20px;">VANS Opportunity Plan</h2>
    <div style="overflow-y: auto; max-height: 70vh; border-radius: 12px; background: #f8fafc; padding: 12px;">
      <img src="img/vansopp.jpg" alt="VANS Opportunity Plan" style="width: 100%; height: auto; display: block; border-radius: 10px; margin: 0 auto;">
    </div>
  </div>

  <!-- Director Profile 0: Abhishek Saraff -->
  <div class="modal-dialog" id="prof0">
    <span class="close-modal" onclick="closeModal()">&times;</span>
    <img src="img/abhishek saraf.jpg" alt="Abhishek Saraff" class="profile-pic">
    <h2>Abhishek Saraff</h2>
    <p class="role">Managing Director, Avadh Rail Infra Ltd.<br>Chairman, CII Uttar Pradesh (2025&ndash;26)</p>
    <p class="meta">Academic background: M.S. in International Business, University of Kansas, USA (2001)</p>

    <h3>Executive Summary</h3>
    <p>Industrial leader and Managing Director of Avadh Rail Infra Ltd., with executive leadership experience across rail infrastructure and engineering. Under his leadership the group achieved roughly 500% growth, with annual sales reaching nearly &#8377;600 crore, turning Avadh Rail Infra Ltd. into an integrated, technology-led rail solutions provider.</p>

    <h3>Core Sectoral Expertise</h3>
    <div class="cols">
      <div>
        <b>Railway Infrastructure &amp; Operations</b>
        <ul>
          <li>Critical and safety-critical components for Indian Railways</li>
          <li>Rolling stock, overhead electrification (OHE) and track systems</li>
          <li>Semi-high-speed, high-speed and metro rail infrastructure</li>
          <li>Integrated rail solutions and civil infrastructure</li>
        </ul>
      </div>
      <div>
        <b>Strategic Growth &amp; Global Business</b>
        <ul>
          <li>Global partnerships across USA, Germany, France, China, Russia, and Australia</li>
          <li>Enterprise scale-up and diversification (~&#8377;600 Cr revenue)</li>
          <li>Operational excellence and technology integration</li>
          <li>Corporate leadership and multi-enterprise governance</li>
        </ul>
      </div>
    </div>

    <h3>Leadership &amp; Executive Experience</h3>
    <p><b>Avadh Rail Infra Ltd.</b> &mdash; Managing Director (present)</p>
    <ul>
      <li>Leads corporate strategy, manufacturing operations, technology adoption, and overall group expansion for a trusted rail infrastructure manufacturer established in 1977.</li>
      <li>Engineered a ~500% business expansion, taking group annual revenue to nearly &#8377;600 crore through strategic diversification across Rolling Stock, OHE, Track, and Civil Infrastructure.</li>
      <li>Fosters international technology transfers and joint collaborations with partners in the USA, Germany, France, China, Russia, and Australia.</li>
    </ul>

    <p><b>Confederation of Indian Industry (CII) - Uttar Pradesh</b> &mdash; Chairman (2025&ndash;2026)</p>
    <ul>
      <li>Leads industrial strategy, policy advocacy, and economic engagement across regional infrastructure and engineering sectors in Uttar Pradesh.</li>
    </ul>

    <h3>Group Umbrella Enterprises &amp; Education</h3>
    <div class="cols">
      <div>
        <b>Education &amp; Qualifications</b>
        <ul><li>M.S. in International Business, University of Kansas, USA (2001)</li></ul>
      </div>
      <div>
        <b>Group Umbrella Enterprises</b>
        <ul style="list-style-type: none; padding-left: 0;">
          <li style="margin-bottom: 6px;"><a href="http://www.novius.co.in" target="_blank" rel="noopener" style="color: #0D287A; text-decoration: none; font-weight: 600;">Novius Technologies India Pvt. Ltd. &rarr;</a></li>
          <li style="margin-bottom: 6px;"><a href="http://www.avadhtechnometals.com" target="_blank" rel="noopener" style="color: #0D287A; text-decoration: none; font-weight: 600;">Avadh Technometals Pvt. Ltd. &rarr;</a></li>
          <li style="margin-bottom: 6px;"><a href="http://www.vanselectroengineerings.com" target="_blank" rel="noopener" style="color: #0D287A; text-decoration: none; font-weight: 600;">VANS Electroengineerings &rarr;</a></li>
          <li style="margin-bottom: 6px;"><a href="https://www.linkedin.com/company/atpl-lko/?originalSubdomain=in" target="_blank" rel="noopener" style="color: #0D287A; text-decoration: none; font-weight: 600;">Atlantic Tradeengineers LLP &rarr;</a></li>
          <li style="margin-bottom: 6px;"><a href="http://www.pullman.in" target="_blank" rel="noopener" style="color: #0D287A; text-decoration: none; font-weight: 600;">Pullman Engineering Co. Pvt. Ltd. &rarr;</a></li>
          <li style="margin-bottom: 6px;"><a href="http://www.primaxequipment.com" target="_blank" rel="noopener" style="color: #0D287A; text-decoration: none; font-weight: 600;">Primax Industry Pvt. Ltd. &rarr;</a></li>
        </ul>
      </div>
    </div>

    <a class="pdf-link" target="_blank" rel="noopener" href="pdf/Abhishek_Saraff_Executive_Profile_Vans_Background.pdf">Download Executive Profile PDF</a>
  </div>

  <!-- Director Profile 1: B. Srinivasan -->
  <div class="modal-dialog" id="prof1">
    <span class="close-modal" onclick="closeModal()">&times;</span>
    <img src="img/srinivas (1).jpg" alt="B. Srinivasan" class="profile-pic">
    <h2>B. Srinivasan</h2>
    <p class="role">Managing Director, VANS Electroengineerings Limited<br>MV Switchgear Specialist &amp; Innovator</p>
    <p class="meta">Age: 58 Years | Industry Experience: 25+ Years | Qualification: B.Sc. (Electronics), MBA (International Business)</p>

    <h3>Executive Summary</h3>
    <p>Seasoned executive and technological leader with extensive expertise in research &amp; development, detailed engineering, prototype manufacturing, type testing, production, installation, and commissioning of medium voltage switchgear (AIS &amp; GIS) ranging from 3.3 kV to 40.5 kV. Successfully heading a medium voltage switchgear manufacturing enterprise in Salem, Tamil Nadu for over 11 years.</p>

    <h3>Technical Expertise &amp; Switchgear Solutions</h3>
    <div class="cols">
      <div>
        <b>Medium Voltage Switchgear &amp; Actuators</b>
        <ul>
          <li>AIS &amp; GIS Vacuum Circuit Breakers, Load Break Switches, Off-load Isolators, Earth Switches (3.3 kV to 40.5 kV).</li>
          <li>Permanent Magnetic Actuator Operated Vacuum Circuit Breakers, Auto Reclosers, Sectionalisers, and Special VCBs for Capacitor Switching.</li>
        </ul>
      </div>
      <div>
        <b>Protection &amp; Heavy Duty Breakers</b>
        <ul>
          <li>Control &amp; Relay Panels, Metal-clad Indoor/Outdoor VCB Switchboards, High Voltage Motor Starters, Vacuum Contactors, Generator Circuit Breakers, and Traction Breakers.</li>
        </ul>
      </div>
    </div>

    <h3>Leadership &amp; Key Achievements</h3>
    <ul>
      <li><b>Managing Director (11+ Years):</b> Heading a premier medium voltage switchgear manufacturing industry based in Salem, Tamil Nadu.</li>
      <li><b>Patents &amp; Innovations:</b> Filed 7 Patents related to distribution automation and electrical safety solutions.</li>
    </ul>

    <a class="pdf-link" target="_blank" rel="noopener" href="pdf/B_Srinivasan_Executive_Profile_Vans_Logo_v5.pdf">Download Executive Profile PDF</a>
  </div>

  <!-- Director Profile 2: Nitin Jain -->
  <div class="modal-dialog" id="prof2">
    <span class="close-modal" onclick="closeModal()">&times;</span>
    <img src="img/images.jpg" alt="Nitin Jain" class="profile-pic">
    <h2>Nitin Jain</h2>
    <p class="role">Mechanical Engineer | Visionary Entrepreneur | Executive Director<br>DIN: 03385362 | Company: Concord Control Systems Limited</p>
    <p class="meta">Qualifications: Bachelor of Engineering (Mechanical Engineering), Siddaganga Institute of Technology, Tumkur</p>

    <h3>Executive Summary</h3>
    <p>Visionary founder, Promoter, and Joint Managing Director of Concord Control Systems Limited with decades of profound expertise in mechanical engineering. A highly committed, success-driven leader dedicated to advancing national infrastructure through top-notch engineering and client-focused product innovation. Proven track record in providing strategic direction, setting long-term organizational goals, guiding multi-disciplinary teams to achieve rigorous industry benchmarks.</p>

    <h3>Core Sectoral Expertise &amp; Capabilities</h3>
    <div class="cols">
      <div>
        <b>Strategic Leadership &amp; Governance</b>
        <ul>
          <li>Long-Term Corporate &amp; Strategic Planning</li>
          <li>Board Governance &amp; Regulatory Compliance</li>
          <li>Promoter &amp; Executive Management</li>
          <li>Cross-Functional Team Mentorship &amp; Guidance</li>
        </ul>
      </div>
      <div>
        <b>Mechanical Engineering &amp; Product Innovation</b>
        <ul>
          <li>Advanced Mechanical Engineering Solutions</li>
          <li>Client-Centric Product Development</li>
          <li>Quality Benchmarking &amp; Process Standardization</li>
          <li>Professional Communication &amp; Client Relations</li>
        </ul>
      </div>
    </div>

    <h3>Leadership &amp; Professional Experience</h3>
    <p><b>Concord Control Systems Limited</b> &mdash; Joint Managing Director | Founder &amp; Promoter (DIN: 03385362)</p>
    <ul>
      <li>Spearheads long-term strategic goal setting, organizational vision, and corporate governance for high-precision manufacturing operations.</li>
      <li>Leads product innovation and mechanical engineering development to consistently exceed client expectations with high-quality market offerings.</li>
      <li>Directs and mentors engineering and operational teams to maintain top-tier industry benchmarks, professionalism, and effective communication.</li>
      <li>Ensures full compliance with corporate and regulatory frameworks, including SEBI Listing Obligations and Disclosure Requirements (LODR).</li>
    </ul>

    <a class="pdf-link" target="_blank" rel="noopener" href="pdf/Nitin_Jain_Executive_Profile_Vans_Background-v3.pdf">Download Executive Profile PDF</a>
  </div>

  <!-- Director Profile 3: Viraj Bansal -->
  <div class="modal-dialog" id="prof3">
    <span class="close-modal" onclick="closeModal()">&times;</span>
    <img src="img/VIRAJ.jpg" alt="Viraj Bansal" class="profile-pic">
    <h2>Viraj Bansal</h2>
    <p class="role">Electrical &amp; Electronics Engineer | Entrepreneur | Industrial Executive<br>Joint Managing Director, Vans Electroengineerings Limited</p>
    <p class="meta">Education: M.Sc. (University of Warwick, UK) | B.Tech. (VIT, India) | Location: South Delhi, India</p>

    <h3>Executive Summary</h3>
    <p>Dynamic entrepreneur and business management professional with over 6 years of leadership experience across railway infrastructure, switchgear manufacturing, vacuum circuit breaker production, foundry operations, engineering diagnostics, and industrial business management. Currently holds key directorship and executive roles across multiple enterprises within the Hotspot Group, overseeing corporate business strategy, plant operations, global market expansion, and internal marketing.</p>

    <h3>Leadership &amp; Executive Experience</h3>
    <p><b>Vans Electroengineerings Limited</b> &mdash; Joint Managing Director (since June 2026); Director (August 2024 &ndash; present)</p>
    <ul>
      <li>Spearheads corporate strategy, operations and governance across sales and marketing, finance, supply chain management, logistics and legal.</li>
      <li>Drives manufacturing and technical innovation for specialised 2&times;25 kV vacuum circuit breakers and power distribution protection systems for railway traction.</li>
      <li>Builds technology partnerships, product commercialisation and expansion across domestic and international infrastructure markets.</li>
    </ul>

    <p><b>Avadh Technometals Private Limited</b> &mdash; Director &amp; CEO (February 2023 &ndash; present)</p>
    <ul>
      <li>Runs operations and expansion of a Class-A foundry in Haridwar producing up to 450 MT/month of precision-engineered components.</li>
      <li>Led production of coach and locomotive castings supplied to Indian Railways, defence, automotive and heavy industrial sectors.</li>
    </ul>

    <a class="pdf-link" target="_blank" rel="noopener" href="pdf/Viraj_Bansal_Executive_Profile_With_Photo_v2.pdf">Download Executive Profile PDF</a>
  </div>

  <!-- JavaScript Interaction Logic -->
  <script>
    const INFO = {{
      'Greenland': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Greenland', op: null, energy: 'https://ourworldindata.org/profile/energy/greenland' }},
      'Canada': {{ pct: '0.2%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Canada', op: 'VIA Rail', energy: 'https://ourworldindata.org/profile/energy/canada' }},
      'United States': {{ pct: '1%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_the_United_States', op: 'Amtrak', energy: 'https://ourworldindata.org/profile/energy/united-states' }},
      'Mexico': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mexico', op: null, energy: 'https://ourworldindata.org/profile/energy/mexico' }},
      'Venezuela': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Venezuela', op: null, energy: 'https://ourworldindata.org/profile/energy/venezuela' }},
      'Colombia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Colombia', op: null, energy: 'https://ourworldindata.org/profile/energy/colombia' }},
      'Brazil': {{ pct: '30%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Brazil', op: 'VALE / Rumo', energy: 'https://ourworldindata.org/profile/energy/brazil' }},
      'Bolivia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Bolivia', op: null, energy: 'https://ourworldindata.org/profile/energy/bolivia' }},
      'Paraguay': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Paraguay', op: null, energy: 'https://ourworldindata.org/profile/energy/paraguay' }},
      'Argentina': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Argentina', op: null, energy: 'https://ourworldindata.org/profile/energy/argentina' }},
      'Algeria': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Algeria', op: null, energy: 'https://ourworldindata.org/profile/energy/algeria' }},
      'Libya': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Libya', op: null, energy: 'https://ourworldindata.org/profile/energy/libya' }},
      'Mauritania': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mauritania', op: null, energy: 'https://ourworldindata.org/profile/energy/mauritania' }},
      'Mali': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mali', op: null, energy: 'https://ourworldindata.org/profile/energy/mali' }},
      'Niger': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Niger', op: null, energy: 'https://ourworldindata.org/profile/energy/niger' }},
      'Chad': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Chad', op: null, energy: 'https://ourworldindata.org/profile/energy/chad' }},
      'Nigeria': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Nigeria', op: null, energy: 'https://ourworldindata.org/profile/energy/nigeria' }},
      'Central African Republic': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_the_Central_African_Republic', op: null, energy: 'https://ourworldindata.org/profile/energy/central-african-republic' }},
      'Democratic Republic of the Congo': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_the_Democratic_Republic_of_the_Congo', op: null, energy: 'https://ourworldindata.org/profile/energy/democratic-republic-of-congo' }},
      'Angola': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Angola', op: null, energy: 'https://ourworldindata.org/profile/energy/angola' }},
      'Namibia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Namibia', op: null, energy: 'https://ourworldindata.org/profile/energy/namibia' }},
      'Egypt': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Egypt', op: null, energy: 'https://ourworldindata.org/profile/energy/egypt' }},
      'Sudan': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Sudan', op: null, energy: 'https://ourworldindata.org/profile/energy/sudan' }},
      'Ethiopia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Ethiopia', op: null, energy: 'https://ourworldindata.org/profile/energy/ethiopia' }},
      'Kenya': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Kenya', op: null, energy: 'https://ourworldindata.org/profile/energy/kenya' }},
      'Tanzania': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Tanzania', op: null, energy: 'https://ourworldindata.org/profile/energy/tanzania' }},
      'Zambia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Zambia', op: null, energy: 'https://ourworldindata.org/profile/energy/zambia' }},
      'Zimbabwe': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Zimbabwe', op: null, energy: 'https://ourworldindata.org/profile/energy/zimbabwe' }},
      'Mozambique': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mozambique', op: null, energy: 'https://ourworldindata.org/profile/energy/mozambique' }},
      'Madagascar': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Madagascar', op: null, energy: 'https://ourworldindata.org/profile/energy/madagascar' }},
      'Turkey': {{ pct: '100%', wiki: 'https://en.wikipedia.org/wiki/State_Railways_of_the_Republic_of_Turkey', op: 'TCDD', energy: 'https://ourworldindata.org/profile/energy/turkey' }},
      'Syria': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Syria', op: null, energy: 'https://ourworldindata.org/profile/energy/syria' }},
      'Iraq': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Iraq', op: null, energy: 'https://ourworldindata.org/profile/energy/iraq' }},
      'Saudi Arabia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Saudi_Arabia', op: null, energy: 'https://ourworldindata.org/profile/energy/saudi-arabia' }},
      'Yemen': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Yemen', op: null, energy: 'https://ourworldindata.org/profile/energy/yemen' }},
      'Iran': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Iran', op: null, energy: 'https://ourworldindata.org/profile/energy/iran' }},
      'Afghanistan': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Afghanistan', op: null, energy: 'https://ourworldindata.org/profile/energy/afghanistan' }},
      'Pakistan': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Pakistan', op: null, energy: 'https://ourworldindata.org/profile/energy/pakistan' }},
      'India': {{ pct: '99%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_India', op: 'Indian Railways', energy: 'https://ourworldindata.org/profile/energy/india' }},
      'Kazakhstan': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Kazakhstan', op: null, energy: 'https://ourworldindata.org/profile/energy/kazakhstan' }},
      'Mongolia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mongolia', op: null, energy: 'https://ourworldindata.org/profile/energy/mongolia' }},
      'China': {{ pct: '75%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_China', op: 'China State Railway', energy: 'https://ourworldindata.org/profile/energy/china' }},
      'Russia': {{ pct: '51%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Russia', op: 'Russian Railways', energy: 'https://ourworldindata.org/profile/energy/russia' }},
      'Myanmar': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Myanmar', op: null, energy: 'https://ourworldindata.org/profile/energy/myanmar' }},
      'Thailand': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Thailand', op: null, energy: 'https://ourworldindata.org/profile/energy/thailand' }},
      'Cambodia': {{ pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Cambodia', op: null, energy: 'https://ourworldindata.org/profile/energy/cambodia' }},
      'Australia': {{ pct: '33%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Australia', op: null, energy: 'https://ourworldindata.org/profile/energy/australia' }},
      'United Kingdom': {{ pct: '38%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Great_Britain', op: 'Network Rail', energy: 'https://ourworldindata.org/profile/energy/united-kingdom' }},
      'France': {{ pct: '58%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_France', op: 'SNCF', energy: 'https://ourworldindata.org/profile/energy/france' }},
      'Spain': {{ pct: '68%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Spain', op: 'Renfe', energy: 'https://ourworldindata.org/profile/energy/spain' }},
      'Germany': {{ pct: '62%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Germany', op: 'Deutsche Bahn', energy: 'https://ourworldindata.org/profile/energy/germany' }},
      'Poland': {{ pct: '64%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Poland', op: 'PKP', energy: 'https://ourworldindata.org/profile/energy/poland' }},
      'Sweden': {{ pct: '75%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Sweden', op: 'Trafikverket', energy: 'https://ourworldindata.org/profile/energy/sweden' }}
    }};

    const OPERATOR_URLS = {{
      'Indian Railways': 'https://indianrailways.gov.in/',
      'Amtrak': 'https://www.amtrak.com/',
      'SNCF': 'https://www.sncf.com/',
      'Renfe': 'https://www.renfe.com/',
      'Deutsche Bahn': 'https://www.bahn.com/',
      'PKP': 'https://www.pkp.pl/',
      'TCDD': 'https://www.tcdd.gov.tr/',
      'Russian Railways': 'https://www.rzd.ru/',
      'China State Railway': 'http://www.china-railway.com.cn/',
      'VIA Rail': 'https://www.viarail.ca/',
      'Network Rail': 'https://www.networkrail.co.uk/',
      'Trafikverket': 'https://www.trafikverket.se/'
    }};

    // Handle Map Clicks
    document.querySelectorAll('.country-path').forEach(el => {{
      el.addEventListener('click', function(e) {{
        e.stopPropagation();
        const country = this.getAttribute('data-c');
        const d = INFO[country] || {{
          pct: 'No figure on this map',
          wiki: 'https://en.wikipedia.org/wiki/Special:Search?search=' + encodeURIComponent('Rail transport in ' + country),
          op: null,
          energy: 'https://ourworldindata.org/profile/energy/' + encodeURIComponent(country.toLowerCase().replace(/\s+/g, '-'))
        }};

        // Active highlight styling
        document.querySelectorAll('.country-path').forEach(p => p.classList.remove('active-country'));
        this.classList.add('active-country');

        const pctText = (d.pct === 'No figure on this map' || d.pct === null)
          ? 'No figure on this map'
          : (d.pct.includes('%') ? d.pct + ' of route electrified' : d.pct);

        const opLink = (d.op && OPERATOR_URLS[d.op])
          ? `<a class="panel-btn" target="_blank" rel="noopener" href="${{OPERATOR_URLS[d.op]}}"><b>2 &nbsp; National operator &mdash; ${{d.op}}</b><span>Official network operator site \u2197</span></a>`
          : (d.op ? `<div class="panel-btn"><b>2 &nbsp; Operator &mdash; ${{d.op}}</b></div>` : '');

        const panelBody = document.getElementById('panel-body');
        panelBody.innerHTML = `
          <h2>${{country}}</h2>
          <p class="pct">${{pctText}}</p>
          <a class="panel-btn" target="_blank" rel="noopener" href="${{d.wiki}}"><b>1 &nbsp; Railway information</b><span>Network, operators, electrification and history \u2197</span></a>
          ${{opLink}}
          <a class="panel-btn alt" target="_blank" rel="noopener" href="${{d.energy}}"><b>2 &nbsp; Electricity generation</b><span>Breakdown by primary energy source: coal, gas, oil, nuclear, hydro, wind, solar \u2197</span></a>
        `;
        document.getElementById('info-panel').style.display = 'block';
      }});
    }});

    function hidePanel() {{
      document.getElementById('info-panel').style.display = 'none';
      document.querySelectorAll('.country-path').forEach(p => p.classList.remove('active-country'));
    }}

    function toggleHighlights() {{
      document.getElementById('mapContainer').classList.toggle('show-highlight-all');
    }}

    // Modal Controls
    function closeModal() {{
      document.getElementById('modal-overlay').style.display = 'none';
      document.querySelectorAll('.modal-dialog').forEach(m => m.style.display = 'none');
    }}

    document.getElementById('modal-overlay').addEventListener('click', closeModal);

    function openProfile(idx) {{
      closeModal();
      document.getElementById('modal-overlay').style.display = 'block';
      document.getElementById('prof' + idx).style.display = 'block';
    }}

    function openOppModal() {{
      closeModal();
      document.getElementById('modal-overlay').style.display = 'block';
      document.getElementById('opp-modal').style.display = 'block';
    }}
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as out:
    out.write(html_content)

print('Successfully generated complete index.html')
