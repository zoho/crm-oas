### `multipart/form-data` — SamplePostRequest

Create a Function With Metadata and Code File

```json
{
  "metadata": {
    "functions": [
      {
        "name": "Name of the Function",
        "description": "description",
        "category": "Button",
        "api_name": "test_function",
        "runtime": "Deluge 1.0",
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
