import time
import numpy as np
import multiprocessing as mp

def heavy_matrix_test(size):
    """
    Performs a heavy CPU test by multiplying two large matrices.
    """
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    start = time.time()
    C = A @ B
    end = time.time()

    return end - start


def auto_size():
    """
    Choose matrix size based on CPU count.
    Higher core count → larger matrix.
    """
    cores = mp.cpu_count()
    if cores <= 4:
        return 5000
    elif cores <= 8:
        return 5000
    else:
        return 5000


if __name__ == "__main__":
    total_cores = mp.cpu_count()

    # Use all cores only if more than 4
    if total_cores > 4:
        cores_to_use = total_cores
    else:
        cores_to_use = 4

    print("=== HIGH COMPUTATION CPU BENCHMARK ===")
    print(f"Detected CPU cores: {total_cores}")
    print(f"Cores used in benchmark: {cores_to_use}")

    size = auto_size()
    print(f"Matrix size used: {size} x {size}")

    print("\nRunning heavy matrix multiplications in parallel...\n")

    tasks = [size] * cores_to_use

    start_global = time.time()
    with mp.Pool(cores_to_use) as pool:
        results = pool.map(heavy_matrix_test, tasks)
    end_global = time.time()

    avg_time = sum(results) / len(results)
    total_time = end_global - start_global

    # GFLOPS estimation
    gflops_per_core = [(2 * size**3) / (t * 1e9) for t in results]
    total_gflops = sum(gflops_per_core)

    print("=== RESULTS ===")
    print(f"Average time per core: {avg_time:.3f} s")
    print(f"Total parallel time: {total_time:.3f} s")
    print(f"Total estimated performance: {total_gflops:.2f} GFLOPS")
