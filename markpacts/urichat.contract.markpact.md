# urichat contract (MVP)

Scheme: `chat://` — **deprecated**, use `llm://` + `message://`.

```yaml markpact:contract
apiVersion: urisys.io/v1
kind: UriContract
metadata:
  id: urichat.contract
  version: 1.0.0
scheme: chat
commands:
  - id: chat.message.send
    pattern: chat://local/message/command/send
    side_effects: true
    requires_approval: true
  - id: chat.uri.execute
    pattern: chat://local/uri/command/execute
    side_effects: true
    requires_approval: true
```
