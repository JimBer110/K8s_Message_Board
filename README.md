# Kubernetes Messsage Board

A user can connect to application and be presented a text box, they can then write something and send it. All the sent messages will show up in chronological order on the index page.

## First connection
```mermaid
sequenceDiagram
Browser->>Frontend: GET index.html
Frontend->>Backend: GET /list
Backend->>db: select messages
db-->>Backend: messages
Backend-->>Frontend: messages
Frontend-->>Browser: index.html
```

## Sends message
```mermaid
sequenceDiagram
Browser->>Frontend: POST /post_message
Frontend->>Backend: POST /create
Backend->>db: insert message
db-->>Backend: status
Backend-->>Frontend: status
Frontend-->>Browser: redirect to index.html
```

## Modify message
```mermaid
sequenceDiagram
Browser->>Frontend: POST /modify_message
Frontend->>Backend: POST /update
Backend->>db: update message
db-->>Backend: status
Backend-->>Frontend: status
Frontend-->>Browser: redirect to index.html
```

## Delete message
```mermaid
sequenceDiagram
Browser->>Frontend: POST /delete_message
Frontend->>Backend: POST /delete
Backend->>db: delete message
db-->>Backend: status
Backend-->>Frontend: status
Frontend-->>Browser: redirect to index.html
```
