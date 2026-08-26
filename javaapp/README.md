# Java Docker Demo

A small, visually polished **100% Java backend** demonstration using Spring Boot, Maven and Docker.

The UI is server-rendered with Thymeleaf, so there is no separate JavaScript frontend framework.

## What you need

- JDK 21
- Maven 3.6+
- Docker Desktop
- Any IDE (IntelliJ IDEA, VS Code, or Eclipse)

Spring Boot currently supports Java 17+; this demo uses Java 21 LTS.

## Demo 1 — Run locally

Verify Java:

```bash
java -version
```

Build:

```bash
mvn clean package
```

Run the JAR:

```bash
java -jar target/java-docker-demo-1.0.0.jar
```

Open:

http://localhost:8080

Useful endpoints:

- `/` — demo UI
- `/api/hello` — REST endpoint
- `/api/info` — Java/runtime information
- `/actuator/health` — health endpoint

## Demo 2 — Build a Docker image

From the project directory:

```bash
docker build -t java-docker-demo:1.0 .
```

Check the image:

```bash
docker images
```

## Demo 3 — Run the container

```bash
docker run -d --name java-demo -p 8080:8080 java-docker-demo:1.0
```

Check it:

```bash
docker ps
```

Open:

http://localhost:8080

Then show the logs:

```bash
docker logs java-demo
```

Stop/remove:

```bash
docker stop java-demo
docker rm java-demo
```

## What to explain during the demo

1. Java source code is compiled by Maven.
2. Maven creates an executable JAR under `target/`.
3. The Dockerfile uses a multi-stage build.
4. The first stage contains Maven and JDK tools.
5. The second stage contains only the Java runtime and JAR.
6. `docker build` creates an immutable image.
7. `docker run` creates a container from that image.
8. Port `8080` inside the container is mapped to port `8080` on the laptop.

## Optional: run with Docker Compose

```bash
docker compose up --build
```

The application will be available on:

http://localhost:8080
