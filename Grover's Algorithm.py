from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import MCXGate
from qiskit.visualization import plot_histogram

# Set number of qubits
n = 2
qc = QuantumCircuit(n)

# Initialize in superposition
qc.h(range(n))

# Oracle (mark |11> as the solution)
qc.cz(0, 1)

# Grover Diffusion Operator
qc.h(range(n))
qc.x(range(n))
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x(range(n))
qc.h(range(n))

# Measurement
qc.measure_all()

# Execute
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Grover's Algorithm result:", counts)
