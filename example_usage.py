"""Example usage for SQL Injection AST Taint Analyzer."""
from client import SqlInjectionAstTaintAnalyzer

if __name__ == "__main__":
    sql = "SELECT id, name FROM users WHERE username = 'admin' OR '1'='1';"
    res = SqlInjectionAstTaintAnalyzer.analyze_sql(sql, "admin' OR '1'='1")
    print("SQL Vulnerability Audit Result:", res)
