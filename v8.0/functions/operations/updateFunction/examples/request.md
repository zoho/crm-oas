### `multipart/form-data` — SamplePutRequest

Update Function Metadata and Publish With a Changelog

```json
{
  "metadata": {
    "functions": [
      {
        "name": "Name of the Function",
        "description": "description",
        "_code": "function script details as an string"
      }
    ],
    "publish": {
      "changelog": "message"
    }
  },
  "code": "(binary content of the file to be uploaded, not represented in JSON format)"
}
```
