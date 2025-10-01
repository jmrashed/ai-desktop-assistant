const socket = io();
const conversation = document.getElementById('conversation');
const startButton = document.getElementById('startButton');
const listeningIndicator = document.getElementById('listeningIndicator');

function addMessage(text, className) {
    const message = document.createElement('div');
    message.className = `message ${className}`;
    message.textContent = text;
    conversation.appendChild(message);
    conversation.scrollTop = conversation.scrollHeight;
}

startButton.addEventListener('click', () => {
    startButton.disabled = true;
    listeningIndicator.classList.add('active');
    socket.emit('start_listening');
});

socket.on('status', (data) => {
    addMessage(data.text, 'status');
});

socket.on('command', (data) => {
    addMessage(`You: ${data.text}`, 'command');
});

socket.on('response', (data) => {
    addMessage(`Assistant: ${data.text}`, 'response');
    startButton.disabled = false;
    listeningIndicator.classList.remove('active');
});

socket.on('error', (data) => {
    addMessage(data.text, 'error');
    startButton.disabled = false;
    listeningIndicator.classList.remove('active');
});

document.addEventListener('keypress', (e) => {
    if (e.code === 'Space' && !startButton.disabled) {
        e.preventDefault();
        startButton.click();
    }
});