Partial Success With Compilation Error on Publish

```json
{
  "functions": [
    {
      "code": "PARTIAL_SUCCESS",
      "details": {
        "id": "111111000000187000",
        "errors": {
          "code": "COMPILATION_ERROR",
          "details": {
            "errors": [
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 60,
                "message": "error: no source files"
              },
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 60,
                "message": "enum constant expected here"
              },
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 61,
                "message": "<identifier> expected"
              },
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 62,
                "message": "',', '}', or ';' expected"
              },
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 66,
                "message": "<identifier> expected"
              },
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 81,
                "message": "invalid method declaration; return type required"
              },
              {
                "file": "/java_17_test/RecordValidator.java",
                "line": 113,
                "message": "reached end of file while parsing"
              },
              {
                "file": "/java_17_test/DataManager.java",
                "line": 18,
                "message": "'(' expected"
              },
              {
                "file": "/java_17_test/DataManager.java",
                "line": 90,
                "message": "field declaration must be static"
              },
              {
                "file": "/java_17_test/DataManager.java",
                "line": 110,
                "message": "illegal escape character"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 47,
                "message": "';' expected"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 53,
                "message": "unclosed string literal"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 59,
                "message": "illegal start of expression"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 69,
                "message": "';' expected"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 72,
                "message": "';' expected"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 75,
                "message": "not a statement"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 75,
                "message": "';' expected"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 126,
                "message": "'[' expected"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 126,
                "message": "-> expected"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 300,
                "message": "unclosed text block"
              },
              {
                "file": "/java_17_test/java_17_test.java",
                "line": 323,
                "message": "reached end of file while parsing"
              }
            ]
          },
          "message": "function publish failed due to compilation errors",
          "status": "error"
        }
      },
      "message": "function created but publish failed",
      "status": "success"
    }
  ]
}
```
