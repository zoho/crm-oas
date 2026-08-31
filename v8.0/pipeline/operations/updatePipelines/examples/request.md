### `application/json` — PipelineUpdateRequest

```json
{
  "pipeline": [
    {
      "id": "12345678901234567890",
      "display_value": "adfadf12adf",
      "default": false,
      "maps": [
        {
          "id": "2766660000000007106",
          "sequence_number": 2
        },
        {
          "id": "2766660000000007104",
          "sequence_number": 1
        }
      ]
    }
  ]
}
```

### `application/json` — PipelineDeleteRequest

```json
{
  "pipeline": [
    {
      "id": "12345678901234567890",
      "_delete": {
        "permanent": null
      }
    }
  ]
}
```
