FROM python:3.11-slim

# uv/uvx are needed because the gateway launches the proxied MCP servers with `uvx`
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    UV_TOOL_BIN_DIR=/usr/local/bin

WORKDIR /app

# Install the gateway's Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-install the proxied MCP servers so uvx doesn't download them at runtime
RUN uv tool install duckduckgo-mcp-server && \
    uv tool install mani-agentic-terminal

# Copy the gateway code
COPY app/ ./app/

EXPOSE 8092

CMD ["python", "app/gateway.py"]
