from livereload import Server, shell


if __name__ == '__main__':
    server = Server()
    server.watch('.', shell('make html', cwd='docs'))
    server.serve(root='.')