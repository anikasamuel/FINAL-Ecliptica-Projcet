import subprocess
import shutil
import os

def run_ctm_analysis(file_name):
    cleaned_csv = f"C:/Users/anika/ecliptica/cleaned_{file_name}.csv"
    rdata_output = f"C:/Users/anika/ecliptica/CTMmods/ctm5.Rdata"
    ctm_output_csv = "C:/Users/anika/ecliptica/CTM10 - Topics With Keywords and Abstracts.csv"
    final_output_path = f"C:/Users/anika/ecliptica/{file_name}_ctmResults.csv"

    print("CTM files loading...")

    try:
        result = subprocess.run(
            ["Rscript", "CTM_Code/ctm_optimized.R", cleaned_csv, "ctm5"],
            check=True,
            capture_output=True,
            text=True
        )
        print("🔧 Rscript STDOUT:\n", result.stdout)
        print("🛑 Rscript STDERR:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print("❌ Error running CTM script.")
        print("🔧 STDOUT:\n", e.stdout)
        print("🛑 STDERR:\n", e.stderr)
        return None, None

    if not os.path.exists(rdata_output):
        print("❌ CTM script ran but .Rdata file was not created.")
        return None, None

    print("Assessing model, please wait...")

    try:
        assess = subprocess.run(
            ["Rscript", "CTM_Code/assess_model.R", rdata_output, cleaned_csv],
            check=True,
            capture_output=True,
            text=True
        )
        print("🔧 Assess STDOUT:\n", assess.stdout)
        print("🛑 Assess STDERR:\n", assess.stderr)
    except subprocess.CalledProcessError as e:
        print("❌ Error running the Assess model script.")
        print("🔧 Assess STDOUT:\n", e.stdout)
        print("🛑 Assess STDERR:\n", e.stderr)
        return None, None

    if not os.path.exists(ctm_output_csv):
        print(f"❌ Output file {ctm_output_csv} was not generated.")
        return None, None

    try:
        shutil.copy(ctm_output_csv, final_output_path)
        print(f"✅ Duplicate saved to {final_output_path}")
    except Exception as e:
        print(f"❌ Error copying output file: {e}")
        return None, None

    return final_output_path, rdata_output
