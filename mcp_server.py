"""MCP Server wrapper for SQL Injection AST Taint Analyzer."""
import json
import sys
from client import SqlInjectionAstTaintAnalyzer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "audit_sql_injection",
                    "description": "Analyze dynamic SQL query for AST taint patterns, tautologies, and destructive statements",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "user_input": {"type": "string"}
                        },
                        "required": ["query"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = SqlInjectionAstTaintAnalyzer.analyze_sql(args.get("query", ""), args.get("user_input", ""))
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
