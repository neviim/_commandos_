# Instalando tensorflow

	::: https://www.tensorflow.org/install/pip

		$ virtualenv --system-site-packages -p python3 ./venv
		$ pip install --upgrade pip
		$ pip list 
		$ deactivate


		$ pip3 install jupyter pandas matplotlib scikit-learn

		$ pip install --upgrade tensorflow
		$ python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"


	::: Windows

		$ conda install python=3.6
		$ pip install tensorflow