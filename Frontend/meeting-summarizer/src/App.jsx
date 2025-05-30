import React, { useState } from "react";

export default function MeetingSummarizer() {
  const [summary, setSummary] = useState("");
  const [actions, setActions] = useState([]);
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const upload = async (e) => {
    e.preventDefault(); // prevent form submission if using a form element

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        console.error("Server responded with error", res.status);
        alert("Upload failed: " + res.statusText);
        return;
      }

      const data = await res.json();
      console.log("Response from backend:", data);

      setSummary(data.summary || "No summary found");
      setActions(data.action_text || []);
    } catch (error) {
      console.error("Fetch error:", error);
    }
  };

  return (
    <div>
      <h1>Upload Meeting Audio/Video</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={upload}>Upload & Summarize</button>

      <h2>Summary:</h2>
      <pre
         style={{
          maxWidth: "70vw",
          whiteSpace: "pre-wrap",
          wordWrap: "break-word",
          background: "#f9f9f9",
          padding: "1rem",
          borderRadius: "5px",
          fontSize:"20px",
          color:"black"
        }}
      >
        {summary}
      </pre>

      <h2>Action Items:</h2>
      <pre  style={{
          maxWidth: "70vw",
          whiteSpace: "pre-wrap",
          wordWrap: "break-word",
          background: "#f1f1f1",
          padding: "1rem",
          borderRadius: "5px",
          fontSize:"20px",
          color:"black"
        }}>
          {actions.join("\n")}
        </pre>
    </div>
  );
}
