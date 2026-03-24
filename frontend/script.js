async function upload() {
    const file = document.getElementById("fileInput").files[0];

    let formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    renderDashboard(data);
    renderLogs(data.findings);
    renderInsights(data.insights);
}
async function analyze() {
    const content = document.getElementById("inputText").value;
    const inputType = document.getElementById("inputType").value;

    const response = await fetch(`http://127.0.0.1:8000/analyze?input_type=${inputType}&content=${encodeURIComponent(content)}`, {
        method: "POST"
    });

    const data = await response.json();

    document.getElementById("result").innerText = JSON.stringify(data, null, 2);
}

function renderDashboard(data) {
    let color = getColor(data.risk_level);

    document.getElementById("dashboard").innerHTML = `
        <div class="card" style="border-color:${color}">
            <h2>Risk Level: ${data.risk_level.toUpperCase()}</h2>
            <h3>Score: ${data.risk_score}</h3>
        </div>
    `;
}

function renderLogs(findings) {
    let html = "";

    findings.forEach(f => {
        let color = getColor(f.risk);

        html += `
            <div class="log-line" style="border-left:5px solid ${color}">
                <span class="line">Line ${f.line}</span>
                <span class="content">${f.content}</span>
                <span class="badge" style="background:${color}">
                    ${f.risk.toUpperCase()}
                </span>
            </div>
        `;
    });

    document.getElementById("logOutput").innerHTML = html;
}

function renderInsights(insights) {
    let html = "";

    insights.forEach(i => {
        html += `<li>${i}</li>`;
    });

    document.getElementById("insights").innerHTML = html;
}

function getColor(risk) {
    if (risk === "critical") return "#ef4444";
    if (risk === "high") return "#f97316";
    if (risk === "medium") return "#eab308";
    return "#22c55e";
}

function highlight(text) {
    return text
        .replace(/password\s*=\s*\S+/gi, "🔴 $&")
        .replace(/sk-[a-zA-Z0-9]+/g, "🟠 $&")
        .replace(/\S+@\S+/g, "🟡 $&");
}
