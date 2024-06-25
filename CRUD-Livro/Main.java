import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();
        Scanner scanner = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\nSistema de Gestão de Biblioteca");
            System.out.println("1. Adicionar Livro");
            System.out.println("2. Buscar Livro por ID");
            System.out.println("3. Remover Livro por ID");
            System.out.println("4. Listar Livros");
            System.out.println("5. Adicionar Usuario");
            System.out.println("6. Buscar Usuario por ID");
            System.out.println("7. Remover Usuario por ID");
            System.out.println("8. Listar Usuarios");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opcao: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Consome a nova linha

            switch (opcao) {
                case 1:
                    System.out.print("ID do Livro: ");
                    int livroId = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Titulo do Livro: ");
                    String titulo = scanner.nextLine();
                    System.out.print("Autor do Livro: ");
                    String autor = scanner.nextLine();
                    System.out.print("Ano de Publicacao: ");
                    int ano = scanner.nextInt();
                    Livro livro = new Livro(livroId, titulo, autor, ano);
                    biblioteca.adicionarLivro(livro);
                    break;
                case 2:
                    System.out.print("ID do Livro: ");
                    livroId = scanner.nextInt();
                    livro = biblioteca.buscarLivroPorId(livroId);
                    if (livro != null) {
                        System.out.println(livro);
                    } else {
                        System.out.println("Livro não encontrado.");
                    }
                    break;
                case 3:
                    System.out.print("ID do Livro: ");
                    livroId = scanner.nextInt();
                    if (biblioteca.removerLivroPorId(livroId)) {
                        System.out.println("Livro removido com sucesso.");
                    } else {
                        System.out.println("Livro não encontrado.");
                    }
                    break;
                case 4:
                    biblioteca.listarLivros();
                    break;
                case 5:
                    System.out.print("ID do Usuario: ");
                    int usuarioId = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nome do Usuario: ");
                    String nome = scanner.nextLine();
                    System.out.print("Email do Usuario: ");
                    String email = scanner.nextLine();
                    Usuario usuario = new Usuario(usuarioId, nome, email);
                    biblioteca.adicionarUsuario(usuario);
                    break;
                case 6:
                    System.out.print("ID do Usuario: ");
                    usuarioId = scanner.nextInt();
                    usuario = biblioteca.buscarUsuarioPorId(usuarioId);
                    if (usuario != null) {
                        System.out.println(usuario);
                    } else {
                        System.out.println("Usuario não encontrado.");
                    }
                    break;
                case 7:
                    System.out.print("ID do Usuario: ");
                    usuarioId = scanner.nextInt();
                    if (biblioteca.removerUsuarioPorId(usuarioId)) {
                        System.out.println("Usuario removido com sucesso.");
                    } else {
                        System.out.println("Usuario não encontrado.");
                    }
                    break;
                case 8:
                    biblioteca.listarUsuarios();
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida.");
                    break;
            }
        } while (opcao != 0);

        scanner.close();
    }
}
