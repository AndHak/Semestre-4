# ANDRES FELIPE MARTINEZ GUERRA
# SEBASTIAN DAVID ORDOÑEZ BOLAÑOS 
from cola import Cola

class ColaPrioridad:
    """Clase que implementa el TAD Cola de Prioridad utilizando varias Colas.

    Parameters
    ----------
    niveles_prioridad : int
        Número de prioridades (niveles) en la cola de prioridad.
    """

    def __init__(self, niveles_prioridad: int):
        """Inicializa las colas según el número de prioridades.

        Parameters
        ----------
        niveles_prioridad : int
            Cantidad de niveles de prioridad.
        """
        self.colas = [Cola() for _ in range(niveles_prioridad)]
        self.niveles = niveles_prioridad

    def es_vacia(self) -> bool:
        """Verifica si todas las colas están vacías.

        Returns
        -------
        bool
            True si todas las colas están vacías, False en caso contrario.
        """
        return all(cola.es_vacia() for cola in self.colas)

    def encolar(self, nuevo_dato: object, prioridad: int) -> bool:
        """Agrega un nuevo dato a la cola correspondiente según su prioridad.

        Parameters
        ----------
        nuevo_dato : object
            El dato a ser encolado.
        prioridad : int
            Nivel de prioridad del dato.

        Returns
        -------
        bool
            True si el dato se encoló correctamente, False si la prioridad es inválida.
        """
        return 0 <= prioridad < self.niveles and self.colas[prioridad].encolar(nuevo_dato)

    def desencolar(self):
        """Desencola el primer dato de la cola con mayor prioridad (menor número).

        Returns
        -------
        object or None
            El dato desencolado o None si todas las colas están vacías.
        """
        return next((cola.desencolar() for cola in self.colas if not cola.es_vacia()), None)

    def frente(self):
        """Retorna el primer dato de la cola con mayor prioridad sin quitarlo.

        Returns
        -------
        object or None
            El dato en el frente o None si todas las colas están vacías.
        """
        return next((cola.frente() for cola in self.colas if not cola.es_vacia()), None)

    def __len__(self) -> int:
        """Retorna el número total de elementos en todas las colas.

        Returns
        -------
        int
            El número total de elementos.
        """
        return sum(len(cola) for cola in self.colas)

    def __str__(self) -> str:
        """Muestra las colas de prioridad en el formato de una cola normal.

        Returns
        -------
        str
            Una representación en cadena de las colas según su prioridad.
        """
        return "\n".join(f"Prioridad {i}: [{', '.join(map(str, cola))}]" for i, cola in enumerate(self.colas) if not cola.es_vacia())
