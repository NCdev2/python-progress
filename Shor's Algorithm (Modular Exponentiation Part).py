from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Function to calculate modular exponentiation circuit (controlled)
def mod_exp(a, power, N, n):
    qc = QuantumCircuit(n)
    # Apply control-unitary operation for a**power % N
    for i in range(power):
        qc.append(MCXGate(n), list(range(n))) # This simulates modular exp
    return qc

# Parameters
a = 2   # number to factor
N = 15  # modulus (the number we wish to factor)
n = 3   # number of qubits

qc = QuantumCircuit(n)

# Simplified modular exponentiation operation
mod_exp_circuit = mod_exp(a, 2, N, n)
qc.append(mod_exp_circuit, range(n))

# Execute
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Shor's Algorithm (Simplified) Modular Exponentiation result:", statevector)
