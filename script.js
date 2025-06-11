function simulateProcessing() {
  const fileInput = document.getElementById("audioInput");
  if (!fileInput.files.length) {
    alert("Please upload an .mp3 file.");
    return;
  }

  // Simulate processing time
  document.getElementById("transcript").textContent = "Transcribing...";
  document.getElementById("summary").textContent = "Summarizing...";

  setTimeout(() => {
    document.getElementById("transcript").textContent =
      "This is a simulated transcript of the uploaded audio.";
    document.getElementById("summary").textContent =
      "This is a summary of the above transcript.";
  }, 2000);
}
