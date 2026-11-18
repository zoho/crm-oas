CANNOT_PROCESS error when a deleted state still has connecting transitions

```json
{
  "blueprints": [
    {
      "code": "CANNOT_PROCESS",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[0].states.id"
      },
      "message": "the state is deleted but transitions connecting the state are not deleted",
      "status": "error"
    }
  ]
}
```
