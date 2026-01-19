import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Varun – Voice Bot",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Talk to Varun")
st.write("Ask me about my journey, strengths, growth areas, or mindset.")
st.caption("No login • No API keys • Just talk")

html_code = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      color: #e5e7eb;
    }
    button {
      padding: 14px 24px;
      font-size: 16px;
      border-radius: 8px;
      border: none;
      background-color: #2563eb;
      color: white;
      cursor: pointer;
    }
    button:hover {
      background-color: #1d4ed8;
    }
    #output {
      margin-top: 20px;
      font-size: 15px;
      color: #c7d2fe;
      white-space: pre-line;
    }
  </style>
</head>
<body>

<button onclick="startListening()">🎤 Start Talking</button>
<div id="output"></div>

<script>
const responses = {
  life: "I’m an engineering student with a strong interest in AI and machine learning. Over time, I moved from just learning concepts to building practical solutions, especially where technology can create real-world impact. My journey is defined by curiosity, consistency, and self-learning.",
  superpower: "My number one superpower is my ability to learn quickly and apply that learning to real problems. I enjoy breaking down complex challenges and improving through iteration.",
  growth: "The top three areas I want to grow in are advanced machine learning, communicating complex ideas more clearly, and gaining more real-world decision-making experience.",
  misconception: "A common misconception is that I’m quiet or reserved. I usually observe first, but once I understand the context, I contribute actively and confidently.",
  limits: "I push my limits by deliberately taking on challenges that are slightly beyond my comfort zone. That discomfort usually means I’m learning and growing."
};

function getResponse(text) {
  text = text.toLowerCase();

  if (text.includes("life")) return responses.life;
  if (text.includes("superpower")) return responses.superpower;
  if (text.includes("grow")) return responses.growth;
  if (text.includes("misconception")) return responses.misconception;
  if (text.includes("limit") || text.includes("boundary")) return responses.limits;

  return "That’s a thoughtful question. I generally approach challenges with curiosity, continuous learning, and a focus on practical impact.";
}

function speak(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 1;
  utterance.pitch = 1;
  speechSynthesis.speak(utterance);
}

function startListening() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  recognition.lang = "en-US";

  recognition.start();

  recognition.onresult = function(event) {
    const userText = event.results[0][0].transcript;
    const reply = getResponse(userText);

    document.getElementById("output").innerText =
      "You asked: " + userText + "\\n\\nVarun says: " + reply;

    speak(reply);
  };

  recognition.onerror = function() {
    speak("Sorry, I couldn’t hear you clearly. Please try again.");
  };
}
</script>

</body>
</html>
"""

components.html(html_code, height=350)
