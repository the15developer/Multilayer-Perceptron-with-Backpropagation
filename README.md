EN

# Multilayer-Perceptron-with-Backpropagation

Overview

This project implements a simple multilayer perceptron (MLP) neural network using Python. The MLP consists of an input layer, one hidden layer, and an output layer. It is trained using the backpropagation algorithm to learn a binary classification task based on provided training data.

Features

Sigmoid Activation Function: The network uses the sigmoid activation function for both hidden and output layers.

Backpropagation Algorithm: Implements the backpropagation algorithm for training the network, allowing it to adjust weights based on the error.

Training Data: The network is trained on a small dataset with binary outputs based on four input features.

Error Monitoring: The total error is calculated and displayed during the training process, allowing for monitoring of learning progress.

Training Data
The training dataset consists of four input features and two output classes:

Input Features:
X1,X2,X3,X4

Target Outputs:
HEDEF1,HEDEF2

The dataset is defined as follows:

X1	X2	X3	X4  	HEDEF1	HEDEF2
1	  0	  0  	0	    0	      0
0	  1	  0  	0   	0	      1
0  	0 	1	  0	    1	      0
0  	0  	0 	1	    1     	1

Results
The script will output the total error at each epoch, allowing you to observe how the error decreases over time as the network learns.


TR 

# Çok Katmanlı Algılayıcı-Geri-Yayılımlı

Genel Bakış

Bu proje, Python kullanarak basit bir çok katmanlı algılayıcı (MLP) sinir ağı uygular. MLP, bir giriş katmanı, bir gizli katman ve bir çıktı katmanından oluşur. Sağlanan eğitim verilerine dayalı ikili bir sınıflandırma görevi öğrenmek için geri yayılım algoritması kullanılarak eğitilir.

Özellikler

Sigmoid Aktivasyon Fonksiyonu: Ağ, hem gizli hem de çıktı katmanları için sigmoid aktivasyon fonksiyonunu kullanır.

Geri Yayılım Algoritması: Ağı eğitmek için geri yayılım algoritmasını uygular ve hataya göre ağırlıkları ayarlamasına olanak tanır.

Eğitim Verileri: Ağ, dört giriş özelliğine dayalı ikili çıktılara sahip küçük bir veri kümesi üzerinde eğitilir.

Hata İzleme: Toplam hata, eğitim süreci sırasında hesaplanır ve görüntülenir ve öğrenme ilerlemesinin izlenmesine olanak tanır.

Eğitim Verileri
Eğitim veri kümesi dört giriş özelliği ve iki çıkış sınıfından oluşur:

Giriş Özellikleri:
X1,X2,X3,X4

Hedef Çıktılar:
HEDEF1,HEDEF2

Veri kümesi aşağıdaki gibi tanımlanır:

X1	X2	X3	X4  	HEDEF1	HEDEF2
1	  0	  0  	0	    0	      0
0	  1	  0  	0   	0	      1
0  	0 	1	  0	    1	      0
0  	0  	0 	1	    1     	1

Sonuçlar
Program her epoch'ta toplam hatayı çıktı olarak verir ve böylece ağ öğrendikçe hatanın zamanla nasıl azaldığını gözlemlemenize olanak tanır.

