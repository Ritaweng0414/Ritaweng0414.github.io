function changeMood() {
    const mood = document.getElementById("moodInput").value.toLowerCase();
    const messageElement = document.getElementById("message");
    const emojiElement = document.getElementById("emoji");
}
    if (mood === "happy") {
      document.body.className = "happy";
      messageElement.textContent = "You are feeling happy!";
      emojiElement.textContent = "😊";
    } else if (mood === "sad") {
      document.body.className = "sad";
      messageElement.textContent = "You are feeling sad.";
      emojiElement.textContent = "😢";
    } else {
      messageElement.textContent = "Please type 'happy' or 'sad'.";
      emojiElement.textContent = "";
    }