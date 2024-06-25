public class Livro {
    private int id;
    private String titulo;
    private String autor;
    private int anoPublicacao;

    public Livro(int id, String titulo, String autor, int anoPublicacao) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
    }

    public int getId() {
        return id;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    @Override
    public String toString() {
        return "Livro [ID=" + id + ", Titulo=" + titulo + ", Autor=" + autor + ", Ano de Publicacao=" + anoPublicacao + "]";
    }
}
