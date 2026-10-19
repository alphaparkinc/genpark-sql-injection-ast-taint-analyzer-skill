# genpark-sql-injection-ast-taint-analyzer-skill

[![Verified by Smithery](https://smithery.ai/badge/@alphaparkinc/genpark-sql-injection-ast-taint-analyzer-skill)](https://smithery.ai/servers/@alphaparkinc/genpark-sql-injection-ast-taint-analyzer-skill)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![Website](https://img.shields.io/badge/Website-GenPark.ai-green)](https://www.genpark.ai)

> Dynamic SQL AST taint tracking and static vulnerability auditor detecting tautologies and destructive piggybacking

## Quick Installation & MCP Integration
Add to your Claude Desktop or Cursor configuration:
```json
{
  "mcpServers": {
    "genpark-sql-injection-ast-taint-analyzer-skill": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

## Zero Dependencies
Implemented entirely in Python 3 standard library.
