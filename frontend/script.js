const API_URL = "https://ai-resume-analyzer-k4pc.onrender.com/analyze";

async function analyze() {
    const resume = document.getElementById("resume").value;
    const job = document.getElementById("job").value;

    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            resume: resume,
            job_description: job
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Match: ${data.match_percentage}%</h3>
        <p><b>Missing Skills:</b> ${data.missing_skills.join(", ")}</p>
        <ul>
            ${data.suggestions.map(s => `<li>${s}</li>`).join("")}
        </ul>
    `;
}
