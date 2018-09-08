training_step =tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function, global_step)
