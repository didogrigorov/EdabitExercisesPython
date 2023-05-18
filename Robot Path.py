def robot_path(commands):
	dest = [(3, 2), (-4, 3)]
	x = commands.count('e') - commands.count('w')
	y = commands.count('n') - commands.count('s')
	return (x, y) in dest

print(robot_path(['n', 's', 'n', 'n', 'e', 'n', 'w', 'w', 's', 'w', 'w', 'w', 'n']))