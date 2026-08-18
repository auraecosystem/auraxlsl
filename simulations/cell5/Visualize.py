stages = [r["stage"] + "\n(" + r["name"] + ")" for r in results]
fidelities = [r["fidelity"] for r in results]
required = [r["required"] for r in results]

plt.figure(figsize=(10, 5))
plt.plot(stages, fidelities, marker='o', linewidth=2, label="Simulated Coherence Fidelity")
plt.plot(stages, required, color='red', linestyle='--', label="Required Threshold")
plt.axhline(0, color='black', lw=0.5)
plt.ylabel("Fidelity Ratio (0.0 - 1.0)")
plt.title("Aura Teleportation Pipeline: Coherence Fidelity Across Scale Thresholds")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
