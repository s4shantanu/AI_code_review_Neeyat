import os

def generate_report(analysis, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, 'review_report.md')

    with open(report_path, 'w') as f:
        f.write("# AI Code Review Report\n\n")
        for tool, output in analysis.items():
            f.write(f"## {tool.upper()} Analysis\n")
            f.write("```\n")
            f.write(output)
            f.write("\n```\n\n")
    return report_path
