# IP Change notifier on Docker
This is a notifier on changes to your Global IP Address.
Execute HTTP requests(ipinfo.io) and get global IP address repeatedly every configured time, and save it.
Compare the previous global IP address and the current one, if it has different, send a slack post for notification.

# Usage
1. Configure your slack webhook URL to an environmanet variables in 2way.
  - specify it directry to `docker-compase.yml`
  - `.env` file(specify file on `docker-compose.yml`)
2. build and execute app on docker
```
docker compose up -d
```

## systemctl compose
```
vim dc-ip-change-notifier.service # optional (ex. path to workingdir)
sudo ln -s /home/composer/dc-ip-change-notifier.service /etc/systemd/system/
cp docker-compose.yml docker-compose.override.yml # optional
sudo systemctl daemon-reload
sudo systemctl status dc-ip-change-notifier.service
sudo systemctl [start/stop/restart] dc-ip-change-notifier.service
```
