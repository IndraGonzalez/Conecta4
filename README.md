# Conecta4
Primer trabajo de curso: Búsqueda con oponente - Juego de Conecta 4

	El fichero run.py, se ha modificado de manera que se pueda elegir si juega el humano contra la máquina o la máquina contra la máquina. Para ello, hemos creado dos funciones diferentes que simulan el juego de la máquina en los dos turnos (juega solo automáticamente) o que permiten jugar al humano.
	En el caso de que se elija la versión jugador contra máquina, se permite elegir el jugador que empieza la partida.  La asignación de variables se hace de la siguiente forma: Jugador -> O, Máquina -> X. 
	Todas estas opciones se hacen comprobando que lo que el usuario inserta sea correcto y dándole tres oportunidades. En caso de que se agoten, cada uno tiene un valor por defecto.
	Además, hemos hecho lo mismo para las dificultades, donde si se supera el límite de intentos se comienza con el nivel medio.
	Para la realización de las dificultades, se ha aumentado la profundidad conforme se aumenta de nivel:
	Nivel fácil, hemos llegado a un nivel de profundidad.
	Nivel medio, hemos llegado hasta dos niveles de profundidad.
	Nivel difícil, hemos llegado hasta cuatro niveles de profundidad.

	En el fichero games.py, hemos realizado una modificacion, para permitir que el jugador tenga el O y la máquina las X. Para ello hemos modificado la TicTacToe, pasandole en el constructor le pasamos la variable player con el jugador que, por defecto, es X.

	En el fichero heuristics.py hemos implementado la heurística:

		La heurística asigna un valor a cada uno de los tableros en función de los movimientos legales, que son aquellas posiciones inmediatamente superiores a aquellas ya ocupadas o que son el borde inferior horizontal. Para cada uno de los posibles movimientos, buscamos la facilidad que tiene de hacer 4 en raya. Para ello, recorremos las posiciones contiguas del tablero en horizontal, vertical y en diagonal en ambas direcciones (para ello se suma y se resta la variable del desplazamiento).
		Para ello llamamos al método find_connect, que nos devuelve una heuristica para dichos recorridos. Si encontramos un espacio, sumamos a la heurística parcial un 2 y si encontramos una ficha de nuestro jugador, sumamos 6.
		Le restamos 4 al final porque entra dos veces en la posición que vamos a explorar y, tras comprobar que era un punto (vacío) restamos 4 para que la heurística no tenga en cuenta la propia posición.
		Esto lo hacemos para el jugador y para el contrario, pero la heurísitica parcial del contrario se resta a la otra.
		Además, utilizamos la variable state.utility para que, en caso de que sea inminente nuestra victoria, vaya a esa posición sin dudas y en el caso de que la derrota sea inminente, también para que la impida.
		
	En cuanto a la repartición del trabajo, la parte general, el esqueleto de la práctica, tanto en la primera versión como en la segunda, la hemos realizado conjuntamente, Iraida Artiles Corvo e Indra González Cabrera.
	Sin embargo, surgieron ciertos errores que hacían que el funcionamiento no fuese óptimo en la última versión.
	
	La optimización del código y los dos apartados opcionales fueron realizados íntegramente por Indra González Cabrera.

