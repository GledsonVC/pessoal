class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete 
        self.compositor = compositor 
        self.ano = ano

class Buscador:
    def buscaPorTitulo(self, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:
                return i
        return -1

    def vamosBuscar(self):
        playlist = [ Musica('Ponta de Areia', 'Milton Nascimento', 'Milton Nascimento', 1975),
                     Musica('Pobres Poderes', 'Caetano Veloso', 'Caetano Veloso', 1984),
                     Musica('Baby', 'Gal Costa', 'Caetano Veloso', 1975)]

        ondeAchou = self.buscaPorTitulo(playlist, 'Baby')

        if ondeAchou == -1:
            print('Minha musica preferida não está na playlist')
        else:
            preferida  =  playlist[ondeAchou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano,
                  sep = ', ')
        
