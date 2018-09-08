
def multilayer_perceptron(x, weights, biases):
    # Hidden Layer 1
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.sigmoid(layer_1)
    
    # Hidden Layer 2
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.sigmoid(layer_2)
    
    # Hidden Layer 3
    layer_2 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    layer_2 = tf.nn.sigmoid(layer_3)
    
    # Output Layer
    out_layer = tf.matmul(layer_3, weights['out'])+ biases['out']
    return out_layer

    cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_))
