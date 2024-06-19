def hash(n):
	n = abs(n)
	hash_val = 305872493
	while n > 0:
		last_digit = n % 10
		hash_val = last_digit + (hash_val << 6) + (hash_val << 16) - hash_val
		n //= 10
		hash_val %= (2**32)
	
	return hash_val

def benchmark(n):
	hashes = [hash(i) for i in range(n)]
	collisions = 0
	for i, h in enumerate(hashes):
		if h in hashes[:i] or h in hashes[i+1:]:
			collisions += 1
	
	return collisions / len(hashes)

if __name__ == '__main__':
	print('Benchmark results:')
	print('    Collisions: %.02f%% (Lower is better)' % (benchmark(10000) * 100))
