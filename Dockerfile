# Gunakan base image Odoo
FROM odoo:15
COPY . /app
# Install dependensi yang diperlukan untuk Code Server
RUN apt-get update && apt-get install -y curl

# Unduh dan instal Code Server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Expose port untuk Code Server
EXPOSE 8080

# Jalankan Code Server saat container dimulai
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "."]

# docker build -t odoocode.docker 
