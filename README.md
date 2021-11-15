# IP Change notifier on Docker
This is a notifier on changes to your Global IP Address.
- Execute HTTP requests(ipinfo.io) and get global IP address repeatedly every configured time, and save it.
- Compare the previous global IP address and the current one, if it has different, send a slack post for notification.

# Usage
1. Configure your slack webhook URL to an environment variables in 2way.
  - Specify it directly to `docker-compase.yml`
  - `.env` file(specify file on `docker-compose.yml`)
2. Build and execute app on docker
  ```
  docker-compose up -d
  ```
