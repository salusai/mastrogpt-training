hostname gpu
echo "gpu" > /etc/hostname
useradd -m msciab
usermod -aG sudo msciab
echo "msciab ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/msciab
chsh -s /bin/bash msciab
cp -r /root/.ssh /home/msciab
chown -R msciab:msciab /home/msciab/.ssh
curl -fsSL https://ollama.com/install.sh | sh


sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-arychive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy

sudo systemctl enable caddy

sudo cp Caddyfile /etc/caddy/Caddyfile
sudo systemctl restart caddy

curl -v https://ollama.nuvolaris.io
curl -v https://ollama.nuvolaris.io

sudo journalctl -u caddy -f


