# API

## Frontend

```
https://frontend
```

Displays a html for the frontend, displaying all previous messages

### Add a message

```
https://frontend/post_message
```
Post request, expects message (Required), username (Optional)

### Modify a message

```
https://frontend/modify_message
```
Post request, expects message (Required), message_id (Required)

### Delete a message

```
https://frontend/delete_message
```
Post request, expects message_id (Required)

### Note

These should all then redirect back to `https://frontend`


## Backend

### List all previous messages

```
https://backend/list
```

### Add a message

```
https://backend/create
```

### Modify a message

```
https://backend/update
```

### Delete a message

```
https://backend/delete
```
