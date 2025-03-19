async function analyzeFakeNews() {
    const text = document.getElementById("newsText").value;
    const response = await fetch("http://127.0.0.1:5001/detect_fake_news", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });
    const result = await response.json();
    document.getElementById("result").innerText = "Result: " + result.result;
}

async function summarizeNews() {
    const text = document.getElementById("newsText").value;
    const response = await fetch("http://127.0.0.1:5001/summarize_news", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });
    const result = await response.json();
    document.getElementById("result").innerText = "Summary: " + result.summary;
}
