from utils.unzipper import unzip_code
from utils.analyzer import analyze_code
from utils.improver import improve_code
from utils.reporter import generate_report

def main():
    zip_path = "examples/sample_project.zip"
    
    print("📦 Unzipping code...")
    extracted_path = unzip_code(zip_path)

    print("🔍 Analyzing code...")
    analysis = analyze_code(extracted_path)

    print("🛠 Improving code...")
    improved_path = improve_code(extracted_path)

    print("📝 Generating report...")
    report = generate_report(analysis)

    print("✅ Done!")
    print(f"📁 Improved code saved to: {improved_path}")
    print(f"📄 Report saved to: {report}")

if __name__ == "__main__":
    main()
