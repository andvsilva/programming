import os
import time
import platform
import multiprocessing as mp
import numpy as np
from datetime import datetime

# ───────────────────────────────────────────
# Force NumPy to use 1 thread per process
# (important for accurate per-core benchmark)
# ───────────────────────────────────────────
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"


# ───────────────────────────────────────────
# Heavy computation per core
# ───────────────────────────────────────────
def single_core_test(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    t0 = time.time()
    C = A @ B
    t1 = time.time()
    return t1 - t0


def worker_compute(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = A @ B
    return True


# ───────────────────────────────────────────
# MAIN
# ───────────────────────────────────────────
if __name__ == "__main__":

    # Auto detect ALL cores
    CORES = mp.cpu_count()

    # Matrix size
    MATRIX_SIZE = 8000

    # System info
    os_name = platform.system()
    os_version = platform.release()
    os_full = f"{os_name} {os_version}"

    cpu_name = platform.processor()
    if not cpu_name:
        try:
            cpu_name = os.popen("cat /proc/cpuinfo | grep 'model name' | head -1").read().split(":")[1].strip()
        except:
            cpu_name = "Unknown CPU"


    print("===========================================")
    print("   FULL CPU BENCHMARK USING ALL CORES")
    print("===========================================\n")
    print(f"Operating System: {os_full}")
    print(f"CPU: {cpu_name}")
    print(f"Detected Cores: {CORES}")
    print(f"Matrix Size: {MATRIX_SIZE} x {MATRIX_SIZE}")
    print("\nRunning benchmark...\n")


    # --------------------------------------------
    # 1. Speed Per Core
    # --------------------------------------------
    per_core_times = []
    for i in range(CORES):
        t = single_core_test(MATRIX_SIZE)
        per_core_times.append(t)
        print(f"Core {i+1}: {t:.4f} seconds")


    # --------------------------------------------
    # 2. Speed Using ALL CORES
    # --------------------------------------------
    t0 = time.time()
    with mp.Pool(CORES) as pool:
        pool.map(worker_compute, [MATRIX_SIZE] * CORES)
    t1 = time.time()

    total_time = t1 - t0

    print("\n===========================================")
    print("   RESULTS")
    print("===========================================")
    print(f"Average per-core time: {np.mean(per_core_times):.4f} seconds")
    print(f"All cores parallel time: {total_time:.4f} seconds")


    # --------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------
    filename = f"benchmark_results_{os_name}.txt"

    with open(filename, "w") as f:
        f.write("=== CPU BENCHMARK RESULTS ===\n")
        f.write(f"Timestamp: {datetime.now()}\n\n")
        f.write(f"Operating System: {os_full}\n")
        f.write(f"CPU: {cpu_name}\n")
        f.write(f"Detected Cores: {CORES}\n")
        f.write(f"Matrix Size: {MATRIX_SIZE}\n\n")

        f.write("--- Per-Core Times ---\n")
        for i, t in enumerate(per_core_times):
            f.write(f"Core {i+1}: {t:.4f} seconds\n")

        f.write("\n--- Parallel Performance ---\n")
        f.write(f"All cores time: {total_time:.4f} seconds\n")

    print(f"\nSaved results to: {filename}")
