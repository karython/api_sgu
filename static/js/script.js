const apiBase = "http://localhost:5000/usuario";
const modal = new bootstrap.Modal(document.getElementById("modalResposta"));

function mostrarMensagem(msg) {
    document.getElementById("mensagemResposta").innerText = msg;
    modal.show();
}

document.getElementById("formUsuario").addEventListener("submit", async (e) => {
    e.preventDefault();
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    const payload = { nome, email, senha };

    try {
        const response = await fetch(apiBase, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        mostrarMensagem(data.message || "Usuário cadastrado com sucesso!");
        if (response.ok) document.getElementById("formUsuario").reset();
    } catch {
        mostrarMensagem("Erro ao cadastrar.");
    }
});

async function buscarUsuario() {
    const id = document.getElementById("id_usuario").value;
    if (!id) return mostrarMensagem("Informe um ID para buscar.");

    try {
        const response = await fetch(`${apiBase}/${id}`);
        const data = await response.json();

        if (response.ok) {
            document.getElementById("nome").value = data.nome;
            document.getElementById("email").value = data.email;
            mostrarMensagem("Usuário encontrado.");
        } else {
            mostrarMensagem(data.message || "Usuário não encontrado.");
        }
    } catch {
        mostrarMensagem("Erro ao buscar usuário.");
    }
}

async function editarUsuario() {
    const id = document.getElementById("id_usuario").value;
    if (!id) return mostrarMensagem("Informe um ID para editar.");

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    const payload = { nome, email, senha };

    try {
        const response = await fetch(`${apiBase}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        mostrarMensagem(data.message || "Usuário atualizado.");
    } catch {
        mostrarMensagem("Erro ao editar usuário.");
    }
}

async function excluirUsuario() {
    const id = document.getElementById("id_usuario").value;
    if (!id) return mostrarMensagem("Informe um ID para excluir.");

    try {
        const response = await fetch(`${apiBase}/${id}`, {
            method: "DELETE"
        });

        const data = await response.json();
        mostrarMensagem(data.message || "Usuário excluído.");

        if (response.ok) document.getElementById("formUsuario").reset();
    } catch {
        mostrarMensagem("Erro ao excluir usuário.");
    }
}
