from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a circuit with 3 qubits
qc = QuantumCircuit(3, 2)

# Step 1: Create entanglement between qubit 1 and qubit 2
qc.h(1)
qc.cx(1, 2)

# Step 2: Teleport the state from qubit 0 to qubit 2
qc.cx(0, 1)
qc.h(0)

# Measurement
qc.measure(0, 0)
qc.measure(1, 1)

# Perform conditional operations based on measurement results
qc.cx(1, 2)
qc.cz(0, 2)

# Execute
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Quantum Teleportation result:", statevector)
