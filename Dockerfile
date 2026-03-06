FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg2 curl ca-certificates software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# -------------------------
# Install Google Chrome
# -------------------------
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# -------------------------
# Install Firefox
# -------------------------
RUN apt-get update && \
    apt-get install -y firefox-esr

# -------------------------
# Install Microsoft Edge
# -------------------------
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-edge.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-edge.gpg] https://packages.microsoft.com/repos/edge stable main" \
    > /etc/apt/sources.list.d/microsoft-edge.list && \
    apt-get update && \
    apt-get install -y microsoft-edge-stable

# -------------------------
# Python setup
# -------------------------
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run tests
CMD ["pytest", "Optima_Automation", "-vs"]