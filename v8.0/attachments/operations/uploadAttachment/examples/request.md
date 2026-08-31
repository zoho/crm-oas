### `multipart/form-data` — BasicUpload

Upload with title

```json
{
  "attachmentUrl": "https://example.com/document.pdf",
  "title": "Q4 Financial Report"
}
```

### `multipart/form-data` — MinimalUpload

Upload without title

```json
{
  "attachmentUrl": "https://example.com/document.pdf"
}
```

### `multipart/form-data` — MaxLengthUrl

Maximum length URL

```json
{
  "attachmentUrl": "https://example.com/very/long/path/that/could/reach/maximum/allowed/length/of/2000/characters/...",
  "title": "Document with long URL"
}
```
