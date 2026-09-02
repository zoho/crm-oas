Example of assigning ownership to a Service Provider user outside allowed modules.

```json
{
  "code": "NOT_ALLOWED",
  "message": "Service Provider User can only be assigned to tasks, meetings, calls, and appointments",
  "status": "error",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id"
  }
}
```
