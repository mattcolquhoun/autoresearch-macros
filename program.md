# Autonomous Research Program: Mac-Optimized Architecture Search (MATT PASTED)

## Objective
Minimize the validation bits-per-byte (val_bpb) on the TinyShakespeare dataset within 5-minute training sprints. 

## Search Strategy
1. **Compute Efficiency First**: Since we are on a Mac GPU, prioritize architectures that maximize throughput. 
   - Avoid extremely high attention head counts that might exceed unified memory limits.
   - Experiment with **Linear Attention** or **SSSL** (Shift-SS-Linear) patterns to see if they offer better performance-per-watt than standard Self-Attention.

2. **Hyperparameter Exploration**:
   - Experiment with the **Muon** optimizer settings. Specifically, test if a higher learning rate with a more aggressive decay improves 5-minute convergence.
   - Test various **batch sizes** to find the "sweet spot" for MPS/MLX memory bandwidth.

3. **Architectural Innovations**:
   - Try varying the **embedding dimension** (n_embd) vs. **layer count** (n_layer).
   - Test "asymmetric" architectures where earlier layers are wider than later ones.
   - Explore adding **RMSNorm** or different activation functions like **GeGLU** if they aren't already present.

## Constraints & Rules
- **One Change at a Time**: Only modify one major component (e.g., just the optimizer or just the attention mechanism) per experiment to ensure we can attribute improvements correctly.
- **Metric Focus**: The primary success metric is `val_bpb`. If an experiment shows no improvement but trains significantly faster (higher tokens/sec), consider it a "tie" and keep the change.
- **Memory Safety**: If a training run crashes due to "Out of Memory" (OOM) on the Mac, immediately revert and try a smaller configuration.
- **Git Hygiene**: Every successful improvement must be committed with a descriptive message detailing the change made.

## Current Hypothesis
A slightly deeper model with fewer attention heads but a larger MLP expansion ratio will converge faster on this specific dataset than the baseline "nanochat" configuration.
