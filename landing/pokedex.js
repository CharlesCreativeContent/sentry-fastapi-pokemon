const searchBtn = document.getElementById("search-btn"); // search button
const inputField = document.getElementById("name-input"); // search field input
const nameScreen = document.getElementById("name-screen"); //name-screen
const imageScreen = document.getElementById("main-screen"); // image screen
const aboutScreen = document.getElementById("about-screen"); // about-text screen
const typeScreen = document.getElementById("type-screen"); // type screen
const idScreen = document.getElementById("id-screen"); // spices screen
const jsonBtn = document.getElementById("json"); // json button

const getPokemonData = (pokemon) => {
  fetch(`https://sentry-fastapi-demo.vercel.app/pokemon/${pokemon}`)
  .then((data) => data.json())
    .then((data) => {
console.log(data)

      let id = ("00" + data.id).slice(-3);
      jsonBtn.href = `https://sentry-fastapi-demo.vercel.app/pokemon/${pokemon}`
      imageScreen.style.backgroundImage = `url('https://assets.pokemon.com/assets/cms2/img/pokedex/full/${id}.png')`;
      nameScreen.innerHTML = data.name;
      typeScreen.innerHTML = data.types[0];
      idScreen.innerHTML = `#${data.id}`;
      aboutScreen.innerHTML = `Height: ${data.height * 10}cm Weight: ${
        data.weight / 10
      }kg`;
      inputField.value = "";
    });
};

inputField.addEventListener(
  "keydown",
  (event) => event.key === "Enter" && searchBtn.click()
);
searchBtn.addEventListener("click", () => getPokemonData(inputField.value));
