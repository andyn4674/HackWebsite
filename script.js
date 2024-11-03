import { createSignal, onCleanup } from 'solid-js';
import { render, html } from 'solid-js/web';
const form = document.querySelector('form');
const personality = document.getElementById("personality");
const messageArea = document.getElementById("message-area"); 

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission
  const personalityValue = personality.value.toUpperCase(); 

  if (["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"].includes(personalityValue)) {
    messageArea.innerHTML = ""
  } else {
    messageArea.innerHTML = "<p>Invalid personality type. Please enter a valid MBTI personality type.</p>"; 
  }
});
