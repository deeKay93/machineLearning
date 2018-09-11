cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_))
training_step =tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function, global_step)
