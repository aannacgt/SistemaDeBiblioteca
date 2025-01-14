# Este teste verifica o comportamento da classe 'Livro' em relação à disponibilidade de um livro.
# Ele simula um ciclo completo de empréstimo e devolução, onde o estado de disponibilidade do livro é monitorado em cada etapa.
# O objetivo é garantir que a classe 'Livro' esteja manipulando corretamente a disponibilidade do livro durante o ciclo de empréstimo e devolução.
from src.livro import Livro

livro = Livro("1984", "George Orwell")

print(f"Disponível? {livro.disponibilidade}")
livro.emprestar_livro("2024-12-01")
print(f"Disponível após emprestado? {livro.disponibilidade}")
livro.devolver_livro()
print(f"Disponível após devolução? {livro.disponibilidade}")
