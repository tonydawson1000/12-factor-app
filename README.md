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
## 3) [Config](https://12factor.net/config)
Store config in the environment

An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc).

The twelve-factor app stores config in environment variables

Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires strict separation of config from code. Config varies substantially across deploys, code does not.

---
## 4) [Backing Service](https://12factor.net/backing-services)
Treat backing services as attached resources

---
## 5) [Build, release, run](https://12factor.net/build-release-run)
The twelve-factor app uses strict separation between the build, release, and run stages.

- Build - "the build stage fetches vendors dependencies and compiles binaries and assets."
- Release - "Every release should always have a unique release ID (a timestamp of the release or an incrementing number. Releases are an append-only ledger and a release cannot be mutated once it is created. Any change must create a new release."
- Run - "A Release is taken (Build artifact + config) and is 'Run' on one or more  instances in an environment"

---
## 6) [Processes](https://12factor.net/processes)
Execute the app as one or more stateless processes

Twelve-factor processes are stateless and [share-nothing](https://en.wikipedia.org/wiki/Shared-nothing_architecture). Any data that needs to persist must be stored in a stateful [backing service](https://12factor.net/backing-services), typically a database.

Some web systems rely on “sticky sessions” – that is, caching user session data in memory of the app’s process and expecting future requests from the same visitor to be routed to the same process. 

Sticky sessions are a violation of twelve-factor and should never be used or relied upon. Session state data is a good candidate for a datastore that offers time-expiration, such as Memcached or Redis.

---
## 7) [Port binding](https://12factor.net/port-binding)
Export services via port binding

The twelve-factor app is completely self-contained and does not rely on runtime injection of a webserver into the execution environment to create a web-facing service. The web app exports HTTP as a service by binding to a port, and listening to requests coming in on that port.

---
## 8) [Concurrency](https://12factor.net/concurrency)
Scale out via the process model

---
## 9) [Disposability](https://12factor.net/disposability)
Maximize robustness with fast startup and graceful shutdown

The twelve-factor app’s processes are disposable, meaning they can be started or stopped at a moment’s notice.

Processes shut down gracefully when they receive a SIGTERM signal from the process manager. For a web process, graceful shutdown is achieved by ceasing to listen on the service port (thereby refusing any new requests), allowing any current requests to finish, and then exiting.

---
## 10) [Dev/prod parity](https://12factor.net/dev-prod-parity)
Keep development, staging, and production as similar as possible

The twelve-factor app is designed for continuous deployment by keeping the gap between development and production small.

The twelve-factor developer resists the urge to use different backing services between development and production

---
## 11) [Logs](https://12factor.net/logs)
Treat logs as event streams

A twelve-factor app never concerns itself with routing or storage of its output stream. It should not attempt to write to or manage logfiles. Instead, each running process writes its event stream, unbuffered, to stdout.

---
## 12) [Admin processes](https://12factor.net/admin-processes)
Run admin/management tasks as one-off processes
