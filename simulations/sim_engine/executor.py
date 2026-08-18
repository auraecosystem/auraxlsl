logger = XLogWriter()
results = []

print("="*65)
print(f"{'STAGE':<8} | {'TARGET':<15} | {'FIDELITY':<10} | {'LOGIC GATE':<12} | {'STATUS'}")
print("="*65)

for stage_id, stage_info in TELEPORTATION_STAGES.items():
    # 1. Quantum State Analysis (.xquant)
    fidelity = XQuantState.calculate_fidelity(stage_id, noise_level=0.15)
    
    # 2. Dimensional Transformation Check (.xdim)
    is_valid_dim, det_M = XDimTransform.check_matrix_singularity(dim_count=4)
    
    # 3. Logic & Bounding Gate Evaluation (.xphilo)
    is_permitted, reason = XPhiloGate.evaluate_permission(stage_id, fidelity)
    
    status_str = "SUCCESS" if (is_valid_dim and is_permitted) else "FAILED / HALTED"
    
    # 4. Telemetry Logging (.xlog)
    logger.record_event(stage_id, status_str, fidelity, det_M)
    
    results.append({
        "stage": stage_id,
        "name": stage_info["name"],
        "fidelity": fidelity,
        "required": stage_info["coherence_req"],
        "status": status_str,
        "reason": reason
    })
    
    print(f"{stage_id:<8} | {stage_info['name']:<15} | {fidelity:<10.4f} | {str(is_permitted):<12} | {status_str}")

print("="*65)
