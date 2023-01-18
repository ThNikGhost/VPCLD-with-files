from rich.tree import Tree
from rich import print as rprint
from rich.console import Console
import os

'''tree = Tree('Family Tree')
tree.add('Mom')
tree.add('Dad')
tree.add('Brother').add('Wife')
tree.add('[red]Sister').add('[green]Husband').add('[darkblue]Son')
'''
os.system('cls')
tree = Tree('[red]Что хотите сделать?')
tree_1 = tree.add('[green]1.Вывести список.')
tree_1.add('[blue]1.Вывести список запланированных аниме.')
tree_1.add('[blue]2.Вывести список просмотренных аниме.')
tree_1.add('[blue]3.Вывести список брошенных аниме.')
tree_1.add('[blue]4.Вывести список любимых аниме.')

tree_2 = tree.add('[green]2.Пометить аниме(брошенное, просмотренное, любимое).')
tree_2.add('[blue]1.Пометить брошенное')
tree_2.add('[blue]2.Пометить просмотренное')
tree_2.add('[blue]3.Пометить любимое')

tree.add('[green]3.Вывести рандомное аниме.')



rprint(tree)
