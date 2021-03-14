import numpy as np

def euler(equations,initials,dt,tf,ti):
	def delta_next(eqs, paras):
	# calcultes the derivative at a certain timestep for each equation
		return np.array(list(map(
			lambda x : x(*paras),
			eqs
		)))

	results = [[i] for i in initials]
	ts      = [ti]
	# initializes the intial arrays
	num_eq  = len(equations)
	# variable to store the number of equations. Used to dictate the length of a loop
	steps   = int((tf-ti)/dt)
	# determines the number of time steps based on the final & initial conditions & delta t

	for _ in range(steps):
	# loop to increment through each time step except the last
		ts.append(ts[-1] + dt)
		parameters = [i[-1] for i in results]
		# creates a list of the inital conditions for the time step
		new_vals = np.array(parameters) + dt * delta_next(equations, parameters)
		# leverages numpy SIMD to calculate the value for the current time step
		for i in range(num_eq):
		# loop to calculate the value for each variable within a certain step
			results[i].append(new_vals[i])
			# value calculted via Euler's metheod added to it's perspective list
	return [results,ts]

if __name__ == '__main__':
	x = lambda x , y : y
	y = lambda x , y : -2*x-3*y
	result, times = euler([x,y],[1,1],0.25,5,0)
	result = [i[-1] for i in result]
	print(f'the result is: <{result[0]}, {result[1]}>')
