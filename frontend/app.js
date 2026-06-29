const btn = document.getElementById("generateBtn");

btn.addEventListener("click", async () => {
  const question = document.getElementById("question").value.trim();
  const sqlOutput = document.getElementById("sqlOutput");
  const explanationOutput = document.getElementById("explanationOutput");
  const resultOutput = document.getElementById("resultOutput");

  if (!question) {
    sqlOutput.textContent = "Please enter a question first.";
    return;
  }

  sqlOutput.textContent = "Loading...";
  explanationOutput.textContent = "Loading explanation...";
  resultOutput.innerHTML = "Loading results...";

  try {
    const response = await fetch("http://127.0.0.1:8000/generate-sql", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await response.json();

    if (data.error) {
      sqlOutput.textContent = data.sql || "No SQL generated.";
      explanationOutput.textContent = data.error;
      resultOutput.innerHTML = "";
      return;
    }

    sqlOutput.textContent = data.sql;
    explanationOutput.textContent = data.explanation;
    renderTable(data.rows || []);
  } catch (error) {
    sqlOutput.textContent = "Could not connect to backend.";
    explanationOutput.textContent = "Check whether FastAPI is running on port 8000.";
    resultOutput.innerHTML = "";
  }
});

function renderTable(rows) {
  const resultOutput = document.getElementById("resultOutput");

  if (!rows.length) {
    resultOutput.innerHTML = "<p>No rows returned.</p>";
    return;
  }

  const headers = Object.keys(rows[0]);
  let html = "<table><thead><tr>";
  headers.forEach(h => html += `<th>${h}</th>`);
  html += "</tr></thead><tbody>";

  rows.forEach(row => {
    html += "<tr>";
    headers.forEach(h => html += `<td>${row[h]}</td>`);
    html += "</tr>";
  });

  html += "</tbody></table>";
  resultOutput.innerHTML = html;
} 