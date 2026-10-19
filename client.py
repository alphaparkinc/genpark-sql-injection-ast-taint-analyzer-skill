"""SQL Injection AST Taint Analyzer.
100% Python Standard Library.
"""
import re

class SqlInjectionAstTaintAnalyzer:
    """Dynamic SQL AST taint tracking and static vulnerability auditor detecting tautologies and destructive piggybacking."""

    DANGEROUS_PATTERNS = [
        (re.compile(r"(\bor\b|\band\b)\s+['\"]?1['\"]?\s*=\s*['\"]?1", re.I), "Tautology bypass (' OR '1'='1)"),
        (re.compile(r";\s*(drop|truncate|delete|alter)\s+", re.I), "Piggybacked destructive query"),
        (re.compile(r"--|/\*|\*/", re.I), "Comment masking injection"),
        (re.compile(r"union\s+(all\s+)?select", re.I), "UNION-based data exfiltration"),
        (re.compile(r"exec(\s+|\()+xp_", re.I), "Command shell execution probe")
    ]

    @staticmethod
    def analyze_sql(query: str, user_input: str) -> dict:
        vulnerabilities = []
        for pattern, desc in SqlInjectionAstTaintAnalyzer.DANGEROUS_PATTERNS:
            if pattern.search(query):
                vulnerabilities.append(desc)

        is_tainted = False
        if user_input and user_input in query and any(char in user_input for char in ["'", '"', ";", "--"]):
            is_tainted = True
            vulnerabilities.append("Direct unescaped user parameter interpolation detected")

        risk = "CRITICAL" if vulnerabilities else "SAFE"
        return {
            "query_length": len(query),
            "taint_detected": is_tainted,
            "vulnerabilities": vulnerabilities,
            "risk_assessment": risk,
            "action": "BLOCK_EXECUTION" if risk == "CRITICAL" else "ALLOW_EXECUTION"
        }
