# Conecta4
Primer trabajo de curso: Búsqueda con oponente - Juego de Conecta 4

	En el fichero run.py, lo hemos modificado de manera que se pueda elegir el jugador que empieza la partida, comprobando que lo que el usuario inserta sea correcto y dándole tres oportunidades sino comenzará automáticamente la máquina. En caso que se desee empezar primero, se empezará con el círculo sino se le asignará al jugador la x.
	Posteriormente, hemos echo lo mismo para las dificultades, donde si se supera el límite de intentos se comienza con el nivel medio.
	Para la realización de las dificultades, se avanzado en un nivel mayor de profundidad, según el nivel.
	Nivel fácil, hemos llegado a un nivel de profundidad.
	Nivel medio, hemos llegado hasta dos niveles de profundidad.
	Nivel difícil, hemos llegado hasta cuatro niveles de profundidad.

	En el fichero games.py, hemos realizado una modificacion, para permitir que el jugador  que comience empiece con los O y al otro jugador se le asigne las X. Para ello hemos modificado la TicTacToe, pasandole en el constructor le pasamos la variable X. Hemos realizado lo mismo en la clase ConnectFour.


	En el fichero heuristics.py hemos implementado la heurística:

			En primer lugar, hemos usado el memoize() con la finalidad de que el juego vaya con mayor rapidez, para implementar el memoize, hemos definido una funcion, a la que le pasamos un argumento. Además hemos usado un dictionario memo, para guardar los resultados de la función, guardamos los estados del tablero que no se encuentran en el diccionario y lo devolvemos.

			Posteriormente, recorremos el tablero para en horizontal, hacia arriba , hacia abajo y en diagonal. Para ello llamamos al método find_connect, que nos devuelve una heuristica para dichos recorridos según si encontramos un espacio, al que le subamos 1, o si encontramos una ficha de nuestro jugador, al que le sumamos 5 a la heuristica. Recorremos el tablero hacia la izquierda restándole y hacia la derecha sumándole a nuestra variable encargada del movimiento en horizontal (i). Finalmente devolvemos la heurística.

