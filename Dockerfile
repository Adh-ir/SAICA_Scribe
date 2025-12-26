# CA Scribe - Streamlit Application
# Multi-stage build for smaller image size

FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for layer caching
COPY code/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# --- Production Stage ---
FROM python:3.11-slim

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY code/ .

# Create .streamlit directory for config
RUN mkdir -p .streamlit

# Streamlit configuration for container deployment
RUN echo '[server]\n\
    headless = true\n\
    port = 8501\n\
    address = "0.0.0.0"\n\
    enableCORS = false\n\
    enableXsrfProtection = false\n\
    \n\
    [browser]\n\
    gatherUsageStats = false\n\
    \n\
    [theme]\n\
    base = "light"\n\
    ' > .streamlit/config.toml

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py"]
