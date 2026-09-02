### `application/json` — MassChangeOwnerExample

An example of mass change owner request with territory and criteria filter.

```json
{
  "cvid": "2423488000000091545",
  "owner": {
    "id": "2423488000000483001"
  },
  "territory": {
    "id": "2423488000000780003",
    "include_child": true
  },
  "criteria": {
    "field": {
      "api_name": "Stage",
      "id": "2423488000000000525"
    },
    "comparator": "equal",
    "value": "Qualification"
  }
}
```
