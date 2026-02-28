<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>BLACK PANTHER RULEX</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
    body {
      margin: 0;
      padding: 0;
      font-family: 'Orbitron', sans-serif;
      background: url('https://i.ibb.co/wr33j97F/4a7ee02d696989870ddb8789e49f1841.jpg') no-repeat center center fixed;
      background-size: cover;
      color: #fff;
      overflow-x: hidden;
      position: relative;
    }
    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0;
      height: 100%;
      width: 100%;
      background: url('https://i.ibb.co/dJ9Zr9v/smoke.gif') center/cover no-repeat;
      opacity: 0.03;
      pointer-events: none;
      z-index: 0;
      animation: fogMove 60s linear infinite;
    }
    @keyframes fogMove { 0% { background-position: 0 0; } 100% { background-position: 100% 100%; } }

    /* ===== LOGIN SCREEN ===== */
    .login-screen {
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(0,0,0,0.85);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
      flex-direction: column;
      animation: fadeIn 1s ease;
    }
    .login-box {
      background: #111;
      padding: 40px;
      border: 2px solid crimson;
      border-radius: 15px;
      text-align: center;
      box-shadow: 0 0 25px crimson;
      animation: glowBox 1.5s infinite alternate;
    }
    .login-box h2 {
      color: crimson;
      font-size: 2em;
      margin-bottom: 20px;
      animation: neonGlow 2s infinite alternate;
    }
    .input-wrapper { position: relative; width: 100%; }
    .login-box input {
      padding: 12px;
      width: 100%;
      font-size: 1em;
      border-radius: 10px;
      border: none;
      outline: none;
      margin-bottom: 20px;
      background: #222;
      color: #fff;
      box-shadow: 0 0 10px crimson;
    }
    .toggle-visibility {
      position: absolute; right: 10px; top: 12px;
      cursor: pointer; color: crimson; font-size: 1.1em;
    }
    .login-box button {
      background: crimson; color: #fff;
      padding: 10px 20px; border: none; border-radius: 10px;
      font-weight: bold; cursor: pointer; font-size: 1em;
      transition: 0.3s ease; box-shadow: 0 0 10px crimson;
    }
    .login-box button:hover { background: #ff0033; transform: scale(1.05); }
    .error-msg { color: #ff4d4d; margin-top: 10px; font-size: 0.9em; }

    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes glowBox { from { box-shadow: 0 0 15px crimson; } to { box-shadow: 0 0 25px red; } }
    @keyframes neonGlow { from { text-shadow: 0 0 10px crimson; } to { text-shadow: 0 0 20px red,0 0 30px crimson; } }

    /* ===== MAIN CONTENT ===== */
    .header { text-align:center; padding:80px 20px; background:linear-gradient(to right, #0d0d0d, #1a1a1a); animation: pulse 5s infinite alternate; }
    .header h1 {
      font-size:4em; color:crimson; text-shadow:0 0 20px crimson;
      letter-spacing:3px; animation: neonGlow 2s infinite alternate, flicker 2s infinite;
    }
    .header p { font-size:1.4em; color:#aaa; }

    @keyframes flicker { 0%,19%,21%,23%,25%,54%,56%,100% { opacity:1; } 20%,24%,55% { opacity:0.4; } }
    @keyframes pulse { 0% { background-position:0 0; } 100% { background-position:100% 100%; } }

    .team-section { padding:60px 20px; text-align:center; }
    .team-section h2 {
      color:crimson; font-size:2.5em; margin-bottom:40px;
      text-transform: uppercase; animation: glow 1.5s infinite alternate;
    }
    @keyframes glow { 0% { text-shadow:0 0 5px crimson; } 100% { text-shadow:0 0 20px crimson; } }

    .members { display:flex; flex-wrap:wrap; justify-content:center; gap:30px; }
    .member-card {
      background-color:#111; border:2px solid crimson;
      padding:20px; border-radius:15px; width:240px;
      box-shadow:0 0 20px crimson;
      transition:transform .4s, box-shadow .4s;
      position:relative;
    }
    .member-card:hover {
      transform:scale(1.07);
      box-shadow:0 0 30px red, inset 0 0 10px crimson;
      background: radial-gradient(circle at center, #1a1a1a 20%, #000 100%);
    }
    .member-card::after {
      content:'☠'; position:absolute; font-size:28px;
      color:crimson; top:-10px; right:10px;
      animation: floatSkull 2.5s infinite ease-in-out;
      opacity:0.6;
    }
    @keyframes floatSkull { 0%,100%{ transform:translateY(0); opacity:0.5; } 50%{ transform:translateY(-10px); opacity:1; } }

    .member-card h3 { margin:15px 0 10px; color:#fff; font-size:1.3em; }
    .member-card p { color:#ccc; font-size:0.9em; }
    .member-card a {
      margin-top:10px; display:inline-block; color:crimson;
      text-decoration:none; font-weight:bold;
      border:1px solid crimson; padding:5px 10px;
      border-radius:8px; transition:background .3s, transform .3s;
      animation: buttonPulse 2s infinite;
    }
    .member-card a:hover { background:crimson; color:#fff; transform:scale(1.05); }
    @keyframes buttonPulse { 0%,100%{ transform:scale(1); } 50%{ transform:scale(1.1); } }

    .modal {
      display:none; position:fixed; z-index:999;
      left:0; top:0; width:100%; height:100%;
      background-color:rgba(0,0,0,0.85);
    }
    .modal-content {
      background-color:#111; margin:10% auto;
      padding:30px; border:2px solid crimson;
      width:90%; max-width:500px;
      border-radius:15px; box-shadow:0 0 30px crimson;
      color:#fff; animation:fadeIn .5s ease-in-out, evilShake .5s;
    }
    @keyframes fadeIn { from{ transform:scale(.9); opacity:0 } to{ transform:scale(1); opacity:1 } }
    @keyframes evilShake { 0%,100%{ transform:translate(0,0) rotate(0) } 20%,60%{ transform:translate(-2px,2px) rotate(-1deg) } 40%,80%{ transform:translate(2px,-1px) rotate(1deg) } }

    .close { color:crimson; float:right; font-size:28px; font-weight:bold; cursor:pointer; }
    .close:hover { color:white; }

    .floating-evil {
      position:fixed; z-index:10; pointer-events:none;
      color:crimson; opacity:0.2;
      animation: floatEvil linear infinite;
      font-family: 'Segoe UI Emoji', sans-serif;
    }
    @keyframes floatEvil {
      0%{ transform:translateY(0) rotate(0); opacity:0.1 }
      50%{ transform:translateY(-100px) rotate(180deg); opacity:0.3 }
      100%{ transform:translateY(0) rotate(360deg); opacity:0.1 }
    }
    @keyframes intenseGlow { 0% { text-shadow:0 0 5px #ff1744,0 0 10px #ff1744; } 100%{ text-shadow:0 0 10px #ff1744,0 0 40px red; } }
  </style>
</head>
<body>

<!-- 🔐 Password Screen -->
<div class="login-screen" id="loginScreen">
  <div class="login-box">
    <h2>Enter Access Code</h2>
    <div class="input-wrapper">
      <input type="password" id="passwordInput" placeholder="Secret Password 🔐" />
      <span class="toggle-visibility" onclick="togglePassword()">👁️</span>
    </div>
    <button onclick="checkPassword()">Unlock</button>
    <div class="error-msg" id="errorMsg"></div>
  </div>
</div>

<!-- 🔓 Protected Dashboard Content -->
<div id="mainContent" style="display: none;">
  <audio autoplay loop>
    <source src="https://www.fesliyanstudios.com/play-mp3/6516" type="audio/mp3">
  </audio>
  <audio id="clickSound" src="https://www.fesliyanstudios.com/play-mp3/6963" preload="auto"></audio>

  <div class="header">
    <h1>👑💀BLACK PANTHER RULEX💀☠️</h1>
    <p>The Most Dangerous Rulex Team Ruling Facebook</p>
  </div>

  <div class="team-section">
    <h2>Owners</h2>
    <div class="members">
      <!-- Monster -->
      <div class="member-card">
        <h3>Monster</h3>
        <p>UNSTOPPABLE Server Master & Typer King</p>
        <a onclick="openModal('monster'); speakDetails(modalTexts['monster']);">View More</a>
        <a href="https://www.facebook.com/blackpantherrulexkaownerkamena" target="_blank">Visit FB</a>
      </div>
      <!-- Smarty -->
      <div class="member-card">
        <h3>Smarty</h3>
        <p>Fastest Typist & Server Developer</p>
        <a onclick="openModal('smarty'); speakDetails(modalTexts['smarty']);">View More</a>
        <a href="https://www.facebook.com/ali7s90" target="_blank">Visit FB</a>
      </div>
    </div>
  </div>

  <div class="team-section">
    <h2>Members</h2>
    <div class="members">
      <!-- Alfaz -->
      <div class="member-card">
        <h3>Alfaz</h3>
        <p>Typer & Most Popular Abuser</p>
        <a onclick="openModal('alfaz'); speakDetails(modalTexts['alfaz']);">View More</a>
        <a href="https://www.facebook.com/shakir.knak" target="_blank">Visit FB</a>
      </div>
      <!-- Rubel -->
      <div class="member-card">
        <h3>Rubel</h3>
        <p>Typer & Most Popular Abuser</p>
        <a onclick="openModal('rubel'); speakDetails(modalTexts['rubel']);">View More</a>
        <a href="https://www.facebook.com/md.rubel.1437" target="_blank">Visit FB</a>
      </div>
      <!-- Shad -->
      <div class="member-card">
        <h3>Shad</h3>
        <p>Typer & Popular Abuser</p>
        <a onclick="openModal('shad'); speakDetails(modalTexts['shad']);">View More</a>
        <a href="https://www.facebook.com/c.t.e.857766" target="_blank">Visit FB</a>
      </div>
    </div>
  </div>

  <div class="team-section">
    <h2>Tools</h2>
    <div class="members">
      <div class="member-card">
        <h3>WEB SERVER</h3>
        <p> nonstop Auto msg & spam bot for domination</p>
        <a href="https://first-server-ztz0.onrender.com" target="_blank">Open Tool</a>
      </div>
      <div class="member-card">
        <h3>Auto Typer</h3>
        <p>Fastest text typing automation system</p>
        <a href="https://example.com/auto-typer" target="_blank">Open Tool</a>
      </div>
      <div class="member-card">
        <h3>Group Raider</h3>
        <p>Join + comment flood in target groups</p>
        <a href="https://example.com/group-raider" target="_blank">Open Tool</a>
      </div>
      <div class="member-card">
        <h3>Voice Reply Bot</h3>
        <p>Replies in voice format using text-to-speech</p>
        <a href="https://example.com/voice-reply-bot" target="_blank">Open Tool</a>
      </div>
    </div>
  </div>

  <!-- Modals -->
  <div id="modal-monster" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('monster')">&times;</span>
      <h2>Monster</h2>
      <p>Leader of Black Panther RULEX, known for server domination, bot coding, and powerful Facebook spamming tools.</p>
    </div>
  </div>
  <div id="modal-smarty" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('smarty')">&times;</span>
      <h2>Smarty</h2>
      <p>Smart coder and fast typer, backbone of the team’s tool development and Facebook automation tactics.</p>
    </div>
  </div>
  <div id="modal-alfaz" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('alfaz')">&times;</span>
      <h2>Alfaz</h2>
      <p>Most aggressive abuser and comment attacker, feared across groups and known for night raids.</p>
    </div>
  </div>
  <div id="modal-rubel" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('rubel')">&times;</span>
      <h2>Rubel</h2>
      <p>Master of live trolling and viral meme spamming. Keeps the energy high and the enemies annoyed.</p>
    </div>
  </div>
  <div id="modal-shad" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('shad')">&times;</span>
      <h2>Shad</h2>
      <p>The funniest roaster in the gang, always ready to flood comments and entertain with epic burns.</p>
    </div>
  </div>

  <!-- Footer -->
  <div style="text-align:center; padding:25px 15px; background:linear-gradient(to right,#0d0d0d,#1a0000); border-top:3px solid crimson; color:#ff1744; font-weight:900; font-size:1.5em; letter-spacing:2px; font-family:'Orbitron', sans-serif; box-shadow:0 -5px 20px crimson; animation:intenseGlow 2s infinite alternate; text-transform:uppercase; position:relative; z-index:999;">
    ⚡ Made by <span style="color:white;">Monster</span> ⚡ — 2025 • <span style="color:crimson;">🌚👑</span>
  </div>
</div>

<!-- 🔐 Combined Scripts -->
<script>
  const correctPassword = "thanks monster sir";
  function checkPassword() {
    const input = document.getElementById("passwordInput").value;
    const error = document.getElementById("errorMsg");
    if (input === correctPassword) {
      document.getElementById("loginScreen").style.display = "none";
      document.getElementById("mainContent").style.display = "block";
      document.getElementById("unlockSound")?.play();
    } else {
      error.textContent = "❌ Wrong password. Try again.";
    }
  }
  function togglePassword() {
    const input = document.getElementById("passwordInput");
    const icon = document.querySelector('.toggle-visibility');
    if (input.type === "password") { input.type = "text"; icon.textContent = "🙈"; }
    else { input.type = "password"; icon.textContent = "👁️"; }
  }
  document.getElementById("passwordInput").addEventListener("keyup", e => {
    if (e.key === "Enter") checkPassword();
  });

  const modalTexts = {
    monster: "Monster. Leader of Black Panther Rulex. Known for server domination, bot coding, and powerful Facebook spamming tools.",
    smarty:  "Smarty. Smart coder and fast typer. Backbone of the team’s tool development and Facebook automation tactics.",
    alfaz:   "Alfaz. Most aggressive abuser and comment attacker. Feared across groups and known for night raids.",
    rubel:   "Rubel. Master of live trolling and viral meme spamming. Keeps the energy high and the enemies annoyed.",
    shad:    "Shad. The funniest roaster in the gang. Always ready to flood comments and entertain with epic burns."
  };
  function openModal(name) {
    document.getElementById('clickSound')?.play();
    document.getElementById("modal-"+name).style.display = "block";
  }
  function closeModal(name) {
    document.getElementById("modal-"+name).style.display = "none";
    window.speechSynthesis.cancel();
  }
  function speakDetails(text) {
    if (!window.speechSynthesis) return;
    const u = new SpeechSynthesisUtterance(text);
    u.rate = 0.9; u.pitch = 0.8; u.volume = 1; u.lang = 'en-US';
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(u);
  }
  window.onclick = e => {
    document.querySelectorAll('.modal').forEach(modal => {
      if (e.target === modal) {
        modal.style.display = "none";
        window.speechSynthesis.cancel();
      }
    });
  };
  // Floating evil emojis
  const evilEmojis = ['💀','☠️','👿','🩸','🔥'];
  for (let i=0;i<20;i++){
    const d = document.createElement('div');
    d.className='floating-evil';
    d.innerText = evilEmojis[Math.floor(Math.random()*evilEmojis.length)];
    d.style.left = Math.random()*100+'vw';
    d.style.top = Math.random()*100+'vh';
    d.style.fontSize = (Math.random()*24+20)+'px';
    d.style.animationDuration = (Math.random()*20+10)+'s';
    d.style.animationDelay = Math.random()*5+'s';
    document.body.appendChild(d);
  }
</script>

</body>
</html>
