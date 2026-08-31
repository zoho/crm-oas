An example error response for exceeding the concurrent scheduler job limit.

```json
{
  "status": "error",
  "code": "CONCURRENT_JOB_LIMIT_EXCEEDED",
  "message": "Transfer and delete user scheduler limit reached",
  "details": {
    "limit": "10"
  }
}
```
