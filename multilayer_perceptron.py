import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

inputs = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

outputs_wanted = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])


np.random.seed(1)

input_layer_neurons = 4  # Giriş sayısı: 4
hidden_layer_neurons = 4        # Gizli katman nöron sayısı: 4
output_layer_neurons = 2       # Çıkış nöronları: 2


weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))


learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # İleri yayılım
    hidden_layer_net_matrix = np.dot(inputs, weights_input_hidden)
    hidden_layer_output_matrix = sigmoid(hidden_layer_net_matrix)

    output_layer_net_matrix = np.dot(hidden_layer_output_matrix, weights_hidden_output)
    predicted_output_matrix = sigmoid(output_layer_net_matrix)


    error = outputs_wanted - predicted_output_matrix

    total_error = np.sum(np.square(error)) / 2  # Toplam hata

    # geri yayılımı
    predicted_output_matrix_d = error * sigmoid_derivative(predicted_output_matrix)

    error_hidden_layer_matrix = predicted_output_matrix_d.dot(weights_hidden_output.T)
    hidden_layer_matrix_d = error_hidden_layer_matrix * sigmoid_derivative(hidden_layer_output_matrix)

    # Ağırlık güncelleme
    weights_hidden_output += hidden_layer_output_matrix.T.dot(predicted_output_matrix_d) * learning_rate
    weights_input_hidden += inputs.T.dot(hidden_layer_matrix_d) * learning_rate

    # Her 100 adımda toplam hatayı ekrana yazdırma
    if epoch % 1000 == 0:
        print(f"Epoch {epoch} - Toplam Hata: {total_error}")


print(f"Toplam Hata: {total_error}")
