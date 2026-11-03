COMPILATION_ERROR Response When the Function Fails to Publish Due to Compilation Errors

```json
{
  "code": "COMPILATION_ERROR",
  "details": {
    "errors": [
      {
        "file": "/java_17_test/java_17_test.java",
        "line": 31,
        "message": "';' expected"
      },
      {
        "file": "/java_17_test/java_17_test.java",
        "line": 37,
        "message": "unclosed string literal"
      },
      {
        "file": "/java_17_test/java_17_test.java",
        "line": 43,
        "message": "illegal start of expression"
      }
    ]
  },
  "message": "function publish failed due to compilation errors",
  "status": "error"
}
```
