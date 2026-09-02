### `application/json` — UpdateShareRecordsRequest

An example of updating a share entry for a role.

```json
{
  "share": [
    {
      "shared_with": {
        "id": "111111000000000874",
        "type": "roles"
      },
      "share_related_records": false,
      "permission": "full_access",
      "type": "private"
    }
  ],
  "notify_shared_members": false,
  "notify_on_completion": true
}
```
