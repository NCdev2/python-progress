#from qiskit import QuantumCircuit, Aer, execute
import qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Quantum circuit for Deutsch's Algorithm
qc = QuantumCircuit(2, 1)

# Initialize second qubit in |1>
qc.x(1)
qc.h([0, 1])

# Oracle: Define if function is constant or balanced
qc.cx(0, 1)

# Measurement
qc.h(0)
qc.measure(0, 0)

# Execute
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Deutsch's Algorithm result:", counts)
