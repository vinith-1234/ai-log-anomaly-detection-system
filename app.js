async function uploadLog() {
    const fileInput = document.getElementById("logFile");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload-log", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>File: ${data.filename}</h3>
        <p>Features: ${data.features}</p>
        <p>Anomaly Score: ${data.anomaly_score}</p>
        <h2>Risk: ${data.risk}</h2>
    `;
}