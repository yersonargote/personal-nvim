Vim�UnDo� �ݔ���{�`�_p�M����{��u���H=   h                                  `nS�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             `n!�     �                   �               5��                                         S       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `n"     �         	    �         	    5��                                         (       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `n"     �                  5��                                                  5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             `n"     �   
            �   
            5��    
               `       {               �      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `n",    �          j      from pirinola import Pirinola5��                                                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `n"0    �   i               �   h   j                  game.list_players()�   g   i                  print('Lista General')�   f   h           �   e   g          #            print('No hay ganador')�   d   f                  else:�   c   e           �   b   d                      )�   a   c          P                f'Ganador {ganador.get_name()} con {ganador.get_chips()} fichas'�   `   b                      print(�   _   a                  if ganador is not None:�   ^   `          #        ganador = game.get_winner()�   ]   _                  print(f'{game.name}')�   \   ^              for game in pirinola.games:�   [   ]          def list_games():�   Z   \           �   Y   [           �   X   Z                  game_id += 1�   W   Y          @        pirinola.players = list(pirinola.games[game_id].players)�   V   X          /        pirinola.games[game_id].delete_losers()�   U   W          .        pirinola.games[game_id].start_shifts()�   T   V          /        pirinola.games[game_id].calculate_pot()�   S   U          $    if pirinola.start_game(game_id):�   R   T              global game_id�   Q   S           �   P   R          /    pirinola.set_number_players(number_players)�   O   Q                      continue�   N   P          7            print('Digite un numero mayor o igual a 2')�   M   O                  if number_players < 2:�   L   N          B            input("Digite numero de Jugadores que van a jugar: "))�   K   M                  number_players = int(�   J   L              while number_players < 2:�   I   K           �   H   J          2    print(f'numero de jugadores {number_players}')�   G   I          *    number_players = len(pirinola.players)�   F   H          def start_new_game():�   E   G           �   D   F           �   C   E              print_limit()�   B   D          H    print('|', ' 3...Salir                                    | (exit)')�   A   C          H    print('|', ' 2...Listar partidas                          | (list)')�   @   B          I    print('|', ' 1...Empezar partida                          | (start)')�   ?   A              print_limit()�   >   @              """Print the menu"""�   =   ?          def print_menu():�   <   >           �   ;   =           �   :   <              print('|', '-' * 45, '|')�   9   ;          '    """Print a line to limit content"""�   8   :          def print_limit():�   7   9           �   6   8           �   5   7                  os.system("clear")�   4   6          	    else:�   3   5                  os.system("cls")�   2   4              if os.name == "nt":�   1   3              """Clean screen"""�   0   2          def clean_screen():�   /   1           �   .   0           �   -   /                  clean_screen()�   ,   .          	    else:�   +   -           �   *   ,                  list_games()�   )   +              elif option == 2:�   (   *           �   '   )                  start_new_game()�   &   (              if option == 1:�   %   '          3    """Call the function depending on the option"""�   $   &          def menu(option):�   #   %           �   "   $           �   !   #              return option�       "              clean_screen()�      !                      option = 0�                         else:�                .            option = options.index(option) + 1�                        if option in options:�                    except ValueError:�                        option = int(option)�                    try:�                    print_limit()�                5    option = input('| Digite su Opcion..         | ')�                    """Request the option"""�                def request_option():�                 �                 �                        menu(option)�                 �                            break�                        if option == EXIT:�                 �                !        option = request_option()�                        print_menu()�                    while True:�   
             def main():�   	              �      
           �      	          game_id = 0�                pirinola = Pirinola()�                 �                EXIT = 3�                #options = ('start', 'list', 'exit')�                 �                	import os�                 from ./pirinola import Pirinola5��                                                �               	       	           	       	       �                           *                       �               #       #   +       #       #       �                         O                     �                           X                       �                         Y                     �                         o                     �                           {                       �    	                       |                       �    
                     }                     �                         �                     �                         �                     �               !       !   �       !       !       �                           �                       �                         �                     �                         �                     �                           �                       �                         �                     �                                                 �                                                 �                                             �                         ,                    �               5       5   I      5       5       �                                             �                         �                    �                         �                    �                         �                    �                         �                    �               .       .   �      .       .       �                                             �                         )                    �                          @                    �    !                     S                    �    "                       e                      �    #                       f                      �    $                     g                    �    %           3       3   y      3       3       �    &                     �                    �    '                     �                    �    (                       �                      �    )                     �                    �    *                     �                    �    +                                             �    ,           	       	         	       	       �    -                                         �    .                       (                      �    /                       )                      �    0                     *                    �    1                     >                    �    2                     U                    �    3                     m                    �    4           	       	   �      	       	       �    5                     �                    �    6                       �                      �    7                       �                      �    8                     �                    �    9           '       '   �      '       '       �    :                     �                    �    ;                                             �    <                                             �    =                                         �    >                                         �    ?                     3                    �    @           I       I   E      I       I       �    A           H       H   �      H       H       �    B           H       H   �      H       H       �    C                     !                    �    D                       3                      �    E                       4                      �    F                     5                    �    G           *       *   K      *       *       �    H           2       2   v      2       2       �    I                       �                      �    J                     �                    �    K                     �                    �    L           B       B   �      B       B       �    M                     )                    �    N           7       7   H      7       7       �    O                     �                    �    P           /       /   �      /       /       �    Q                       �                      �    R                     �                    �    S           $       $   �      $       $       �    T           /       /   �      /       /       �    U           .       .   .      .       .       �    V           /       /   ]      /       /       �    W           @       @   �      @       @       �    X                     �                    �    Y                       �                      �    Z                       �                      �    [                     �                    �    \                     �                    �    ]                                         �    ^           #       #   5      #       #       �    _                     Y                    �    `                     y                    �    a           P       P   �      P       P       �    b                     �                    �    c                       �                      �    d                     �                    �    e           #       #   �      #       #       �    f                       	                      �    g                     	                    �    h                     >	                    �    i                      Z	                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `n"T     �          i      from ./pirinola import Pirinola5��                                                5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             `n"T    �          i      from /pirinola import Pirinola5��                                                5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             `n$�    �          i      from pirinola import Pirinola5��                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              5�_�   	              
      
    ����                                                                                                                                                                                                                                                                                                                                                             `n$�   	 �          i      from logic import Pirinola5��        
                  
                      �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              �                                              5�_�   
                 I        ����                                                                                                                                                                                                                                                                                                                                                             `n+4    �   H   I          2    print(f'numero de jugadores {number_players}')5��    H                      z      3               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `nQ�     �         i              �         h    5��                                        	       �                                               �                                             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `nR     �                        returnu5��                                               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `nR     �         i              �         h    5��                                        	       �                                               �                                             �                                             �                                             �                                             �                                             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `nR	     �                        request_option()5��                                               5�_�                    ;        ����                                                                                                                                                                                                                                                                                                                                                             `nR     �   ;   =   i          �   ;   =   h    5��    ;                      
                     �    ;                                          �    ;                                        �    ;                                        �    ;                                        �    ;                                        �    ;                                        5�_�                    <       ����                                                                                                                                                                                                                                                                                                                                                             `nR    �   ;   <              if(1 == treu)5��    ;                      
                     5�_�                    \        ����                                                                                                                                                                                                                                                                                                                                                             `nS�     �   \   ^   i              �   \   ^   h    5��    \                      �                     �    \                     �                    �    \                    �                    �    \                    �                    �    \                    �                    �    \                    �                    �    \                 	   �             	       5�_�                     ]       ����                                                                                                                                                                                                                                                                                                                                                             `nS�    �   \   ]                  for game in pirinola.5��    \                      �                     5��