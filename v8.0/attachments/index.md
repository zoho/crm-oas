# Attachments API

- [OpenAPI specification](attachments.yaml)
- [Download a specific attachment file](mds/getAttachmentById.md)
  - Download the file content of a specific attachment by its ID. This endpoint returns the actual file (image, PDF, document, etc.). Returns an error for link attachments, as they cannot be downloaded.
  - [Examples](mds/examples/getAttachmentById.md)
- [Delete Link Attachment](mds/deleteAttachment.md)
  - Deletes a link attachment associated with a specific record in a module. Note that only link attachments can be deleted using this endpoint; file attachments cannot be deleted through this API.
  - [Examples](mds/examples/deleteAttachment.md)
- [Retrieve All Attachments](mds/getAttachments.md)
  - Retrieves all attachments associated with a specific record in a module.
  - [Examples](mds/examples/getAttachments.md)
- [Upload an Attachment](mds/uploadAttachment.md)
  - Uploads an attachment by providing either a file or a valid URL. Maximum request body size: 100MB.
  - [Examples](mds/examples/uploadAttachment.md)
