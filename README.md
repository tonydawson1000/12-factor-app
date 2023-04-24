# 12-Factor-App

## Description
---
[The Twelve Factor App](https://12factor.net/) documents best practice approach to developing modern, cloud native apps.

## 1) [Codebase](https://12factor.net/codebase)
One codebase tracked in revision control, many deploys

---
## 2) [Dependencies](https://12factor.net/dependencies)
Explicitly declare and isolate dependencies

---
| Command                                   | Description |
| ---                                       | --- |
| Build the image                           | `podman build -t quay.io/tonydawson1000/twelve-factor-app .` |
| Ensure the image has been created         | `podman images` |
| Run (Start an instance of) the container  | `podman run -d -p 8088:5000 quay.io/tonydawson1000/twelve-factor-app:latest` |
| Ensure the image is running...            | `podman ps` (make a note of the container-id) |
| Test                                      | `curl localhost:8088` |
| Login to the running container            | `podman exec -it <container-id> /bin/sh` |
| Stop the container instance               | `podman stop <container-id>` |
| Login to the Image Registry               | `podman login quay.io` |
| Upload Image                              | `podman push quay.io/tonydawson1000/twelve-factor-app:latest` |
| (Optional) Tidyup / Delete the image      | `podman rmi <image-name>` |

---
## 3) 