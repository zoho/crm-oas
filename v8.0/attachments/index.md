# Attachments API

- [OpenAPI specification](attachments.yaml)
- [Download a specific attachment file](operations/getAttachmentById/operation.md)
  - Download the file content of a specific attachment by its ID. This endpoint returns the actual file (image, PDF, document, etc.). Returns an error for link attachments, as they cannot be downloaded.
  - [Examples](operations/getAttachmentById/examples/)
- [Delete Link Attachment](operations/deleteAttachment/operation.md)
  - Deletes a link attachment associated with a specific record in a module. Note that only link attachments can be deleted using this endpoint; file attachments cannot be deleted through this API.
  - [Examples](operations/deleteAttachment/examples/)
- [Retrieve All Attachments](operations/getAttachments/operation.md)
  - Retrieves all attachments associated with a specific record in a module.
  - [Examples](operations/getAttachments/examples/)
- [Upload an Attachment](operations/uploadAttachment/operation.md)
  - Uploads an attachment by providing either a file or a valid URL. Maximum request body size: 100MB.
  - [Examples](operations/uploadAttachment/examples/)
