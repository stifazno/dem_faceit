from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Voice Mask Calculator (15 players)</title>

<style>
body{
    font-family:Arial,sans-serif;
    max-width:900px;
    margin:40px auto;
    padding:20px;
    background:#fafafa;
}

h1{
    text-align:center;
}

.players{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:10px;
    margin-bottom:20px;
}

.player{
    padding:15px;
    cursor:pointer;
    border:1px solid #ccc;
    border-radius:8px;
    text-align:center;
    user-select:none;
    transition:0.2s;
}

.player:hover{
    background:#eee;
}

.player.active{
    background:#222;
    color:white;
}

.box{
    background:white;
    padding:15px;
    border-radius:10px;
    margin-top:15px;
    box-shadow:0 2px 6px rgba(0,0,0,0.1);
}

.command{
    font-family:monospace;
    font-size:18px;
}
</style>
</head>

<body>

<h1>🎧 Voice Mask Calculator (1–15)</h1>

<div class="players" id="players"></div>

<div class="box">
    <div>Selected:</div>
    <div id="selected">—</div>
</div>

<div class="box">
    <div>Mask:</div>
    <div id="mask"><b>0</b></div>
</div>

<div class="box command" id="command">
tv_listen_voice_indices 0
</div>

<br>

<button onclick="copyCommand()">📋 Copy</button>

<script>

const selected = new Set();

function recalc(){

    let mask = 0;

    for(const p of selected){
        mask += (1 << (p - 1));
    }

    const sorted = [...selected].sort((a,b)=>a-b);

    document.getElementById("selected").innerText =
        sorted.length ? sorted.join(" ") : "—";

    document.getElementById("mask").innerText = mask;

    document.getElementById("command").innerText =
        "tv_listen_voice_indices " + mask;
}

// создаём 1–15 игроков
for(let i=1;i<=15;i++){

    const btn = document.createElement("div");
    btn.className = "player";
    btn.innerText = i;

    btn.onclick = () => {

        const num = Number(i);

        if(selected.has(num)){
            selected.delete(num);
            btn.classList.remove("active");
        } else {
            selected.add(num);
            btn.classList.add("active");
        }

        recalc();
    };

    document.getElementById("players").appendChild(btn);
}

function copyCommand(){
    navigator.clipboard.writeText(
        document.getElementById("command").innerText
    );
    alert("Copied!");
}

</script>

</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=HTML_PAGE)