// Floating Chat Widget
class ChatWidget {
  constructor() {
    this.isOpen = false;
    this.conversationHistory = [];
    this.init();
  }

  init() {
    this.createWidget();
    this.attachEventListeners();
    this.showWelcomeMessage();
  }

  createWidget() {
    const widgetHTML = `
      <div class="chat-widget" id="chatWidget">
        <!-- Toggle Button -->
        <button class="chat-toggle-btn" id="chatToggleBtn">
          <span id="chatToggleIcon">💬</span>
          <span class="chat-notification-badge" id="chatNotificationBadge" style="display: none;">1</span>
        </button>

        <!-- Chat Window -->
        <div class="chat-window" id="chatWindow">
          <!-- Header -->
          <div class="chat-window-header">
            <div class="chat-window-title">
              <div class="chat-window-avatar">🤖</div>
              <div class="chat-window-info">
                <h3>Health Assistant</h3>
                <p class="chat-window-status">Online • Siap membantu</p>
              </div>
            </div>
            <div class="chat-window-actions">
              <button class="chat-icon-btn" onclick="chatWidget.clearChat()" title="Hapus chat">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/>
                </svg>
              </button>
              <button class="chat-icon-btn" onclick="chatWidget.toggleChat()" title="Tutup">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 6L6 18M6 6l12 12"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Messages -->
          <div class="chat-window-messages" id="chatMessages"></div>

          <!-- Typing Indicator -->
          <div class="chat-window-typing" id="chatTyping">
            <div class="chat-typing-dot"></div>
            <div class="chat-typing-dot"></div>
            <div class="chat-typing-dot"></div>
            <span>AI sedang mengetik...</span>
          </div>

          <!-- Input -->
          <div class="chat-window-input">
            <div class="chat-input-wrapper">
              <textarea 
                id="chatInput" 
                placeholder="Ketik gejala Anda..."
                rows="1"
                onkeydown="chatWidget.handleKeyPress(event)"
              ></textarea>
              <button class="chat-send-btn" id="chatSendBtn" onclick="chatWidget.sendMessage()">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/>
                </svg>
              </button>
            </div>
            <div class="chat-quick-replies">
              <button class="chat-quick-reply" onclick="chatWidget.quickReply('Saya merasa demam dan batuk')">🤒 Demam & Batuk</button>
              <button class="chat-quick-reply" onclick="chatWidget.quickReply('Pusing dan mual')">😵 Pusing & Mual</button>
              <button class="chat-quick-reply" onclick="chatWidget.quickReply('Sakit kepala')">🤕 Sakit Kepala</button>
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', widgetHTML);
  }

  attachEventListeners() {
    const toggleBtn = document.getElementById('chatToggleBtn');
    const input = document.getElementById('chatInput');

    toggleBtn.addEventListener('click', () => this.toggleChat());
    
    // Auto-resize textarea
    input.addEventListener('input', function() {
      this.style.height = 'auto';
      this.style.height = Math.min(this.scrollHeight, 80) + 'px';
    });
  }

  toggleChat() {
    this.isOpen = !this.isOpen;
    const chatWindow = document.getElementById('chatWindow');
    const toggleBtn = document.getElementById('chatToggleBtn');
    const toggleIcon = document.getElementById('chatToggleIcon');
    const badge = document.getElementById('chatNotificationBadge');

    if (this.isOpen) {
      chatWindow.classList.add('active');
      toggleBtn.classList.add('active');
      toggleIcon.textContent = '✕';
      badge.style.display = 'none';
      
      // Focus input
      setTimeout(() => {
        document.getElementById('chatInput').focus();
      }, 300);
    } else {
      chatWindow.classList.remove('active');
      toggleBtn.classList.remove('active');
      toggleIcon.textContent = '💬';
    }
  }

  showWelcomeMessage() {
    const welcomeMsg = `
      <p>Halo! 👋 Saya Health Assistant AI.</p>
      <p>Ceritakan gejala yang Anda alami, saya akan membantu menganalisisnya.</p>
      <p><strong>Contoh:</strong></p>
      <ul>
        <li>"Saya demam dan batuk"</li>
        <li>"Pusing dan mual"</li>
        <li>"BB 70kg, TB 170cm, sering pusing"</li>
      </ul>
    `;
    this.addMessage(welcomeMsg, 'bot');
  }

  addMessage(content, type) {
    const messagesContainer = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-window-message ${type}`;
    
    const avatar = type === 'bot' ? '🤖' : '👤';
    const time = new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });
    
    messageDiv.innerHTML = `
      <div class="chat-msg-avatar">${avatar}</div>
      <div class="chat-msg-content">
        <div class="chat-msg-bubble">${content}</div>
        <div class="chat-msg-time">${time}</div>
      </div>
    `;
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    // Show notification if chat is closed
    if (!this.isOpen && type === 'bot') {
      const badge = document.getElementById('chatNotificationBadge');
      badge.style.display = 'flex';
    }
  }

  showTyping() {
    document.getElementById('chatTyping').classList.add('active');
    document.getElementById('chatSendBtn').disabled = true;
  }

  hideTyping() {
    document.getElementById('chatTyping').classList.remove('active');
    document.getElementById('chatSendBtn').disabled = false;
  }

  async sendMessage() {
    const input = document.getElementById('chatInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Add user message
    this.addMessage(message, 'user');
    
    // Clear input
    input.value = '';
    input.style.height = 'auto';
    
    // Show typing
    this.showTyping();
    
    try {
      const response = await fetch('/chat/api', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
      });
      
      const data = await response.json();
      
      this.hideTyping();
      
      if (data.success) {
        const formattedResponse = this.formatResponse(data.response);
        this.addMessage(formattedResponse, 'bot');
        
        // Store in history
        this.conversationHistory.push({
          user: message,
          bot: data.response,
          symptoms: data.detected_symptoms,
          results: data.results
        });
      } else {
        this.addMessage('Maaf, terjadi kesalahan: ' + (data.error || 'Unknown error'), 'bot');
      }
    } catch (error) {
      this.hideTyping();
      this.addMessage('Maaf, terjadi kesalahan koneksi. Silakan coba lagi.', 'bot');
      console.error('Error:', error);
    }
  }

  formatResponse(text) {
    // Convert markdown-like syntax to HTML
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/### (.*?)$/gm, '<h4 style="margin: 8px 0 4px 0; font-size: 0.95rem;">$1</h4>');
    text = text.replace(/^- (.*?)$/gm, '<li>$1</li>');
    text = text.replace(/---/g, '<hr style="margin: 8px 0; border: none; border-top: 1px solid rgba(255,255,255,0.1);">');
    
    // Wrap lists
    text = text.replace(/(<li>.*<\/li>)/s, '<ul style="margin: 6px 0; padding-left: 18px; font-size: 0.85rem;">$1</ul>');
    
    // Convert newlines to paragraphs
    const paragraphs = text.split('\n\n').filter(p => p.trim());
    text = paragraphs.map(p => {
      if (p.startsWith('<h4>') || p.startsWith('<ul>') || p.startsWith('<hr>')) {
        return p;
      }
      return '<p>' + p.replace(/\n/g, '<br>') + '</p>';
    }).join('');
    
    return text;
  }

  quickReply(message) {
    document.getElementById('chatInput').value = message;
    this.sendMessage();
  }

  clearChat() {
    if (confirm('Hapus semua riwayat percakapan?')) {
      const messagesContainer = document.getElementById('chatMessages');
      messagesContainer.innerHTML = '';
      this.conversationHistory = [];
      this.showWelcomeMessage();
    }
  }

  handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.sendMessage();
    }
  }
}

// Initialize chat widget when DOM is ready
let chatWidget;
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    chatWidget = new ChatWidget();
  });
} else {
  chatWidget = new ChatWidget();
}
