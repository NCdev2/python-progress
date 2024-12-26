from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import Aer
from qiskit import execute  # Corrected import

# Set hidden bit string s (e.g., '101')
s = '101'
n = len(s)

# Create a circuit with n+1 qubits and n classical bits
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit to |1>
qc.x(n)
qc.h(range(n + 1))

# Oracle: apply CNOT if s_i is 1
for i, bit in enumerate(s):
    if bit == '1':
        qc.cx(i, n)

# Measurement
qc.h(range(n))
qc.measure(range(n), range(n))

# Execute
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Bernstein-Vazirani Algorithm result:", counts)

# Optional: visualize the results
plot_histogram(counts)
