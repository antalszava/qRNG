import qrng
from qiskit import IBMQ

token = ''
qrng.set_provider_as_IBMQ(token) #the IBMQ API token from your dashboard
qrng.set_backend('ibmq_belem') #connect to the 5 qubit 'ibmq_london' quantum computer

qrng.set_provider_as_IBMQ(token) #the IBMQ API token from your dashboard
#qrng.set_backend()

indices = []
cnt = 0
print(qrng.get_random_float(0,1))
while len(indices) < 10:
    cnt += 1
    var = qrng.get_random_int(0, 9) #generate a random 32 bit integer
    if var not in indices:
        indices.append(var)
    print(indices, cnt)
