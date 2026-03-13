import os
import subprocess

# Fixed files (The agent cannot change these)
PROGRAM_FILE = "program.md"
RESEARCH_LOG = "research_log.md"
MATRIX_FILE = "competitor_matrix.csv"

# The "Agent's Playground" (The agent can edit this script to change how it searches)
RESEARCH_TOOL = "research_tool.py" 

def run_iteration():
    print("--- Starting Research Iteration ---")
    
    # 1. READ: Load instructions from program.md
    with open(PROGRAM_FILE, 'r') as f:
        instructions = f.read()
    
    # 2. EXECUTE: Run the research tool (e.g., search Google/Reddit)
    # The agent might have modified RESEARCH_TOOL to target specific rivals
    result = subprocess.run(["python", RESEARCH_TOOL], capture_output=True, text=True)
    
    if result.returncode == 0:
        new_data = result.stdout
        print(f"New Signal Found: {new_data[:50]}...")
        
        # 3. EVALUATE: Is this new info? (Simplified logic)
        with open(RESEARCH_LOG, 'a') as f:
            f.write(f"\n## Iteration Result\n{new_data}\n")
            
        # 4. COMMIT: In a real autoresearch setup, we'd use Git to save progress
        # os.system("git add . && git commit -m 'new competitive insight found'")
    else:
        print("Iteration failed. Reverting changes...")

if __name__ == "__main__":
    # Simulate the "all night" loop (run 5 times for this example)
    for i in range(5):
        run_iteration()
