def generate_partitions(a_list):
	if len(a_list) == 1:
		return [[a_list]]
	test = a_list.copy()
	a = test.pop(0)
	todas_particoes = generate_partitions(test)
	c = []
	for p in todas_particoes:
		q = p.copy()+[[a]]
		c.append(q)
		for i in range(len(p)):
			nova_part = []
			for j in range(len(p)):
				if j == i:
					nova_part.append(p[i]+[a])
				else:
					nova_part.append(p[j])

			c.append(nova_part)

	return c


example = [0,1,2,3,4,5]
print(generate_partitions(example))
