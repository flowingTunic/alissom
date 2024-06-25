import java.util.LinkedList;

public class Biblioteca {
    private LinkedList<Livro> livros;
    private LinkedList<Usuario> usuarios;

    public Biblioteca() {
        livros = new LinkedList<>();
        usuarios = new LinkedList<>();
    }

    // Métodos para gerenciar livros
    public void adicionarLivro(Livro livro) {
        livros.add(livro);
    }

    public Livro buscarLivroPorId(int id) {
        for (Livro livro : livros) {
            if (livro.getId() == id) {
                return livro;
            }
        }
        return null;
    }

    public boolean removerLivroPorId(int id) {
        Livro livro = buscarLivroPorId(id);
        if (livro != null) {
            livros.remove(livro);
            return true;
        }
        return false;
    }

    public void listarLivros() {
        livros.sort((Livro l1, Livro l2) -> Integer.compare(l1.getId(), l2.getId()));
        for (Livro livro : livros) {
            System.out.println(livro);
        }
    }

    // Métodos para gerenciar usuários
    public void adicionarUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    public Usuario buscarUsuarioPorId(int id) {
        for (Usuario usuario : usuarios) {
            if (usuario.getId() == id) {
                return usuario;
            }
        }
        return null;
    }

    public boolean removerUsuarioPorId(int id) {
        Usuario usuario = buscarUsuarioPorId(id);
        if (usuario != null) {
            usuarios.remove(usuario);
            return true;
        }
        return false;
    }

    public void listarUsuarios() {
        usuarios.sort((Usuario u1, Usuario u2) -> Integer.compare(u1.getId(), u2.getId()));
        for (Usuario usuario : usuarios) {
            System.out.println(usuario);
        }
    }
}
