import subprocess

"""
subprocess.call() recibe dos parámetros: primero el comando a ejecutar, segundo
le indicamos que tiene que correrlo en una terminal.
"""
subprocess.call("dir", shell=True)