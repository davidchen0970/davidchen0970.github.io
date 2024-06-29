<<<<<<< HEAD
document.addEventListener("DOMContentLoaded", function () {
  const githubUsername = "davidchen0970";
  const reposUrl = `https://api.github.com/users/${githubUsername}/repos`;

  fetch(reposUrl)
    .then((response) => response.json())
    .then((repos) => {
      const repoList = document.getElementById("repo-list");
      repoList.innerHTML = ""; // 清空初始內容

      repos.forEach((repo) => {
        const col = document.createElement("div");
        col.className = "col-12";
        col.setAttribute("style", "padding: 0 15px 15px 15px;");

        const card = document.createElement("div");
        card.className = "card";

        const cardBody = document.createElement("div");
        cardBody.className = "card-body";

        const repoHeader = document.createElement("h5");
        repoHeader.className = "card-header";

        const repoLink = document.createElement("a");
        repoLink.className = "nav-link";
        repoLink.href = `https://github.com/${githubUsername}/${repo.name}`;
        repoLink.textContent = repo.name;
        repoLink.target = "_blank";

        const readmeContent = document.createElement("div");
        readmeContent.className = "card-text scroll";
        readmeContent.textContent = "正在加載 README.md 內容...";

        cardBody.appendChild(readmeContent);
        card.appendChild(repoHeader);
        repoHeader.appendChild(repoLink);
        card.appendChild(cardBody);
        col.appendChild(card);
        repoList.appendChild(col);

        const readmeUrl = `https://raw.githubusercontent.com/${githubUsername}/${repo.name}/main/README.md`;

        fetch(readmeUrl)
          .then((response) => {
            if (response.ok) {
              return response.text();
            } else {
              throw new Error("無法加載 README.md");
            }
          })
          .then((data) => {
            readmeContent.innerHTML = marked.parse(data);
          })
          .catch((error) => {
            readmeContent.textContent = "無法加載 README.md 內容";
            console.error("Error fetching README.md:", error);
          });
      });
    })
    .catch((error) => {
      const repoList = document.getElementById("repo-list");
      repoList.textContent = "無法加載 repositories 列表";
      console.error("Error fetching repositories:", error);
    });
});
=======
document.addEventListener("DOMContentLoaded", function () {
  const githubUsername = "davidchen0970";
  const reposUrl = `https://api.github.com/users/${githubUsername}/repos`;

  fetch(reposUrl)
    .then((response) => response.json())
    .then((repos) => {
      const repoList = document.getElementById("repo-list");
      repoList.innerHTML = ""; // 清空初始內容

      repos.forEach((repo) => {
        const col = document.createElement("div");
        col.className = "col-12";
        col.setAttribute("style", "padding: 0 15px 15px 15px;");

        const card = document.createElement("div");
        card.className = "card";

        const cardBody = document.createElement("div");
        cardBody.className = "card-body";

        const repoHeader = document.createElement("h5");
        repoHeader.className = "card-header";

        const repoLink = document.createElement("a");
        repoLink.className = "nav-link";
        repoLink.href = `https://github.com/${githubUsername}/${repo.name}`;
        repoLink.textContent = repo.name;
        repoLink.target = "_blank";

        const readmeContent = document.createElement("div");
        readmeContent.className = "card-text scroll";
        readmeContent.textContent = "正在加載 README.md 內容...";

        cardBody.appendChild(readmeContent);
        card.appendChild(repoHeader);
        repoHeader.appendChild(repoLink);
        card.appendChild(cardBody);
        col.appendChild(card);
        repoList.appendChild(col);

        const readmeUrl = `https://raw.githubusercontent.com/${githubUsername}/${repo.name}/main/README.md`;

        fetch(readmeUrl)
          .then((response) => {
            if (response.ok) {
              return response.text();
            } else {
              throw new Error("無法加載 README.md");
            }
          })
          .then((data) => {
            readmeContent.innerHTML = marked.parse(data);
          })
          .catch((error) => {
            readmeContent.textContent = "無法加載 README.md 內容";
            console.error("Error fetching README.md:", error);
          });
      });
    })
    .catch((error) => {
      const repoList = document.getElementById("repo-list");
      repoList.textContent = "無法加載 repositories 列表";
      console.error("Error fetching repositories:", error);
    });
});
>>>>>>> 6984ff432b49b8561aaf51e2c424e80cb86f290a
