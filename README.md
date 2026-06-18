# urichat

**Deprecated** `chat://` URI capability pack — phrase-map + forward to a remote `/uri/call` (RDP stack).

Prefer `llm://local/text/query/plan` + `message://` for new flows. See `urisys-automation-lab/docs/CHAT-DEPRECATED.md`.

Licensed under Apache-2.0.

## Ekosystem TellMesh

Orchestrator: **[urisys](https://github.com/tellmesh/urisys)** · Mapa: **[MESH.md](https://github.com/tellmesh/urisys/blob/main/docs/MESH.md)** · Model: **[ECOSYSTEM.md](https://github.com/tellmesh/urisys/blob/main/../docs/ECOSYSTEM.md)**

| Pole | Wartość |
|------|---------|
| **Warstwa** | Capability pack (deprecated) |
| **Scheme** | `chat://` |
| **Zależność** | `uricore>=0.1.8` |

Runtime edge: **`uri_control.edge`** w pakiecie **`uricore`** (legacy `urisysedge` usunięty 2026-06).
Router intencji: **`urirouter`** (`uri_router`) — resolve + HTTP/MQTT delegate.

<!-- end-ecosystem -->
